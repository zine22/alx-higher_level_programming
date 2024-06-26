#!/usr/bin/python3

"""Deletes all State objects from the database
that contain the letter 'a' in their name.
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

    # Query for all State objects containing 'a' in their name
    state_with_a = session.query(State)\
        .filter(State.name.ilike("%a%")).order_by(State.id).all()

    # Delete each matching State object
    for state in state_with_a:
        session.delete(state)

    # Commit the transaction
    session.commit()
