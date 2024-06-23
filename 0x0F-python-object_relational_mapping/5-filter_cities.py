#!/usr/bin/python3
"""This program runs a query on a database.
"""


import MySQLdb as mysql
import sys


def db_management(args):
    """Select records from two tables.
    """
    db = mysql.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    rows = cur.fetchall()
    switch = 0
    rows = [row for row in rows if row[2] == args[4]]
    for row in rows:
        if switch == 1:
            print(', ', end='')
        print(row[1], end='')
        switch = 1
    print('')


if __name__ == "__main__":
    db_management(sys.argv)
