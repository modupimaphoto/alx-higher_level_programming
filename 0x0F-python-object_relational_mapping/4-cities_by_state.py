#!/usr/bin/python3

"""A script that lists all cities from the database hbtn_0e_4_usa"""

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

    sql = """SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON states.id=cities.state_id"""
    c.execute(sql)

    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
