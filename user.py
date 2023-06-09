from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from hashlib import sha256

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

engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
def add_user(username, password, email):
    try:
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            print("Error: Username already exists.")
            return

        new_user = User(username=username, password=password, email=email)
        session.add(new_user)
        session.commit()
        print("User added successfully.")
        print(new_user)  # Print the added user
    except Exception as e:
        print("Error: ", str(e))

# # Edit a user's email
# def edit_user_email(user_id, new_email):
#     try:
#         user = session.query(User).get(user_id)
#         if user:
#             user.email = new_email
#             session.commit()
#             print("User email updated successfully.")
#             print(user)  # Print the updated user
#         else:
#             print("User not found.")
#     except Exception as e:
#         print("Error: ", str(e))

# # Delete a user
# def delete_user(user_id):
#     try:
#         user = session.query(User).get(user_id)
#         if user:
#             session.delete(user)
#             session.commit()
#             print("User deleted successfully.")
#             print(user)  # Print the deleted user
#         else:
#             print("User not found.")
#     except Exception as e:
#         print("Error: ", str(e))


# # Example usage:
# add_user("timothy", "press", "timon@gmail.com")
# edit_user_email(1, "leonmwas@gmail.com")
# delete_user(1)
