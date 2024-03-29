#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa:"""

import sys
import MySQLdb


if __name__ == '__main__':

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(host, user, password, db, port)

    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
