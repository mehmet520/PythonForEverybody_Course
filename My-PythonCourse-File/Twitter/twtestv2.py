import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
search_url = "https://api.twitter.com/2/tweets/search/all"
url = augment("https://api.twitter.com/2/tweets/search/all", {"screen_name": "MehmetY70026537", "count": "2"})
                # {'screen_name': '@drchuck', 'count': '2'})                
print('\nurl:\n', url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read
print('\ndata connection.read:\n', data)

print ('======================================')
headers = dict(connection.getheaders())
print('\nheaders:\n', headers)