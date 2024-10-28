"""
QUERY
Query the database
"""

import sqlite3


def create():
    """Create function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # create execution
    cursor.execute(
        "INSERT INTO icuDB (MMSA, total_percent_at_risk, high_risk_per_ICU_bed, high_risk_per_hospital, icu_beds, hospitals, total_at_risk) VALUES('Duham, NC','50%',1947,43787,360,14,667189)"
    )
    conn.commit()
    conn.close()
    return "Create Success"


def read():
    """Read function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # read execution
    print("Top 5 rows of the table:")
    cursor.execute("SELECT * FROM icuDB LIMIT 5;")
    # Fetch the results
    rows = cursor.fetchall()  # Fetch results here
    print(rows)  # Print the fetched rows to see the output
    conn.close()
    return "Read Success"


def query():
    """Query the database for the test case"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    print("Querying data...")
    cursor.execute("SELECT * FROM icuDB WHERE MMSA = 'Duham, NC';")
    print(cursor.fetchall())
    conn.close()
    return "Query Success"


def update():
    """Update function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # update execution
    cursor.execute("UPDATE icuDB SET MMSA = 'Durham, NC' WHERE MMSA = 'Duham, NC'")
    conn.commit()
    conn.close()
    return "Update Success"


def delete():
    """Delete function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # delete execution
    cursor.execute("DELETE FROM icuDB WHERE MMSA = 'Durham, NC'")
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
