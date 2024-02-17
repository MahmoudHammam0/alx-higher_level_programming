#!/usr/bin/python3
'''Delete states via SQLAlchemy module'''
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
    for state in session.query(State).filter(State.name.ilike('%a%')):
        session.delete(state)
    session.commit()
    session.close()
