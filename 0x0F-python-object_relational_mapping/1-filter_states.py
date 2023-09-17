#!/usr/bin/python3
"""script to query database.
"""


import MySQLdb as mysql
import sys


def db_management(args):
    """list state names starting with the character 'N'
    """
    db = mysql.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith('N'):
            print(row)


if __name__ == '__main__':
    db_management(sys.argv)
