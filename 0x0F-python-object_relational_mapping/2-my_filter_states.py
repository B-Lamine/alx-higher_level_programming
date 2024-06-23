#!/usr/bin/python3
"""This program executes a SELECT query with a condition based on user input.
"""


import MySQLdb as mysql
import sys


def db_management(args):
    """Select records based on user input.
    """
    db = mysql.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM  states WHERE name='{}' ORDER BY\
                id ASC".format(args[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    db_management(sys.argv)
