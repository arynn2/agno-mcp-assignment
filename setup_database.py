import sqlite3

# Connect to (or create) a database file called business.db
conn = sqlite3.connect("business.db")
cursor = conn.cursor()

# Create a simple employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
)
""")

# Add some sample data
sample_employees = [
    (1, "Alice Johnson", "Engineering", 95000),
    (2, "Bob Smith", "Sales", 72000),
    (3, "Carol Davis", "Engineering", 105000),
    (4, "David Lee", "Marketing", 68000),
    (5, "Eve Martinez", "Sales", 78000),
]

cursor.executemany(
    "INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
    sample_employees
)

conn.commit()
conn.close()

print("Database created successfully with sample employee data!")