from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Customer(customer_id={self.customer_id}, name='{self.name}', email='{self.email}')>"

# Create the engine and session
engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Function to prompt user for customer details
def enter_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")

    customer = Customer(name, email)
    session.add(customer)
    session.commit()
    print("Customer added successfully.")

# Prompt user to enter customer information
enter_customer()
