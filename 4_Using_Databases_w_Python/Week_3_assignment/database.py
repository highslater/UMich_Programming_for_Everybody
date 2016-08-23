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

# print "Contents of: ", fname
stuff = ET.parse(fname)
# print "001", stuff

all = stuff.findall('dict/dict/dict')
print "Dict Count: ", len(all)
# print "003 ", all[0]
# print "003 ", all[0].text, all[1].text
# print "004 ", all[0].tag, all[1].tag
# all_key = all.find('key')
# print all_key.text


def lookup(d, key):
    """Demonstrate high quality docstrings.

    Module-level docstrings appear as the first "statement" in a module.
    """
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    print name, artist, album, count, rating, length

conn.close()
