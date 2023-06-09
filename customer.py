ffrom sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
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

# Function to display product report
def display_product_report():
    print("PRODUCTS:")
    for product in product_data:
        print(f"Product ID: {product['product_id']}")
        print(f"Product Name: {product['product']}")
        print(f"Price: {product['price']}")
        print("---")

# Function to display sale report
def display_sale_report():
    print("SALES:")
    for sale in sale_data:
        print(f"Sale ID: {sale['id']}")
        print(f"Product ID: {sale['product_id']}")
        print(f"Quantity: {sale['quantity']}")
        print("---")

# Fetch all products
products = session.query(Product).all()

# Fetch all sales
sales = session.query(Sale).all()

# Convert fetched data to dictionaries for easier access
product_data = [product.__dict__ for product in products]
sale_data = [sale.__dict__ for sale in sales]

# Prompt user for report type
report_type = input("Enter 'product' for product report or 'sale' for sale report: ")

# Display the corresponding report
if report_type == 'product':
    display_product_report()
elif report_type == 'sale':
    display_sale_report()
else:
    print("Invalid report type.")
