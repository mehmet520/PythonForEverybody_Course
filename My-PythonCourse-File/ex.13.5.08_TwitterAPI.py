import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json' 
print('\nurl:\n', TWITTER_URL)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input ('Enter Twitter Account:')
    if (len(acct)<1): break
    url = twurl.augment (TWITTER_URL, {'screen_name': acct, 'count': '2'})
    print ('\nRetrieving: \n, url')
    connection = urllib.request.urlopen(rul, context=ctx)
    data = connection.read().decode()
    print ('\ndata: \n', data[:250])
    print('==========================================')
    headers = dict(connection.getheaders())
    # print headers
    print('\nRemaining (headers): \n', headers['x-rate-limit-remaining'])



