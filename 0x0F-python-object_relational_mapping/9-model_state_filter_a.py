#!/usr/bin/python3
"""
9-model_state_filter_a.py
    - List all State objects from the database hbtn_0e_6_usa.

Usage: ./9-model_state_filter_a.py <db_username> <db_password> <db_name>

Connects to a MySQL database
    using the given credentials
    and retrieves all State objects from the 'states' table in the database
    that contains the letter 'a'.

The retrieved objects are printed
    to the console in ascending order of their 'id' attribute.
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database using the provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create a session object using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects from the 'states' table
    # that contains the letter 'a'
    # and print them to the console
    for states in session.query(State)\
            .filter(State.name.ilike("%a%")).order_by(State.id).all():
        print("{}: {}".format(states.id, states.name))
