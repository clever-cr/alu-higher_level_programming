#!/usr/bin/python3
"""script that prints the first state object from database"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    eng = create_engine