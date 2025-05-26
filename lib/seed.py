#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie



# Setup database
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Clear any existing data (optional during development)
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create companies
c1 = Company(name="OpenAI", founding_year=2015)
c2 = Company(name="Google", founding_year=1998)
c3 = Company(name="Apple", founding_year=1976)

# Create developers
d1 = Dev(name="Alice")
d2 = Dev(name="Bob")
d3 = Dev(name="Charlie")

# Create freebies
f1 = Freebie(item_name="T-shirt", value=20, company=c1, dev=d1)
f2 = Freebie(item_name="Sticker", value=5, company=c2, dev=d2)
f3 = Freebie(item_name="Water Bottle", value=15, company=c1, dev=d3)
f4 = Freebie(item_name="Notebook", value=10, company=c3, dev=d1)

# Add and commit
session.add_all([c1, c2, c3, d1, d2, d3, f1, f2, f3, f4])
session.commit()

print("🌱 Seeded database successfully!")
