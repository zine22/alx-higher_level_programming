#!/usr/bin/python3
"""
Script that updates the name of a State object from the database hbtn_0e_6_usa.
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

    # Query for the State object where id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name attribute of the State object
    state_to_update.name = "New Mexico"

    # Commit the changes to the database
    session.commit()
