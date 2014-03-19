from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import DateTime
from sqlalchemy import or_
import model
import geo



def load_latlng(session):
    result = session.query(model.Address).filter(or_(model.Address.lat == '', model.Address.lng == '', model.Address.lat == None, model.Address.lng == None)).all()
    for adr in result:
        addr = []
        if (adr.lat == None or adr.lng == None):
            addr = [adr.street,adr.city,adr.state,adr.zipcode]
            format_addr = ",".join(addr) 
            lat,lng = geo.geocode(format_addr,"false")  
            adr.lat = lat
            adr.lng = lng
    session.commit()
  
def get_latlng():
    result = session.query(model.Address).all()
    for adr in result:
        tup = (adr.lat,adr.lng)
        print tup


def main(session):
    # You'll call each of the load_* functions with the session as an argument

    ## Sample code to test geo function call
    # lat,lng = geo.geocode("84 Madrid place, Fremont, CA, 94539", "false")
    # return  lat,lng

    #Call geo code function to load latlng for addresses where latlng is missing
    load_latlng(session)

    #Get all latlng available in the Address table to calculate ceter using kmeans clustering
    get_latlng()
    

if __name__ == "__main__":
    session= model.connect()
    main(session)
   

