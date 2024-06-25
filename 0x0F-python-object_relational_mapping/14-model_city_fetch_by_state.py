#!/usr/bin/python3
"""Script to query joined tables in the given database.
"""


import sys
import sqlalchemy
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city_row, state_row in session.query(City, State).join(State).all():
        print('{}: ({}) {}'.format(state_row.name, city_row.id, city_row.name))
