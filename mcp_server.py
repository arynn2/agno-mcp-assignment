import sqlite3
from mcp.server.fastmcp import FastMCP

# Create the MCP server, give it a name
mcp = FastMCP("business-database")

@mcp.tool()
def query_employees(department: str = None) -> str:
    """
    Get employee data from the database.
    If a department is provided, only return employees in that department.
    Otherwise, return all employees.
    """
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    if department:
        cursor.execute(
            "SELECT name, department, salary FROM employees WHERE department = ?",
            (department,)
        )
    else:
        cursor.execute("SELECT name, department, salary FROM employees")

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No employees found."

    result = "\n".join(f"{name} - {dept} - ${salary}" for name, dept, salary in rows)
    return result

if __name__ == "__main__":
    mcp.run()