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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id ORDER BY \
                cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    db_management(sys.argv)
