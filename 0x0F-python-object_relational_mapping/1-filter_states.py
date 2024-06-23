#!/usr/bin/python3
"""Script to execute conditional SELECT query on a table of a given database.
"""


import MySQLdb as mysql
import sys


def db_management(args):
    """List states names starting with the character 'N'.
        Here this condition is imposed via SQL.
    """
    db = mysql.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE SUBSTRING(name, 1, 1)='N'\
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    db_management(sys.argv)
