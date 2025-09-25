"""
Day 31: Working with Databases in Python

This script demonstrates the two main ways to interact with a
SQLite database from Python: using the built-in `sqlite3` module
and using the powerful `pandas.read_sql_query` function.
"""

import sqlite3
import pandas as pd
import os

DB_FILE = "company_data.db"

# --- 1. Create and Populate a SQLite Database ---
print(f"--- 1. Creating and populating the database: {DB_FILE} ---")
# The 'with' statement ensures the connection is closed automatically.
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()

    # Drop the table if it already exists to make the script re-runnable
    cursor.execute("DROP TABLE IF EXISTS employees")

    # Create a table
    cursor.execute(
        """
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL NOT NULL
    )
    """
    )

    # Insert some data
    employees_to_add = [
        (101, "Alice", "Sales", 80000),
        (102, "Bob", "Engineering", 120000),
        (103, "Charlie", "Sales", 85000),
        (104, "Diana", "HR", 70000),
        (105, "Eve", "Engineering", 130000),
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees_to_add)

    # Commit the changes to the database
    conn.commit()
print("Database and table created successfully.")
print("-" * 20)


# --- 2. Querying with the `sqlite3` module ---
print("--- 2. Querying for 'Sales' employees with sqlite3 ---")
try:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        # Execute a query to select specific data
        cursor.execute("SELECT name, salary FROM employees WHERE department = 'Sales'")

        # Fetch all results from the executed query
        sales_employees = cursor.fetchall()

        print("Results from sqlite3:")
        for employee in sales_employees:
            print(f"  - Name: {employee[0]}, Salary: ${employee[1]:,.2f}")

except sqlite3.Error as e:
    print(f"Database error: {e}")
print("-" * 20)


# --- 3. The Pandas Way: `read_sql_query` ---
print("--- 3. Querying all 'Engineering' employees with Pandas ---")
try:
    with sqlite3.connect(DB_FILE) as conn:
        # The SQL query to execute
        sql_query = "SELECT * FROM employees WHERE department = 'Engineering'"

        # This one function does all the work: connects, queries, and returns a DataFrame
        engineering_df = pd.read_sql_query(sql_query, conn)

        print("DataFrame returned by pd.read_sql_query():")
        print(engineering_df)

        # Now you can use all your Pandas skills on this DataFrame
        avg_eng_salary = engineering_df["salary"].mean()
        print(f"\nAverage Engineering Salary: ${avg_eng_salary:,.2f}")

except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Clean up the created database file
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"\nCleaned up and removed {DB_FILE}.")
print("-" * 20)
