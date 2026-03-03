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
    """
    Creates a new Jira ticket.

    Args:
        title: The summary or title of the ticket.
        description: The detailed description of the ticket.
        project_key: The project key where the ticket should be created (e.g., 'PROJ').
        issue_type: The type of issue (e.g., Task, Bug, Story). Default is Task.

    Returns:
        The ID of the created ticket, or an error message if creation failed.
    """
    jira = _get_jira_client()
    if not jira:
        return "Error: Jira client not configured. Set JIRA_SERVER, JIRA_EMAIL, and JIRA_API_TOKEN environment variables."

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
        return f"Failed to create Jira ticket. Status code: {e.status_code}. Details: {e.text}"
    except Exception as e:
        return f"An unexpected error occurred while creating the Jira ticket: {e}"

def get_jira_ticket(ticket_id: str) -> str:
    """
    Retrieves information about a Jira ticket.

    Args:
        ticket_id: The ID of the ticket to retrieve (e.g., PROJ-1234).

    Returns:
        Details about the ticket, or an error message if retrieval failed.
    """
    jira = _get_jira_client()
    if not jira:
        return "Error: Jira client not configured. Set JIRA_SERVER, JIRA_EMAIL, and JIRA_API_TOKEN environment variables."

    try:
        issue = jira.issue(ticket_id)
        status = issue.fields.status.name
        assignee = issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned"
        summary = issue.fields.summary
        return f"Ticket {ticket_id}: '{summary}' - Status: {status}. Assigned to: {assignee}."
    except JIRAError as e:
        return f"Failed to retrieve Jira ticket. Status code: {e.status_code}. Details: {e.text}"
    except Exception as e:
        return f"An unexpected error occurred while retrieving the Jira ticket: {e}"

def record_standup_update(user: str, update: str) -> str:
    """
    Records a user's update from the daily standup.

    Args:
        user: The name of the team member.
        update: Their update for the day.

    Returns:
        A confirmation message that the update was recorded.
    """
    # Simple file-based storage for standup notes
    notes_file = "standup_notes.jsonl"
    try:
        with open(notes_file, "a") as f:
            record = {"user": user, "update": update}
            f.write(json.dumps(record) + "\n")
        return f"Successfully recorded standup update for {user}. Saved to {notes_file}."
    except Exception as e:
        return f"Error recording standup update for {user}: {e}"

# Define the Scrum Master Agent
agent = Agent(
    name="ScrumMasterAgent",
    instruction=(
        "You are an experienced Agile Scrum Master. "
        "Your responsibilities include running daily standups, helping the team "
        "unblock issues, and managing Jira tickets. "
        "When team members provide their updates, make sure to record them using the record_standup_update tool. "
        "If a team member mentions a new task or a bug, offer to create a Jira ticket for them using the create_jira_ticket tool, "
        "or create it directly if they provide enough details (including the project key). "
        "You can also look up existing tickets using the get_jira_ticket tool. "
        "Always be helpful, concise, and focused on helping the team deliver value."
    ),
    tools=[create_jira_ticket, get_jira_ticket, record_standup_update],
)
