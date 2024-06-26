#!/usr/bin/python3
"""This program executes a SELECT query based on user input in a safe
   way to prevent SQL injections.
"""


import MySQLdb as mysql
import sys


def db_management(args):
    """Select recored safely based on user input.
    """
    db = mysql.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == args[4]:
            print(row)


if __name__ == '__main__':
    db_management(sys.argv)
