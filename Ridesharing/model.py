from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import DateTime
import geo
import background

ENGINE = create_engine("sqlite:///carpool.db", echo=False)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))
#NoResultFound = None

#ENGINE = None
#Session = None

Base = declarative_base()
Base.query = session.query_property()


## Class declarations go here
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    firstname = Column(String(64), nullable=False)
    lastname = Column(String(64),nullable=False)
    email = Column(String(64), nullable =False)
    password = Column(String(64), nullable=False)
    mobile = Column(String(15), nullable=True)
    home = Column(String(15), nullable=True)
    work = Column(String(15), nullable=True)


class Address(Base):
    __tablename__ = "Addresses"
    id = Column(Integer, primary_key = True)
    street = Column(String(65), nullable=False)
    city = Column(String(15), nullable=False)
    state = Column(String(15), nullable=False)
    zipcode = Column(String(15), nullable=False)
    lng = Column(String(15), nullable=True)
    lat = Column(String(15), nullable=True)


class Commute(Base):
    __tablename__ = "Commute"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, nullable=False)
    start_addr_id = Column(Integer, nullable=False)
    end_addr_id = Column(Integer, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)


def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///carpool.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()
    # any time you need a session later, you can just do 'session = Session()'

def authenticate(emailform, passwordform):
    user = session.query(User).filter_by(email=emailform).first()
    if int(user.password) == int(passwordform):
        return user.email
    else:
        return "Auth failed"

def register_user(firstnameform, lastnameform, emailform, passwordform):
    temp_user = User(firstname=firstnameform, lastname=lastnameform, email=emailform, password=hash(passwordform))
    session.add(temp_user)
    session.commit()


def get_user_by_email(email):
    userid = session.query(User).filter_by(email=email).first()
    print "user", userid.id
    return userid.id

#### TODO 
def complete_commute_profile(user_id, startaddrform, destaddrform, starttimeform,endtimform,mobileform,workform,homeform):
    adr_list = [startaddrform, destaddrform]
    for adr in adr_list:
        address = adr.split()
        street = address[0] + " " + address[1]
        temp_addr = Address(street=street, city=address[2], state=address[3], zipcode=address[4])
        session.add(temp_addr)

    current_user = session.query(User).filter_by(id=user_id).first()
    if current_user:
        current_user.mobile = mobileform
        current_user.home = homeform
        current_user.work = workform
        session.add(current_user)

    session.commit()

def get_destination_addresses():




def main():
    Base.metadata.create_all(ENGINE)


if __name__ == "__main__":
    main()












