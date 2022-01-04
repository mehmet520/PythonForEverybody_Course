CREATE TABLE Genre ( 
 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,  
 name TEXT );
 
CREATE TABLE Album ( 
 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
 name TEXT);
 
 ALTER TABLE Album ADD artist_id INTEGER;
 
 
 
 PRAGMA foreign_keys=off;
 

 ALTER TABLE Album RENAME TO _Album_old;
 CREATE TABLE Album (
 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
 artist_id INTEGER,
 title TEXT);
 INSERT INTO Album ( id, artist_id, title)
 SELECT id, artist_id, name FROM _Album_old;
 COMMIT;
 PRAGMA foreign_keys = on;
 
DROP TABLE _Album_old;

CREATE TABLE Track (
 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
 title TEXT,
  album_id INTEGER,
   genre_id INTEGER,
   len INT, rating INT, count INTEGER);
   
 INSERT INTO Artist (name) VALUES ('Led Zepplin');
 INSERT INTO Artist (name) VALUES ('AC/DC');
 
 INSERT INTO Genre (name) VALUES ('Rock');
 INSERT INTO Genre(name) VALUES ('Metal');
 
 INSERT INTO Album (artist_id, title)  VALUES(2, 'Who Made Who');
 INSERT INTO Album (title, artist_id) VALUES ('IV', 1);
 
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ( 'Black Dog', 5, 297, 0,2,1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
VALUES ('Stairway', 5, 482,0,2,1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
VALUES ( 'About to Rock', 5, 313, 0,1,2);

DELETE FROM Track WHERE len = 207;

INSERT INTO Track ( title, rating, len, count, album_id, genre_id)
VALUES ( 'Who Made Who', 5, 207, 0, 1, 2);

SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id=Artist.id;

SELECT Track.title, Genre.name FROM Track JOIN Genre on Track.genre_id=Genre.id;

SELECT Track.title, Genre.name FROM Track JOIN Genre;

SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Genre JOIN Album JOIN Artist   
on Track.genre_id= Genre.id AND  Track.album_id=album_id AND Album.artist_id=Artist.id;

SELECT Track.title, Artist.name
FROM Track JOIN Artist  JOIN Album
on Track.album_id=album_id AND Album.artist_id = Artist.id;