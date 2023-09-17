#!/usr/bin/python3
"""this programs runs a query on a database.
"""


import MySQLdb as mysql
import sys


def db_management(args):
    """select record based on user input
    """
    db = mysql.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(args[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    db_management(sys.argv)
