#!/usr/bin/python3

"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
    sql = """SELECT cities.name FROM cities
    INNER JOIN states ON states.id=cities.state_id
    WHERE states.name=%s"""
    c.execute(sql, (sys.argv[4], ))

    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=', ')

    c.close()
    db.close()
