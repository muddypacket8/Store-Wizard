from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    number = Column(Integer)

    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number

    def __repr__(self):
        return f"<Customer(name='{self.name}', email='{self.email}', number='{self.number}')>"

engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

customer = Customer("leon mwangi", "leonmwas@gmail.com", 794199883)
session.add(customer)
session.commit()
