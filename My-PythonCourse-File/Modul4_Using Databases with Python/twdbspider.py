from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
conn = sqlite3.connection('twdbspider.sqlite')
cur = conn.curosr()
cur.execute('''CREATE TABLE IF NOT EXISTS 
Twitter (name TEXT, retrieved INTEGER, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print ('No unretrieved Twitter account found')
            continue
        
    url = twurl.augment(TWITTER_URL, {'screen_name':acct, 'count':'20'})   
    print('Retrieving ', url)
    connection = urlopen(url, context = ctx)    
    data = connection.read().decoce()
    headers = dict(connection.getheaders())

    print ('Remaning try right is ', headers['x-rate-limit-remainin'])
    data_js = json.loads(data)
    # Debugging
    # print(json.dumps(data_js, indent = 4))

    cur.execute('UPDATE Twitter SET  retrieved = 1 WHERE acct = ?', (acct,))

    countnew = 0
    countold = 0
    for u in data_js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend,))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ?  WHERE name = ?', (count + 1, friend))
            countold = 1            
        except:
            cur.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)', (friend))
            countnew = countnew + 1
            
    print('New accounts= ', countnew, ' ; revisited= ', countold)
    conn.commit()
cur.close()
        
