"""
TRANSFORM AND LOAD
Transforms and Loads data into the local SQLite3 database
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
