#!/usr/bin/python3
"""This program defines the class State, which is mapped to the table
of the same name via SQLAlchemy ORM.
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                       .format("root", "root", "3306", "hbtn_0e_6_usa"),
                       pool_pre_ping=True)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class State(Base):
    """Maps to the States table of the MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
