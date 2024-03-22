#!/usr/bin/python3
"""
Uses sql alchemy to create a table in a database
to work with the ORM
"""


from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ States class
    Attributes:
        __tablename__ (str): The name of the table
        id (int): The state id of the class
        name (string): The state name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
