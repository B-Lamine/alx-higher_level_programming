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
    cur.execute("SELECT name FROM cities WHERE state_id=(SELECT id FROM \
                states WHERE name=%s) ORDER BY id ASC", (args[4],))
    rows = cur.fetchall()
    switch = 0
    for row in rows:
        if switch == 1:
            print(', ', end='')
        print(row[0], end='')
        switch = 1
    print('')


if __name__ == '__main__':
    db_management(sys.argv)
