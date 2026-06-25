from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.anthropic import Claude

agent = Agent(
    model=Claude(id="claude-sonnet-4-5"),
    markdown=True,
)

agent.print_response("What is 2+2, and explain why in one sentence.")