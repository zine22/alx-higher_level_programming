#!/usr/bin/python3

"""
This script adds a new State object named "Louisiana"
to the database hbtn_0e_6_usa.

After adding the new record,
it prints the ID of the new record to the console.
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

    # Create a new instance of State and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)

    # commit the session to save the new instance to the database
    session.commit()

    # Print the id of the new record
    print(new_state.id)
