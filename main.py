from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(100), unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


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


def enter_user(session):
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    user = User(username=username, password=password, email=email)
    session.add(user)
    session.commit()
    print("User added successfully.")


def enter_customer(session):
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")

    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    print("Customer added successfully.")


def enter_product(session):
    product_id = int(input("Enter product ID: "))
    product_name = input("Enter product name: ")
    price = int(input("Enter product price: "))

    product = Product(product_id=product_id, product=product_name, price=price)
    session.add(product)
    session.commit()
    print("Product added successfully.")


def enter_sale(session):
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter sale quantity: "))

    sale = Sale(product_id=product_id, quantity=quantity)
    session.add(sale)
    session.commit()
    print("Sale added successfully.")


def print_report(session):
    # Fetch all products
    products = session.query(Product).all()

    # Fetch all sales
    sales = session.query(Sale).all()

    product_report = []
    sale_report = []

    for product in products:
        product_report.append({'product': product.product, 'price': product.price})

    for sale in sales:
        product = session.query(Product).get(sale.product_id)
        sale_report.append({'product': product.product, 'quantity': sale.quantity})

    print("-------- Product Report --------")
    for product in product_report:
        print(f"Product: {product['product']} | Price: {product['price']}")

    print("\n-------- Sales Report --------")
    for sale in sale_report:
        print(f"Product: {sale['product']} | Quantity: {sale['quantity']}")

    print("\n-------- End of Reports --------")


def main():
    # Create the engine and session
    engine = create_engine('sqlite:///database/database.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("1. Enter User")
        print("2. Enter Customer")
        print("3. Enter Product")
        print("4. Enter Sale")
        print("5. Print Reports")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_user(session)
        elif choice == "2":
            enter_customer(session)
        elif choice == "3":
            enter_product(session)
        elif choice == "4":
            enter_sale(session)
        elif choice == "5":
            print_report(session)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    session.close()


if __name__ == "__main__":
    main()
