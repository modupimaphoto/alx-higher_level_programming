#!/usr/bin/python3

"""
A script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    args = sys.argv

    if len(args) < 5 or ';' in args[4]:
        exit(1)

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(args[1], args[2], args[3]))
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)
    session = Session()
    result = session.query(State).filter(State.name.like(args[4])).all()

    if len(result) == 0:
        print('Not found')
    else:
        print(result[0].id)

    session.close()
