# https://www.py4e.com/tools/python-data/?PHPSESSID=42a85e31df874e5e0130be97f2c3489e
#  Willkommen, Mehmet Yilmaz aus Using Python to Access Web Data
# Calling a JSON API
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service 
# and parse that data, and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

# API End Points
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
# http://py4e-data.dr-chuck.net/json?
# This API uses the same parameter (address) as the Google API. 
# This API also has no rate limit so you can test as often as you like. 
# If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter
# that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

# Make sure to check that your code is using the API endpoint is as shown above.
# You will get different results from the geojson and json endpoints 
#so make sure you are using the same end point as this autograder is using.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# location_name= 'South Federal University'
# location_name= 'Banaras Hindu University'
api_key = False
# If you have a Google Place API key, enter it here
# api_key = 'Akllkkk....lkkk'
# https://developers.google.com/maps/documentation/geocoding/intro
if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    location_name = input('\nEnter Location (Name): ')
    if len(location_name) < 1: 
        print('\nThis is not a valid location name!\n')
        break
    parms = dict()
    parms['address'] = location_name
    if api_key is not False: parms['key'] = api_key
    # print('\nparms: ', parms)
    parms_encode = urllib.parse.urlencode(parms)
    # print('parms_encode: ',parms_encode)
    
    url_address = service_url + parms_encode
    # print('url_address: ', url_address)
    print('Retrieving', url_address)
    url_connect = urllib.request.urlopen(url_address, context = ctx)
    # print('\nurl_connect :\n', url_connect)
    url_read = url_connect.read().decode('utf-8')
    # print('\nurl_read:', url_read)
    print('Retrieving ', len(url_read), 'characters')
    try:
        js_data = json.loads(url_read)
    except:
        js_data = None
        print('There is no data!')
    if not js_data or 'place_id' not in js_data['results'][0] or len(js_data) < 1:
        print('======== Failure to retrieve ========')
        print('Data:\n', json.dumps(js_data, indent=4))
        continue
    # print('jason_data: ', json.dumps(js_data, indent=4))
    place_id = js_data['results'][0]['place_id']
    print('Place id ', place_id)

