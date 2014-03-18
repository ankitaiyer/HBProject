from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import NoResultFound

ENGINE = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))
#NoResultFound = None

#ENGINE = None
#Session = None

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    firstname = Column(String(64), nullable=False)
    lastname = Column(String(64),nullable=False)
    email = Column(String(64), nullable =False)
    password = Column(String(64), nullable=False)


class Address(Base):
    __tablename__ = "Addresses"
    id = Column(Integer, primary_key = True)
    street = Column(String(65), nullable=False)
    city = Column(String(15), nullable=False)
    state = Column(String(15), nullable=False)
    zipcode = Column(String(15), nullable=False)
    mobile = Column(String(15), nullable=True)
    home = Column(String(15), nullable=True)
    work = Column(String(15), nullable=True)
    lng = Column(String(15), nullable=True)
    lat = Column(String(15), nullable=True)

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///carpool.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()
    # any time you need a session later, you can just do 'session = Session()'
