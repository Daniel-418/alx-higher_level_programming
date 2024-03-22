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

    result = session.query(State).filter(State.name == sys.argv[4]).first()

    if result:
        print("{}".format(result.id))
    else:
        print("Not found")
