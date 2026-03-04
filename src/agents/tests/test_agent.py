import pytest
import os
import json
from unittest.mock import MagicMock

from src.agents.scrum_master.agent import (
    agent,
    create_jira_ticket,
    get_jira_ticket,
    record_standup_update
)

def test_agent_initialization():
    """Test that the agent is properly configured."""
    assert agent.name == "ScrumMasterAgent"
    assert len(agent.tools) == 6

    # Assert tools are present in the list
    tool_names = [tool.__name__ for tool in agent.tools]
    assert "create_jira_ticket" in tool_names
    assert "get_jira_ticket" in tool_names
    assert "record_standup_update" in tool_names

@pytest.fixture
def mock_jira_env(monkeypatch):
    """Sets up fake environment variables for Jira client initialization."""
    monkeypatch.setenv("JIRA_SERVER", "https://test.jira.com")
    monkeypatch.setenv("JIRA_EMAIL", "test@example.com")
    monkeypatch.setenv("JIRA_API_TOKEN", "fake_token")

@pytest.fixture
def mock_jira_client(mocker):
    """Mocks the JIRA class to prevent actual network calls."""
    mock_jira = MagicMock()
    # When JIRA() is called, return our mock object
    mocker.patch("src.agents.scrum_master.agent.JIRA", return_value=mock_jira)
    return mock_jira

def test_create_jira_ticket_no_env_vars(monkeypatch):
    """Test creating a ticket when environment variables are not set."""
    monkeypatch.delenv("JIRA_SERVER", raising=False)

    result = create_jira_ticket("Test Title", "Test Desc", "PROJ")
    assert "Error: Jira client not configured" in result

def test_create_jira_ticket_success(mock_jira_env, mock_jira_client):
    """Test creating a ticket successfully."""
    # Configure the mock to return a fake issue object when create_issue is called
    mock_issue = MagicMock()
    mock_issue.key = "PROJ-1234"
    mock_jira_client.create_issue.return_value = mock_issue

    result = create_jira_ticket("Fix login bug", "Users cannot login", "PROJ", "Bug")

    assert "Created ticket PROJ-1234" in result
    assert "Fix login bug" in result

    # Verify the JIRA client was called correctly
    mock_jira_client.create_issue.assert_called_once_with(fields={
        'project': {'key': 'PROJ'},
        'summary': 'Fix login bug',
        'description': 'Users cannot login',
        'issuetype': {'name': 'Bug'}
    })

def test_get_jira_ticket_success(mock_jira_env, mock_jira_client):
    """Test retrieving a ticket successfully."""
    # Configure the mock to return a fake issue object when issue() is called
    mock_issue = MagicMock()
    mock_issue.fields.summary = "Fix login bug"
    mock_issue.fields.status.name = "In Progress"
    mock_issue.fields.assignee.displayName = "Alice Developer"
    mock_jira_client.issue.return_value = mock_issue

    result = get_jira_ticket("PROJ-1234")

    assert "Ticket PROJ-1234" in result
    assert "In Progress" in result
    assert "Alice Developer" in result

    # Verify JIRA client was called correctly
    mock_jira_client.issue.assert_called_once_with("PROJ-1234")

def test_record_standup_update(tmp_path, monkeypatch):
    """Test the record_standup_update tool."""
    # Patch the file location so we don't write to the real project directory
    test_file = tmp_path / "standup_notes.jsonl"

    monkeypatch.chdir(tmp_path)

    user = "Bob"
    update = "Completed sprint planning."
    result = record_standup_update(user, update)

    assert "Successfully recorded standup update for Bob" in result
    assert "standup_notes.jsonl" in result

    # Verify file contents
    assert os.path.exists("standup_notes.jsonl")
    with open("standup_notes.jsonl", "r") as f:
        lines = f.readlines()
        assert len(lines) == 1
        record = json.loads(lines[0])
        assert record["user"] == "Bob"
        assert record["update"] == "Completed sprint planning."

from src.agents.scrum_master.agent import (
    get_agile_boards,
    get_sprints,
    get_sprint_metrics
)

def test_get_agile_boards(mock_jira_env, mock_jira_client):
    mock_board = MagicMock()
    mock_board.id = 123
    mock_board.name = "Test Board"
    mock_jira_client.boards.return_value = [mock_board]

    result = get_agile_boards("Test")
    assert "Board ID: 123" in result
    assert "Test Board" in result

def test_get_sprints(mock_jira_env, mock_jira_client):
    mock_sprint = MagicMock()
    mock_sprint.id = 456
    mock_sprint.name = "Sprint 1"
    mock_sprint.state = "active"
    mock_jira_client.sprints.return_value = [mock_sprint]

    result = get_sprints(123)
    assert "Sprint ID: 456" in result
    assert "Sprint 1" in result
    assert "active" in result

def test_get_sprint_metrics(mock_jira_env, mock_jira_client):
    # Mock two issues, one done and one in progress
    issue1 = MagicMock()
    issue1.fields.status.statusCategory.name = "Done"
    issue2 = MagicMock()
    issue2.fields.status.statusCategory.name = "In Progress"

    mock_jira_client.search_issues.return_value = [issue1, issue2]

    result = get_sprint_metrics(123, 456)

    assert "Total Issues: 2" in result
    assert "Done: 1" in result
    assert "In Progress: 1" in result
    assert "50.0%" in result
    assert "chart=sprintRetrospective&sprint=456" in result
