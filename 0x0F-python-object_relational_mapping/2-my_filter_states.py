#!/usr/bin/python3
"""Script to search for states by name"""

import sys
import MySQLdb

def search_states(username, password, db_name, state_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./search_states.py username password db_name state_name")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    
    search_states(username, password, db_name, state_name)
