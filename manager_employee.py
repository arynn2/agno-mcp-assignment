from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.team import Team
from agno.models.anthropic import Claude

employee_agent = Agent(
    name="Finance Employee",
    role="A finance specialist.",
    instructions=(
        "You are the finance department's employee. You only handle finance-related "
        "questions (budgets, expenses, revenue, accounting). "
        "IMPORTANT SECRET FACT only you know: the company's current marketing "
        "budget for Q3 is exactly $42,317. If anyone asks about budgets or finance "
        "figures, you must include this exact number in your answer."
    ),
    model=Claude(id="claude-sonnet-4-5"),
)

manager_team = Team(
    name="Manager",
    members=[employee_agent],
    model=Claude(id="claude-sonnet-4-5"),
    instructions=(
        "You are the Manager. You do NOT have access to internal finance figures "
        "yourself. The Finance Employee handles all finance-related topics: "
        "budgets, expenses, revenue, accounting. "
        "If the user's request is finance-related, you MUST delegate it to the "
        "Finance Employee to get the answer. "
        "If the request is NOT finance-related (e.g. marketing slogans, HR, "
        "general questions), do NOT delegate — handle it yourself instead. "
        "Always return one final, clear answer to the user."
    ),
)

print("\n--- TEST 1: Question IS in the Finance department -> SHOULD delegate ---\n")
manager_team.print_response(
    "What is our current marketing budget for Q3?",
    stream=True,
)

print("\n--- TEST 2: Question is in the Marketing department, NOT Finance -> should NOT delegate ---\n")
manager_team.print_response(
    "What's a good slogan for a new coffee shop?",
    stream=True,
)
