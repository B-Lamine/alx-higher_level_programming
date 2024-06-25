#!/usr/bin/python3
"""This program defines the class City, which is mapped to the table
of the same name via SQLAlchemy ORM.
"""


from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Maps to the Cities table of the MySQL database.

    Attributes:
        __tablename__ (str): table name.
        id (int): table's id.
        name (str): state's name.
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')

State.cities = relationship('City', order_by=City.id, back_populates='state')
