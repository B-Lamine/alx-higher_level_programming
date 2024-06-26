#!/usr/bin/python3
"""Script to query a specific state given state name in the State
table of the given database.
"""


import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).filter(State.name == sys.argv[4]).first()
    if (row is None):
        print('Not found')
    else:
        print(row.id)
