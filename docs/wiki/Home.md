# Istaris - AI Digital Employees Development Plan

This document outlines the phased approach to building out the AI agents for Istaris using Google's AI ecosystem (Google ADK, Vertex AI, Gemini 3.1).

## Phase 1: Foundation and Initial Prototype (Weeks 1-3)

### Goal: Establish the architecture, set up the shared infrastructure, and build the first functional agent (Scrum Master).

1.  **Environment Setup & Verification:**
    *   Initialize Google Cloud Project.
    *   Enable required APIs: Vertex AI, Cloud Storage.
    *   Set up Service Accounts and authentication for local development and CI/CD.
    *   Configure Python environment with `google-adk`, `google-cloud-aiplatform`, and testing frameworks (`pytest`).
    *   Ensure the Next.js frontend can communicate with a basic Python API endpoint (if applicable, e.g., via FastAPI).

2.  **Develop Shared Tooling (`src/agents/shared/`):**
    *   **Core Utility:** Create base classes/interfaces for tools if the ADK requires them.
    *   **Authentication/API Clients:** Implement robust wrappers for calling external APIs (e.g., Jira, Slack) with proper error handling and rate limiting.
    *   **Memory/Context Management:** Set up a basic mechanism (e.g., Vector Search or simply passing recent context in the prompt) for agents to remember past interactions.

3.  **Build the Scrum Master Agent (`src/agents/scrum_master/`):**
    *   **System Prompt:** Define the persona, goals, and constraints of the Scrum Master.
    *   **Tool Integration:** Integrate the Jira tool (using the existing `jira` package mentioned in requirements) to read sprint boards, identify stale tickets, and update statuses.
    *   **Testing:** Write unit tests for individual tools and integration tests for the agent's interaction loop. Simulate a sprint review and ensure the agent correctly identifies blockers.

4.  **Demonstrate End-to-End Workflow:**
    *   Trigger the Scrum Master agent (e.g., via a simple script or a basic UI button).
    *   Verify it can analyze a dummy Jira board and generate a summary report or update tickets correctly using Gemini 3.1.

## Phase 2: Expanding Capabilities and Multi-Agent Introduction (Weeks 4-6)

### Goal: Add the Digital Marketing Specialist agent and establish patterns for rapidly creating new roles.

1.  **Build the Digital Marketing Specialist Agent (`src/agents/marketing_specialist/`):**
    *   **System Prompt:** Define the persona focusing on content creation, campaign analysis, and social media management.
    *   **Tool Development:**
        *   Create tools for interacting with simulated (or sandbox) Analytics/Ads APIs.
        *   Create tools for generating and scheduling content (e.g., a "SocialMediaTool").
    *   **Model Selection:** Utilize Gemini 3.1 Pro for high-level strategy and Gemini 3.1 Flash for rapid generation of ad copy variations.

2.  **Refine Shared Infrastructure:**
    *   Identify common patterns between the Scrum Master and Marketing Specialist and move them into the `shared/` directory.
    *   Improve error handling and fallback mechanisms (e.g., what happens if an API is down or the model hallucinates a tool call).
    *   Implement robust logging (to Cloud Logging or similar) for auditing agent actions.

3.  **Implement Human-in-the-Loop (HITL) (Optional but Recommended):**
    *   Design a mechanism where agents can propose actions (e.g., "I suggest moving these 5 tickets to 'Blocked'") that require human approval before execution. This is crucial for safety and trust.

## Phase 3: Scaling, Integration, and Production Readiness (Weeks 7+)

### Goal: Make the system generic, robust, and ready for production deployment.

1.  **Generic Agent Framework:**
    *   Abstract the agent creation process. Create a factory or configuration-driven approach where defining a new agent is as simple as providing a YAML config with its name, prompt, and a list of authorized tools.
    *   Example: `AgentFactory.create(config_path="scrum_master.yaml")`.

2.  **Frontend Integration (Next.js):**
    *   Build robust API endpoints (e.g., using FastAPI or Cloud Run) to expose agent capabilities to the Next.js frontend.
    *   Develop the UI for users to view agent logs, approve/reject actions (HITL), and configure agent settings.

3.  **Advanced Features (Exploration):**
    *   **Long-Term Memory:** Implement persistent storage (e.g., Vertex AI Vector Search) so agents can recall information from months ago (e.g., "What did we do last time this bug occurred?").
    *   **Multi-Agent Collaboration:** Explore allowing agents to communicate directly (e.g., the Scrum Master asks the Marketing Specialist for the status of a release announcement).

4.  **Production Deployment:**
    *   Containerize the Python backend (Docker).
    *   Deploy to a scalable environment like Google Cloud Run or GKE.
    *   Set up monitoring, alerting, and CI/CD pipelines (e.g., GitHub Actions to deploy to Cloud Run on merge to `main`).
    *   Ensure compliance and security best practices (least privilege for Service Accounts, secure secret management using Google Secret Manager).
