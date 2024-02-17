#!/usr/bin/python3
'''Add a new state via SQLAlchemy module'''
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
    Louisiana = State(name='Louisiana')
    session.add(Louisiana)
    for state in session.query(State).filter(State.name == 'Louisiana'):
        print(state.id)
    session.commit()
    session.close()
