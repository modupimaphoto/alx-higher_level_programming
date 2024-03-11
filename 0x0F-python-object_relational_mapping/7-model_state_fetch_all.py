#!/usr/bin/python3


"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    args = sys.argv

    if len(args) < 4:
        exit(1)

    conn_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_string.format(args[1], args[2], args[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
    session = Session()
    result = session.query(State).order_by(State.id).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))

    session.close()
