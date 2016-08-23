"""Read file in XML and produce a properly normalized database.

Submit
You do not need to export or convert the database - simply upload the .sqlite
file that your program creates. See the example code for the use of the
connect() statement.

Musical Track Database
This application will read an iTunes export file in XML and produce a properly
normalized database with this structure:

If you run the program multiple times in testing or with different files, make
sure to empty out the data before each run.

You can use this code as a starting point for your application:
http://www.pythonlearn.com/code/tracks.zip.

The ZIP file contains the Library.xml file to be used for this assignment.
You can export your own tracks from iTunes and create a database, but for the
database that you turn in for this assignment, only use the Library.xml data
that is provided.

To grade this assignment, the program will run a query like this on your
uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
    AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre
    (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

''')

default = 'Library.xml'
fname = raw_input('Enter file name: ') or default
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
all_short = all[:5]
counter = 1


def get_it(entry, label):
    """Demonstrate high quality docstrings.

    Module-level docstrings appear as the first "statement" in a module.
    """
    present = False
    for key in entry:
        if present:
            return key.text
        if key.tag == "key" and key.text == label:
            present = True
    return None


for entry in all:
    artist = get_it(entry, 'Artist')
    genre = get_it(entry, 'Genre')
    album = get_it(entry, 'Album')
    track = get_it(entry, 'Name')
    if artist is None or genre is None or album is None or track is None:
        continue
    print
    print " ~", counter, "~"
    print "\tArtist:\t\t", artist
    print "\tGenre:\t\t", genre
    print "\tAlbum:\t\t", album
    print "\tTrack:\t\t", track
    print
    counter += 1

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id)
        VALUES ( ?, ?, ?)''', (track, album_id, genre_id))

conn.commit()

conn.close()

# TEST:
# SELECT Track.title, Artist.name, Album.title, Genre.name
#     FROM Track JOIN Genre JOIN Album JOIN Artist
#     ON Track.genre_id = Genre.ID and Track.album_id = Album.id
#         AND Album.artist_id = Artist.id
#     ORDER BY Artist.name, Track.title LIMIT 3

# DESIRED OUTPUT:
# Track   Artist  Album   Genre
# Chase the Ace   AC/DC   Who Made Who    Rock
# D.T.    AC/DC   Who Made Who    Rock
# For Those About To Rock (We Salute You) AC/DC   Who Made Who    Rock
