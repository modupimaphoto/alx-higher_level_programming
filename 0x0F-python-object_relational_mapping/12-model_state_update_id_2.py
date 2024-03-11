#!/usr/bin/python3

"""
A script that changes the name of a State object
from the database hbtn_0e_6_usa
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

    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'

    session.commit()
