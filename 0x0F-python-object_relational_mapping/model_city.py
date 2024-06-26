#!/usr/bin/python3
"""
python file that contains the class definition of
a City and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    A SQLAlchemy model class for the cities table.
    """

    # Set the table name for the class
    __tablename__ = "cities"

    # Define the table columns and their properties
    id = Column(Integer(), primary_key=True, nullable=False,
                unique=True, autoincrement=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer(), ForeignKey("states.id"),
                      nullable=False)
