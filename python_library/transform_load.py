"""
TRANSFORM AND LOAD
Transforms and Loads data into the local SQLite3 database
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="covid-geography/mmsa-icu-beds.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    print("Transforming and loading data...")
    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, encoding="utf-8", newline=""), delimiter=",")
    conn = sqlite3.connect("icu.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS icuDB")
    c.execute(
        "CREATE TABLE icuDB (MMSA, total_percent_at_risk, high_risk_per_ICU_bed, high_risk_per_hospital, icu_beds, hospitals, total_at_risk)"
    )
    # insert data into database
    c.executemany("INSERT INTO icuDB VALUES (?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "icuDB.db"
