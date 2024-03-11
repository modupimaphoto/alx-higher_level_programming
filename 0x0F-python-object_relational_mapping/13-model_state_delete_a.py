#!/usr/bin/python3

"""
A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    args = sys.argv
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(args[1], args[2], args[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    result = session.query(State).filter(State.name.like('%a%'))

    for instance in result:
        session.delete(instance)

    session.commit()
