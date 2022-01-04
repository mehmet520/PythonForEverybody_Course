# Worked Example: Page Rank - Computation (Chapter 16)
# will download and run a simple version of the Google PageRank Algorithm and 
# practice spidering some content.
# The assignment is peer-graded, and the first of three optional Honors assignments
# in the course. This a continuation of the material covered in Course 4 of the 
# specialization, and is based on Chapter 16 of the textbook.

import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('m5_w1_PRC_spider.sqlite')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS Pages(
        id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
        error INTEGER, old_rank REAL, new_rank REAL
    ); 
        CREATE TABLE IF NOT EXISTS Links(
        from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id)
    );
        CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)
    ''')

# Check to see if we are already in progress...
cur.execute('''SELECT id, url FROM Pages WHERE html is NULL and error is NULL 
ORDER BY RANDOM() LIMIT 1''')
row = cur.fetchone()
print ('39 row: ', row)
if row is not None:
    print("Resartingn existing crawl. Remove spider.sqlite to start a fresh crawl.")
else :
    starturl = input ('Enter web url or enter:')
    if (len(starturl) < 1): starturl = 'http://www.dr-chuck.com/'
    if (starturl.endswith('/') ): starturl = starturl[:-1]
    web = starturl
    print(starturl, web)
    if (starturl.endswith('.htm') or starturl.endswith('.html') ) :
        pos = starturl.rfind('/')
        web = starturl[:pos]

    if (len(web) > 1) :
        cur.execute('INSERT OR IGNORE INTO Webs(url) VALUES(?)', (web,))
        cur.execute('''INSERT OR IGNORE INTO Pages (url, html, new_rank) 
                    VALUES (?, NULL, 1.0)''', (starturl,))
        conn.commit()

# Get the current webs
cur.execute('SELECT url FROM Webs')
print('60 cur: ', cur)

webs = list()
for row in cur:

    print('65 row: ', row)

    webs.append(str(row[0]))

print('69 webs: ', webs)

many = 0
while True:
    if ( many < 1) :
        sval = input ('\nHow many pages: ')
        if (len(sval) < 1): break
    many = many - 1
    print('77 many: ', many)
    cur.execute(''' SELECT id,url FROM Pages WHERE html is NULL and
                error is NULL ORDER BY RANDOM() LIMIT 1''')
    try:
        row = cur.fetchone()
        print ('82 row: ', row)
        fromid = row[0]
        url = row[1]
    except:
        print ('No unretrieved HTML pages found')
        many = 0
        break

    print ('fromid: ', fromid, '\nurl: ', url, end= ' ')

    # If we are retrieving this page, there schould be no links from it
    cur.execute('DELETE FROM Links WHERE from_id=?', (fromid,))    
    try:
        document = urlopen(url, context = ctx)
        print('96 docement: ', document)
        html = document.read()
        print('html: ', html)
        if document.getcode() != 200 :
            print('document.getcode(): ', document.getcode())
            print(' Error on page: ', document.getcode())
            cur.execute('UPDATE Pages SET error = ? WHERE url = ?', (document.getcode(), url))

        if 'text/html' != document.info().get_content_type() :
            print("Ignore non text/html page")
            cur.execute('DELETE FROM Pages WHERE url = ?', (url,))
            conn.commit()
            continue

        print('html_lengt: ( '+str(len(html))+' )', end=' ')

        soup = BeautifulSoup(html, 'html.parser')
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except:
        print('Unable to retrieve or parse page')
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url,))
        conn.commit()
        continue
