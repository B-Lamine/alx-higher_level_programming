#!/usr/bin/python3
"""Script to query all state names with the letter 'a' in them in
the State table of the given database.
"""


import sys
import sqlalchemy
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).filter(State.name.like('%a%'))\
            .order_by(asc(State.id)):
        print(str(row.id) + ': ' + row.name)
