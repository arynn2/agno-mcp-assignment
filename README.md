# Agno MCP + Manager/Employee Assignment

This project completes two tasks using the Agno agent framework:

## Task 1: MCP Server + Database + Agno Agent

A SQLite database (`business.db`) stores employee data. An MCP server
(`mcp_server.py`) exposes a `query_employees` tool that reads from this
database. An Agno agent (`business_agent.py`) connects to this MCP server
and uses the tool to answer questions with real data.

**Files:** `setup_database.py`, `mcp_server.py`, `business_agent.py`

**Sample output:**
## Task 2: Manager + Employee Agent Delegation

A Manager agent and a Finance Employee agent are set up using Agno's
`Team` feature. The Manager delegates finance-related questions to the
Finance Employee, and handles non-finance questions itself.

To prove delegation actually happens (not just a plausible-sounding
answer), the Employee was given a secret fact unknown to the Manager:
a fake Q3 marketing budget of $42,317.

**File:** `manager_employee.py`

**Test 1 — Finance question (should delegate):**
This proves delegation occurred — the Manager has no way to produce
that number on its own.

**Test 2 — Marketing question (should NOT delegate):**
No delegation occurred, confirming the Manager correctly recognized
this request was outside the Finance Employee's department.

## Setup (to run this yourself)
Create a `.env` file with:
cat > README.md << 'EOF'
# Agno MCP + Manager/Employee Assignment

This project completes two tasks using the Agno agent framework.

## Task 1: MCP Server + Database + Agno Agent
A database stores employee data. An MCP server reads from it. An Agno agent uses that server to answer questions with real data.

## Task 2: Manager + Employee Delegation
A Manager agent delegates finance questions to a Finance Employee agent, and handles non-finance questions itself. Tested and confirmed working.

## Setup
pip install agno anthropic python-dotenv mcp
Create a .env file with your own ANTHROPIC_API_KEY
Then run: python setup_database.py, python business_agent.py, python manager_employee.py
