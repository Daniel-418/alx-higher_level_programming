#!/usr/bin/python3
"""
Selects all the states from a database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    """
    queries the states database
    and displays the result
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    update_state = session.query(State).filter(State.id == 2).first()

    update_state.name = 'New Mexico'

    session.commit()
    session.close()
