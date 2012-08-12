#	DontGetMugged
#	HacknJill 2012
# 	Author: miriam.melnick@gmail.com

from restful_lib import Connection
from temboo.Library.Google.Geocoding.GeocodeByAddress import GeocodeByAddress
from temboo.miriam import MyTemboo
from xml.dom.minidom import parseString
import xml.dom
import json



def test_rest(myLat, myLng):
	# http://api.spotcrime.com/crimes.json?lat=40.740234&lon=-73.99103400000001&radius=0.01&callback=jsonp1339858218680&key=MLC
	spotcrime_base_url = "http://api.spotcrime.com"
	
	conn = Connection(spotcrime_base_url)

	resp = conn.request_get("/crimes.json", args={	'lat'	: myLat,
													'lon'	: myLng,		
													'radius': '0.01',
													'key' 	: 'MLC'},
											headers={'Accept': 'text/json'})
	
	
	resp_body = resp["body"]
	return resp_body
	

#test_rest(40.740234, -73.99103400000001)

def geocode(myAddress):
	
	# Instantiate a Temboo session with valid APP key credentials
	session = MyTemboo('dontGetMugged', 'jnQ9JFRM6NqiNCUUaYyw')
	
	# Instantiate the choreography, using the session object
	choreo = GeocodeByAddress(session)
	
	# Get an InputSet object for the choreo
	inputs = choreo.new_input_set()
	
	# Set inputs
	inputs.set_Address(myAddress)
	
	# Execute choreo
	results = choreo.execute_with_results(inputs)
	
	readResult = results.get_Response().encode('utf-8')
	
	#print readResult
	
	dom1 = parseString(readResult)
	
	myLat = dom1.getElementsByTagName('location').item(0).getElementsByTagName('lat').item(0).firstChild.nodeValue
	myLng = dom1.getElementsByTagName('location').item(0).getElementsByTagName('lng').item(0).firstChild.nodeValue
	
	print 'Latitude = ' + myLat
	print 'Longitude = ' + myLng
	
	return [myLat, myLng]

#def parseJson(jsoninput):
#	print jsoninput["crimes"]
	


def main():
	coords = geocode('50 West 23 Street, NY')
	crimeJson = test_rest(coords[0], coords[1])
#	parseJson(crimeJson)



main()
#item(0).childNodes[0].data
#print dom1.getElementsByTagName('location')[0].firstChild().nodeValue