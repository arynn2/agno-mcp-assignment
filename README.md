# Agno MCP + Manager/Employee Assignment

This project completes two tasks using the Agno agent framework.

## Task 1: MCP Server + Database + Agno Agent

A SQLite database stores employee data. An MCP server exposes a tool that reads from this database. An Agno agent connects to the MCP server and uses that tool to answer questions using real data.

**Files:** setup_database.py, mcp_server.py, business_agent.py

**Sample output:**

Tool Calls: query_employees(department=Engineering)

Response: Alice Johnson - Engineering - $95,000, Carol Davis - Engineering - $105,000

## Task 2: Manager + Employee Agent Delegation

A Manager agent and a Finance Employee agent are set up using Agno's Team feature. The Manager delegates finance-related questions to the Finance Employee, and handles non-finance questions itself.

To prove delegation actually happens, the Employee was given a secret fact unknown to the Manager: a fake Q3 marketing budget of $42,317.

**File:** manager_employee.py

**Test 1, finance question, should delegate:**
Result: The Manager delegated to the Finance Employee and the response correctly included $42,317, proving delegation occurred.

**Test 2, marketing question, should NOT delegate:**
Result: No delegation occurred. The Manager answered directly, correctly recognizing the request was outside the Finance Employee's department.

## Setup

pip install agno anthropic python-dotenv mcp

Create a .env file with your own ANTHROPIC_API_KEY

Then run:
python setup_database.py
python business_agent.py
python manager_employee.py
