#!/usr/bin/python3

"""
A script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument,
that is safe from MySQL injections!
"""

import sys
import MySQLdb


if __name__ == '__main__':

    host = 'localhost'
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(host, user, password, db, port)
    c = db.cursor()
    name = sys.argv[4]
    sql = "SELECT * FROM states WHERE name LIKE %s"
    c.execute(sql, (name, ))

    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
