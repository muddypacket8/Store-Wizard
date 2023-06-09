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
        return f"<User(username='{self.username}', email='{self.email}')>"

engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

user = User(username='leonmwangi', password='passcode', email='leonmwas@gmail.com')
session.add(user)
session.commit()


def login(username, password):
    try:
        session = Session()

        # Retrieve the user with the provided username
        user = session.query(User).filter_by(username=username).one_or_none()

        # Validate the user's password
        if user and user.password == sha256(password.encode()).hexdigest():
            session.close()
            return "Login successful"
        else:
            session.close()
            return "Error: Invalid username or password"
    except NoResultFound:
        session.close()
        return "Error: Invalid username or password"
    except Exception as e:
        session.close()
        return "Error: " + str(e)
