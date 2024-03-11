#!/usr/bin/python3

"""
A script 14-model_city_fetch_by_state.py that prints all
City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    args = sys.argv
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(args[1], args[2], args[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    result = session.query(State.name, City.id, City.name)
    filtered_result = result.filter(State.id == City.state_id)

    for instance in filtered_result:
        print(instance[0] + ': (' + str(instance[1]) + ') ' + instance[2])
