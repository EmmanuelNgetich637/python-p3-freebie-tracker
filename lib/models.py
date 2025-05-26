from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __repr__(self):
        return f'<Company {self.name}>'
    
    def give_freebie(self, dev, item_name, value):
        from sqlalchemy.orm import object_session
        session = object_session(self)
        freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        session.add(freebie)
        session.commit()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, dev, freebie):
        from sqlalchemy.orm import object_session
        if freebie in self.freebies:
            freebie.dev = dev
            session = object_session(freebie)
            session.commit()

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    company = relationship('Company', backref=backref('freebies', lazy=True))
    dev = relationship('Dev', backref=backref('freebies', lazy=True))

    def __repr__(self):
        return f'<Freebie {self.item_name} from {self.company.name} to {self.dev.name}>'
    
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
