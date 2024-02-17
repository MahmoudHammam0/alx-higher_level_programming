#!/usr/bin/python3
'''First state via SQLAlchemy module'''
import sqlalchemy
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    if (len(sys.argv[4]) < 10):
        states = session.query(State).filter(State.name == sys.argv[4])
        if (states.count() == 0):
            print("Not found")
        else:
            for state in states:
                print(state.id)
    session.close()
