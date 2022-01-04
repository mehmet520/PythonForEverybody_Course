import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('db_w3_exam1_Musical_Track_Database.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Album(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );

    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    )
''')

# fname = input('Enter file name: ')
# if (len(fname)) < 1 : fname = 'Library.xml'
fname = 'Library.xml'

def lookup(entry, key):
    found = False
    for tg in entry:
        if found: return tg.text
        if tg.tag=='key' and tg.text==key:
            found = True
    return None


stuff = ET.parse(fname)
all_dict = stuff.findall('dict/dict/dict')

for entry in all_dict:
    if (lookup(entry, 'Track ID')) is None: continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')

    if artist is None or album is None or name is None or genre is None: continue
    print(name, artist, album, genre, length, rating, count)

    cur.execute(' INSERT OR IGNORE INTO Artist(name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name=?', (genre,))
    genre_id=cur.fetchone()[0]
    print(genre_id, type(genre_id))
    # s=input()
    cur.execute(''' INSERT OR IGNORE INTO Album(artist_id, title)
                VALUES ( ? , ? ) ''', (artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title=?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
    (title, album_id, genre_id, len, rating, count) VALUES 
    (?,?,?,?,?,?)''', (name, album_id, genre_id, length, rating, count))
conn.commit()
cur.close()