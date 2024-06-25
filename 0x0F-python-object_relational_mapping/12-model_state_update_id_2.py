#!/usr/bin/python3
"""Script to update a specific state's name given the state's id in
the State table of the given database.
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
    row = session.query(State).filter(State.id == 2).first()
    row.name = 'New Mexico'
    session.commit()
