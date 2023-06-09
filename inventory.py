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

# Create product instances
product1 = Product(1, "shrink", 3245)
product2 = Product(5, "expand", 2500)
product3 = Product(2, "catriges,", 450)

# Add products to the session and commit the changes
session.add_all([product1, product2, product3])
session.commit()

# Retrieve the products from the database
products = session.query(Product).all()

# Create sales instances
sale1 = Sale(product_id=products[0].product_id, quantity=10)
sale2 = Sale(product_id=products[1].product_id, quantity=5)
sale3 = Sale(product_id=products[2].product_id, quantity=14)

# Add sales to the session and commit the changes
session.add_all([sale1, sale2, sale3])
session.commit()
