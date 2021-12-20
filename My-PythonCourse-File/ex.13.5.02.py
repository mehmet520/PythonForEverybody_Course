import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('\n servisurl: \n', serviceurl)
s=input()

while True:
    # address = input('Enter location: ')
    address = 'Gierather Str. 16, 51069 Köln'
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    print ('\nparms: \n', parms)
    s=input()
    x= urllib.parse.urlencode(parms)
    print('\nx: \n', x)
    s=input()
    url = serviceurl + urllib.parse.urlencode(parms)

    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    print ('\nuh: \n', uh)
    s=input()

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    print('\ndata: \n', data)
    s=input()

    try:
        js = json.loads(data)
    except:
        js = None
    print ('\njs:   \n', js)
    s=input()

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    break

