from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product = Column(String(100))
    price = Column(Integer)

    def __init__(self, product, price):
        self.product = product
        self.price = price

    def __repr__(self):
        return f"<Product(product='{self.product}', price={self.price})>"

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer)

    product = relationship("Product", backref="sales")

    def __init__(self, quantity):
        self.quantity = quantity

    def __repr__(self):
        return f"<Sale(id={self.id}, quantity={self.quantity})>"


# Create the engine and session
engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create product instances
product1 = Product(product="shrink", price=3245)
product2 = Product(product="expand", price=2500)
product3 = Product(product="cartridges", price=450)

# Add products to the session and commit the changes
session.add_all([product1, product2, product3])
session.commit()

# Retrieve the products from the database
products = session.query(Product).all()

# Create sales instances
sale1 = Sale(quantity=10)
sale1.product = product1

sale2 = Sale(quantity=5)
sale2.product = product2

sale3 = Sale(quantity=14)
sale3.product = product3

# Add sales to the session and commit the changes
session.add_all([sale1, sale2, sale3])
session.commit()

# Update a product
# product_to_update = session.query(Product).filter_by(product="expand").first()
# if product_to_update:
#     product_to_update.price = 2000
#     session.commit()

# Delete a sale
# sale_to_delete = session.query(Sale).filter_by(quantity=14).first()
# if sale_to_delete:
#     session.delete(sale_to_delete)
#     session.commit()

# Retrieve the updated products from the database
# updated_products = session.query(Product).all()
print(products)

