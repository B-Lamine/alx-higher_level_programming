#!/usr/bin/python3
"""this programs runs a query on a database.
"""


import MySQLdb as mysql
import sys


def db_management(args):
    """display the table  states from given database.
    """
    db = mysql.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    db_management(sys.argv)
