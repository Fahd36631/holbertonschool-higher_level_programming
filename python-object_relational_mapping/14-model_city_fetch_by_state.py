#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db_name),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join cities with states, order by City.id
    results = (session.query(State, City)
               .filter(State.id == City.state_id)
               .order_by(City.id.asc())
               .all())

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
