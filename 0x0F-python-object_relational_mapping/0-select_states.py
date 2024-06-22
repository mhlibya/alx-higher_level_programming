#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
import MYSQLdb

def list_states(username, password, db_name):
	db = MYSQLdb.connect(
	host="localhost",
	port=3306,
	user=username,
	passwd=password,
	db=db_name)

	cur = db.cursor()

	cur.excute("SELECT * FROM states ORDER BY id ASC")

	rows = cur.fetchall()

	for row in rows:
		print(row)

	cur.close()
	db.close()

if __name__ == __main__:
	list_states(sys.srgv[1], sys.argv[2], sys.argv[3])
