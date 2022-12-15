#!/usr/bin/python3
"""print first state object"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        user,
                        password,
                        name),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    ssn = sessionmaker(bind=eng)
    session = ssn()
    if session.query(State).order_by(State.id).first():
        print(f"{State.id}: {State.name}")
    else:
        print('Nothing')
