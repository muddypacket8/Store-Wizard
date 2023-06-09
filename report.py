from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
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

# Function to generate products report
def generate_products_report():
    products = session.query(Product).all()
    print("PRODUCTS:")
    for product in products:
        print(f"Product ID: {product.product_id}")
        print(f"Product Name: {product.product}")
        print(f"Price: {product.price}")
        print("---")

# Function to generate sales report
def generate_sales_report():
    sales = session.query(Sale).all()
    print("\nSALES:")
    for sale in sales:
        print(f"Sale ID: {sale.id}")
        print(f"Product ID: {sale.product_id}")
        print(f"Quantity: {sale.quantity}")
        print("---")

# Prompt user for report type
report_type = input("Enter 'products' to generate the products report or 'sales' to generate the sales report: ")

if report_type == 'products':
    generate_products_report()
elif report_type == 'sales':
    generate_sales_report()
else:
    print("Invalid report type. Please try again.")
