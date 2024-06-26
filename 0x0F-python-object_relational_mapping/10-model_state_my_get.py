#!/usr/bin/python3
"""
    Connects to a MySQL database using the given credentials and retrieves the
    ID of the first State object whose name matches the provided name.

usage:
./10-model_state_my_get.py <db_username> <db_password> <db_name> <state_name>
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

    # Query the 'states' table
    #   for the first State object whose name matches the provided name
    state = session.query(State).filter(State.name == argv[4])\
        .order_by(State.id).first()

    # Print the ID of the matching State object,
    #   or "Not found" if no match is found
    if state is None:
        print("Not found")
    else:
        print(state.id)
