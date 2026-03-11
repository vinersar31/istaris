# Istaris - AI Digital Employees Architecture

This document describes the high-level architecture of Istaris, focusing on the AI Agent ecosystem built with Google AI tools.

## System Overview

Istaris consists of two primary components:
1.  **Frontend (Next.js):** The client-facing web application where users interact with and manage their digital employees.
2.  **Agent Backend (Python):** The intelligence layer powered by Google Cloud's AI ecosystem, responsible for executing complex, multi-step workflows autonomously.

## Core Technologies

*   **Google Agent Development Kit (ADK):** The foundation for building, running, and managing the AI agents. It handles tool calling, state management, and interaction loops.
*   **Google Vertex AI:** The secure, enterprise-grade machine learning platform used to host and orchestrate our models.
*   **Gemini 3.1 Family (via Vertex AI):**
    *   **Gemini 3.1 Pro:** The primary engine for complex reasoning, planning, and executing intricate tasks requiring deep context.
    *   **Gemini 3.1 Flash:** Used for rapid, high-volume tasks, data processing, and simple API interactions where speed and cost-efficiency are critical.
*   **Vertex AI Search / Vector Search:** For providing Long-Term Memory (RAG) capabilities to the agents, allowing them to index and retrieve company knowledge bases, past sprint data, or marketing copy guidelines.
*   **Google Cloud Storage / BigQuery:** Used for persistent storage of logs, user data, and agent analytics.

## Agent Architecture

The agent architecture follows a modular, capability-based design.

### Directory Structure

```
src/agents/
├── requirements.txt         # Core dependencies (google-adk, google-cloud-aiplatform, jira, etc.)
├── shared/                  # Common utilities and tools
│   ├── __init__.py
│   ├── memory.py            # Vector Search / RAG interactions
│   ├── auth.py              # Google Cloud Auth utilities
│   └── tools/               # Shared tools (e.g., Slack, Email, Calendar)
├── scrum_master/            # Specific Agent Implementation
│   ├── __init__.py
│   ├── agent.py             # Defines the ADK Agent (system prompt, tools)
│   └── tools/
│       └── jira_tool.py     # Jira API integration
└── marketing_specialist/    # Specific Agent Implementation
    ├── __init__.py
    ├── agent.py             # Defines the ADK Agent (system prompt, tools)
    └── tools/
        ├── analytics.py     # Google Analytics/Ads integrations
        └── social.py        # Social media API integrations
```

### Agent Design Principles

1.  **Modularity:** Each agent role (e.g., `scrum_master`, `marketing_specialist`) is contained within its own module. This allows for independent development, testing, and deployment.
2.  **Shared Tools:** Capabilities that are common across multiple roles (like sending an email or querying a database) are centralized in the `shared/` directory to maximize code reuse.
3.  **Extensibility:** Adding a new agent role involves creating a new folder, defining its specific system prompt in its `agent.py`, and provisioning it with the necessary tools from `shared/` or its own specific tools.
4.  **Google Ecosystem Integration:** We heavily lean on Google Cloud infrastructure. Authentication is handled via Service Accounts or Workload Identity.

## Agent Workflows (Examples)

### 1. Scrum Master Agent
*   **Triggers:** Scheduled daily standups, webhook from Jira (e.g., sprint start), or manual user request via the Next.js frontend.
*   **Capabilities (Tools):**
    *   `JiraTool`: Reads current sprint status, identifies blockers, updates tickets.
    *   `SlackTool` (Shared): Pings team members for updates.
*   **Model:** Uses Gemini 3.1 Pro to analyze sprint velocity and identify risks.

### 2. Digital Marketing Specialist Agent
*   **Triggers:** Weekly schedule, new product launch event.
*   **Capabilities (Tools):**
    *   `AnalyticsTool`: Reads traffic data and conversion rates.
    *   `CopywritingTool`: Generates ad copy variations.
    *   `SocialMediaTool`: Schedules posts.
*   **Model:** Uses Gemini 3.1 Pro for strategic campaign planning and Gemini 3.1 Flash for rapid ad copy generation.

## Future Considerations

*   **Multi-Agent Orchestration:** Exploring frameworks (potentially within the Google ecosystem or libraries like LangGraph/AutoGen if ADK doesn't support complex hierarchies) to allow agents to collaborate (e.g., the Scrum Master asks the Marketing Specialist for an update on a release campaign).
*   **Human-in-the-Loop (HITL):** Implementing a robust approval mechanism where agents draft actions (like a major Jira reshuffle or a large ad spend) and await human approval via the Next.js frontend before executing.
