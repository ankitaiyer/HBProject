from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import DateTime
import model
import geo



def load_latlng(session):
    result = session.query(model.Address).all()
    # print result[0].lat
    # print result[0].lng
   
    for adr in result:
        # print "RESULT lat IS ", adr.lat 
        # print "RESULT LNG is", adr.lng
        addr = []
        if (adr.lat == None or adr.lng == None):
            addr = [adr.street,adr.city,adr.state,adr.zipcode]
            format_addr = ",".join(addr) 
            print format_addr   
            lat,lng = geo.geocode(format_addr,"false")  
            print lat, lng
            adr.lat = lat
            adr.lng = lng
    session.commit()
  
    

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_latlng(session)

    # lat,lng = geo.geocode("84 Madrid place, Fremont, CA, 94539", "false")
    # return  lat,lng




if __name__ == "__main__":
    session= model.connect()
    main(session)
   

