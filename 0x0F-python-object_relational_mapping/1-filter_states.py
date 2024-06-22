#!/usr/bin/python3
"""state selector"""
import sys
import MYSQLdb

if __name__ == "__main__":
	db = MYSQLdb.connect(
	host="localhost",
	port=3306,
	user=sys.argv[1],
	passwd=sys.argv[2],
	db=sys.argv[3]
	)

	cur = db.cursor()
	cur.excute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
	rows = cur.fetchall()
	for row in rows:
		print(row)
	cur.close()
	db.close()
