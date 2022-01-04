import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect ('db_w3_Tracks.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript ('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    album_id INTEGER,
    title TEXT UNIQUE,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')
# fname = input ('Enter file name:  ')
# if (len(fname) < 1): fname = 'db_w3_Track_Library.xml'
fname = 'db_w3_Track_Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:  # Hier chilg gives the 'Tags Object'  respectively. 
        # i.e. : 1.Tag: <key>Track ID</key>, 2.Tag: <integer>369</integer>
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
# stuff (dict)= <xml.etree.ElementTree.ElementTree object at 0x000001D9F56F1040>
# There is Dicts (count: 404) inside stuff
all_dict = stuff.findall('dict/dict/dict') # List of 3. level dictionaries  
print('all_dict count:  ', len(all_dict))
for entry in all_dict:
    if (lookup(entry, 'Track ID') is None): continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Album Rating')
    length = lookup(entry, 'Total Time')
    
    if name is None or artist is None or album is None:
        continue
    print (name, artist, album, count, rating, length)

    cur.execute(''' INSERT OR IGNORE INTO Artist (name)
                VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )

    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track 
    (title, album_id, len, rating, count) VALUES
    ( ? , ? , ? , ? , ? )''', (name, album_id, length, rating, count))

    # cur.execute('''SELECT id, title, album_id, len, rating, count FROM Track 
    # WHERE title = ?''', (name,))
    # t = cur.fetchone()  #Track:  (1, 'Another One Bites The Dust', 1, 217103, 100, 55) typ:  <class 'tuple'>
    # t = cur.fetchone()[0]   # Track:  1 typ:  <class 'int'>
    # t = cur.fetchone()[1]   # Track:  Another One Bites The Dust typ:  <class 'str'>
    # t = cur.fetchall()  # Track:  [(1, 'Another One Bites The Dust', 1, 217103, 100, 55)] typ:  <class 'list'>
    # print ('Track: ', t, 'typ: ', type(t))
    # d=input()

conn.commit()
cur.close()