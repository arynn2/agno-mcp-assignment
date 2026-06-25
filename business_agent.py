import asyncio
from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.mcp import MCPTools


async def main():
    async with MCPTools(command="python mcp_server.py") as mcp_tools:
        agent = Agent(
            model=Claude(id="claude-sonnet-4-5"),
            tools=[mcp_tools],
            markdown=True,
        )

        await agent.aprint_response(
            "Who works in the Engineering department, and what are their salaries?",
            stream=True,
        )


if __name__ == "__main__":
    asyncio.run(main())