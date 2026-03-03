import os
import json
from google.adk import Agent
from jira import JIRA
from jira.exceptions import JIRAError

def _get_jira_client() -> JIRA | None:
    """Helper to initialize the Jira client from environment variables."""
    server = os.environ.get("JIRA_SERVER")
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")

    if not all([server, email, token]):
        return None

    try:
        return JIRA(server=server, basic_auth=(email, token))
    except Exception as e:
        print(f"Failed to initialize Jira client: {e}")
        return None

def create_jira_ticket(title: str, description: str, project_key: str, issue_type: str = "Task") -> str:
    """Creates a new Jira ticket."""
    jira = _get_jira_client()
    if not jira:
        return "Error: Jira client not configured."

    try:
        issue_dict = {
            'project': {'key': project_key},
            'summary': title,
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = jira.create_issue(fields=issue_dict)
        return f"Created ticket {new_issue.key}: '{title}' ({issue_type})"
    except JIRAError as e:
        return f"Failed to create Jira ticket. Status code: {e.status_code}."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def get_jira_ticket(ticket_id: str) -> str:
    """Retrieves information about a Jira ticket."""
    jira = _get_jira_client()
    if not jira:
        return "Error: Jira client not configured."

    try:
        issue = jira.issue(ticket_id)
        status = issue.fields.status.name
        assignee = issue.fields.assignee.displayName if getattr(issue.fields, 'assignee', None) else "Unassigned"
        summary = issue.fields.summary
        return f"Ticket {ticket_id}: '{summary}' - Status: {status}. Assigned to: {assignee}."
    except JIRAError as e:
        return f"Failed to retrieve Jira ticket. Status code: {e.status_code}."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def get_agile_boards(project_keyword: str) -> str:
    """Finds Agile boards matching a project key or name keyword."""
    jira = _get_jira_client()
    if not jira:
        return "Error: Jira client not configured."

    try:
        boards = jira.boards(projectKeyOrId=project_keyword)
        if not boards:
            # Try by name if projectKeyOrId fails to match
            boards = [b for b in jira.boards() if project_keyword.lower() in getattr(b, 'name', '').lower()]

        if not boards:
            return f"No boards found matching '{project_keyword}'."

        results = []
        for board in boards[:5]: # Return top 5
            results.append(f"Board ID: {board.id}, Name: '{board.name}'")
        return "\n".join(results)
    except Exception as e:
        return f"Failed to retrieve boards: {e}"

def get_sprints(board_id: int, state: str = "active,future") -> str:
    """Gets sprints for a specific Agile board."""
    jira = _get_jira_client()
    if not jira:
        return "Error: Jira client not configured."

    try:
        sprints = jira.sprints(board_id=board_id, state=state)
        if not sprints:
            return f"No sprints found for board {board_id} in state '{state}'."

        results = []
        for sprint in sprints[:10]:
            results.append(f"Sprint ID: {sprint.id}, Name: '{sprint.name}', State: {sprint.state}")
        return "\n".join(results)
    except Exception as e:
        return f"Failed to retrieve sprints: {e}"

def get_sprint_metrics(board_id: int, sprint_id: int) -> str:
    """Gets metrics and issue data for a specific sprint, calculating burndown progress."""
    jira = _get_jira_client()
    if not jira:
        return "Error: Jira client not configured."

    try:
        jql = f"sprint = {sprint_id}"
        issues = jira.search_issues(jql, maxResults=100)

        total_issues = len(issues)
        done_issues = 0
        in_progress_issues = 0
        todo_issues = 0

        for issue in issues:
            status_category = getattr(getattr(issue.fields.status, 'statusCategory', None), 'name', '').lower()
            if status_category == 'done':
                done_issues += 1
            elif status_category == 'in progress':
                in_progress_issues += 1
            else:
                todo_issues += 1

        server_url = os.environ.get("JIRA_SERVER", "https://your-domain.atlassian.net")
        report_url = f"{server_url}/secure/RapidBoard.jspa?rapidView={board_id}&view=reporting&chart=sprintRetrospective&sprint={sprint_id}"

        completion_rate = (done_issues/total_issues*100) if total_issues > 0 else 0

        summary = (
            f"Sprint {sprint_id} Metrics:\n"
            f"- Total Issues: {total_issues}\n"
            f"- Done: {done_issues}\n"
            f"- In Progress: {in_progress_issues}\n"
            f"- To Do: {todo_issues}\n"
            f"Completion Rate (by issue count): {completion_rate:.1f}%\n"
            f"\nTo view the visual Sprint Report and Burndown Chart with auto-generated graphs, visit: {report_url}"
        )
        return summary
    except Exception as e:
        return f"Failed to retrieve sprint metrics: {e}"

def record_standup_update(user: str, update: str) -> str:
    """Records a user's update from the daily standup."""
    notes_file = "standup_notes.jsonl"
    try:
        with open(notes_file, "a") as f:
            record = {"user": user, "update": update}
            f.write(json.dumps(record) + "\n")
        return f"Successfully recorded standup update for {user}. Saved to {notes_file}."
    except Exception as e:
        return f"Error recording standup update for {user}: {e}"

agent = Agent(
    name="ScrumMasterAgent",
    instruction=(
        "You are an experienced Agile Scrum Master. "
        "Your responsibilities include running daily standups, helping the team "
        "unblock issues, and managing Jira tickets, sprints, and metrics. "
        "When a team member asks about sprint progress, sprint burnout, or metrics, "
        "use get_agile_boards to find their project, get_sprints to find the current sprint, "
        "and get_sprint_metrics to give them the breakdown and a URL to view the auto-generated visual graphs in Jira. "
        "When team members provide their updates, make sure to record them using the record_standup_update tool. "
        "If a team member mentions a new task or a bug, offer to create a Jira ticket for them using the create_jira_ticket tool, "
        "or create it directly if they provide enough details (including the project key). "
        "You can also look up existing tickets using the get_jira_ticket tool. "
        "Always be helpful, concise, and focused on helping the team deliver value."
    ),
    tools=[
        create_jira_ticket,
        get_jira_ticket,
        record_standup_update,
        get_agile_boards,
        get_sprints,
        get_sprint_metrics
    ],
)
