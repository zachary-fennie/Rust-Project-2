"""
Complete Python Command Line Tool
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="sample_data.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    print("Transforming and loading data...")
    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, encoding="utf-8", newline=""), delimiter=",")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INTEGER
        )"""
    )
    # insert data into database
    cursor.executemany(
        "INSERT INTO users (id, name, email, age) VALUES (?, ?, ?, ?)", payload
    )
    conn.commit()
    conn.close()
    return "users.db"


def create():
    """Create function for CRUD"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # create execution
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        )"""
    )
    conn.commit()
    conn.close()
    return "Create Success"


def read():
    """Read function for CRUD"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # read execution
    print("Top 5 rows of the table:")
    cursor.execute("SELECT * FROM users LIMIT 5;")
    # Fetch the results
    rows = cursor.fetchall()  # Fetch results here
    print(rows)  # Print the fetched rows to see the output
    conn.close()
    return "Read Success"


def query():
    """Query the database for the test case"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    print("Querying data...")
    cursor.execute("SELECT * FROM users WHERE name = 'Zachar Carter';")
    print(cursor.fetchall())
    conn.close()
    return "Query Success"


def update():
    """Update function for CRUD"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # update execution
    cursor.execute(
        "UPDATE users SET name = 'Zachary Carter' WHERE name = 'Zachar Carter'"
    )
    conn.commit()
    conn.close()
    return "Update Success"


def delete():
    """Delete function for CRUD"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # delete execution
    cursor.execute("DELETE FROM users WHERE name = 'Zachary Carter'")
    conn.close()
    return "Delete Success"


def full_crudquery():
    """Run all functions of crud_query.py"""
    full1 = create()
    full2 = read()
    full3 = query()
    full4 = update()
    full5 = delete()

    return {
        "full_crudquery": [
            full1,
            full2,
            full3,
            full4,
            full5,
        ]
    }
