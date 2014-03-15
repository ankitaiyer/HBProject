import urllib2, urllib, json, re, cookielib, requests
from gmaps import Geocoding
import simplejson, urllib

#Please collect your project api_key
api_key = ''
GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

def geocode(address,sensor, **geo_args):
    geo_args.update({
        'address': address,
        'sensor': sensor
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = simplejson.load(urllib.urlopen(url))
    #prints formatted address 
    print "FORMATTED ADDRESS IS ", simplejson.dumps([s['formatted_address'] for s in result['results']], indent=2)
    #prints lat and lng for the selected address
    print  "LATTITUDE IS: " , simplejson.dumps([s['geometry']['location']['lat'] for s in result['results']], indent=2)    
    print  "LONGITUDE IS: " , simplejson.dumps([s['geometry']['location']['lng'] for s in result['results']], indent=2)    
  
def reverse_geocode(latlng,sensor,location_type,result_type, **geo_args):
    print "LAT AND LNG ARE: ", latlng
    geo_args.update({
        'latlng': latlng,
        'location_type': location_type,
        'result_type': result_type,
        'sensor': sensor,
        'key':api_key
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = simplejson.load(urllib2.urlopen(url))
    print "FORMATTED ADDRESS IS ", simplejson.dumps([s['formatted_address'] for s in result['results']], indent=2)


if __name__ == '__main__':
    block = "1600"
    street = "Amphitheatre Parkway"
    city = "Mountain View"
    state = "CA"

    lattitude = 40.714224
    longitude =  -73.961452
    location_type = "ROOFTOP" 
    result_type = "street_address"

    
    address = block + "+" + street + "+" + city + "+" + state
    latlng = str(lattitude) + "," + str(longitude)
    geocode(address=address ,sensor="false")
    reverse_geocode(latlng=latlng,location_type=location_type,result_type=result_type,sensor="true")



