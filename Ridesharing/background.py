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
import numpy 
from scipy.cluster.vq import *
import unicodedata 



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
    latlng = []
    for adr in result:
        tup_item1 = float(unicode(adr.lat)) if adr.lat else None
        tup_item2 = float(unicode(adr.lng)) if adr.lng else None
        tup = (tup_item1, tup_item2)
        #print "TUP:", tup
        latlng.append(tup)
        #print "latlng" , latlng
    return latlng

def get_latlng_clustercenter(data, clusterscount):
    centers = kmeans2(data, clusterscount)
    print "centers: ", centers[0]
    return centers[0]
    #print "DATA IS: ",data
    #centers,idx = kmeans2(data, clusterscount)
    #return centers,idx



def main(session):
    # You'll call each of the load_* functions with the session as an argument

    ## Sample code to test geo function call
    # lat,lng = geo.geocode("84 Madrid place, Fremont, CA, 94539", "false")
    # return  lat,lng

    #Call geo code function to load latlng for addresses where latlng is missing
    load_latlng(session)

    #Get all latlng available in the Address table to calculate ceter using kmeans clustering. Return data as Tuple
    latlng_list = get_latlng()

    
    #sample data
    # data = numpy.array([[  37.7708158, -122.421831 ],
    #    [  37.4301485, -122.098137 ], [37.9559086,-122.088220],[37.158562,-122.930034],[37.7901435,-122.290267],[37.31463,-122.147957]])
    data = numpy.array(latlng_list)
    centers = get_latlng_clustercenter(data,6)
    # print "Centers are: ", centers
    # print "idx is:," ,idx


if __name__ == "__main__":
    session= model.connect()
    main(session)
   

