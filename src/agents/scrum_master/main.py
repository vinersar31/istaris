import os
import sys

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from .agent import agent

# We must ensure there's an API key set, otherwise it will fail to start the agent.
# This assumes the user will export GOOGLE_API_KEY when running locally
def main():
    if not os.environ.get("GOOGLE_API_KEY") and not os.environ.get("GOOGLE_GENAI_API_KEY"):
        print("WARNING: GOOGLE_API_KEY or GOOGLE_GENAI_API_KEY environment variable is not set.", file=sys.stderr)
        print("The agent will likely fail when generating responses.", file=sys.stderr)

    session_service = InMemorySessionService()
    runner = Runner(app_name="ScrumMasterApp", agent=agent, session_service=session_service)

    user_id = "user_cli"
    session_id = "session_cli"

    print("\n" + "="*50)
    print(f"[{agent.name}] started. Type 'exit' or 'quit' to exit.")
    print("="*50 + "\n")

    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            break

        if user_input.strip().lower() in ["exit", "quit"]:
            break

        if not user_input.strip():
            continue

        print("Agent:", end=" ")

        try:
            # We iterate over the yielded events from runner.run()
            # These can include message chunks, tool calls, and completions
            # Using synchronous runner for simplicity in the CLI
            for event in runner.run(
                user_id=user_id,
                session_id=session_id,
                new_message=user_input,
            ):
                if hasattr(event, "message_content") and event.message_content:
                    print(event.message_content, end="", flush=True)
                elif hasattr(event, "tool_call") and event.tool_call:
                    print(f"\n[Tool Execution: {event.tool_call.name}]", end=" ")
                elif hasattr(event, "tool_return") and event.tool_return:
                    # To show that tool execution finished
                    print(f" -> {event.tool_return.result}", end=" ")
                    print("\nAgent:", end=" ")
        except Exception as e:
            print(f"\n[Error: {e}]", end="")

        print()

if __name__ == "__main__":
    main()
