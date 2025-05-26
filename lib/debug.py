#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev

# Setup DB and session
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

alice = session.query(Dev).filter_by(name="Alice").first()
openai = session.query(Company).filter_by(name="OpenAI").first()

print(alice.freebies[0].print_details())


openai.give_freebie(alice, "USB Drive", 30)

print(alice.received_one("USB Drive"))  # Expected: True

bob = session.query(Dev).filter_by(name="Bob").first()
freebie_to_give = alice.freebies[0]
alice.give_away(bob, freebie_to_give)