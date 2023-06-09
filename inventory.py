from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product = Column(String(100))
    price = Column(Integer)

    def __init__(self, product_id, product, price):
        self.product_id = product_id
        self.product = product
        self.price = price

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, product='{self.product}', price={self.price})>"

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer)

    product = relationship("Product", backref="sales")

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"<Sale(id={self.id}, product_id={self.product_id}, quantity={self.quantity})>"


# Create the engine and session
engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Function to prompt user for product details
def enter_product():
    product_id = int(input("Enter product ID: "))
    product_name = input("Enter product name: ")
    price = int(input("Enter product price: "))

    product = Product(product_id, product_name, price)
    session.add(product)
    session.commit()
    print("Product added successfully.")

# Function to prompt user for sale details
def enter_sale():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter sale quantity: "))

    sale = Sale(product_id, quantity)
    session.add(sale)
    session.commit()
    print("Sale added successfully.")

# Prompt user for action
action = input("Enter 'product' to enter a new product or 'sale' to enter a new sale: ")

if action == 'product':
    enter_product()
elif action == 'sale':
    enter_sale()
else:
    print("Invalid action. Please try again.")

