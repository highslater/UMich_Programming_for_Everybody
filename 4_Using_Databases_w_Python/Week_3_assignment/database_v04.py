"""Read file in XML and produce a properly normalized database.

Submit

"""
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()
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


for entry in all_short:
    name = get_it(entry, 'Name')
    artist = get_it(entry, 'Artist')
    album = get_it(entry, 'Album')
    count = get_it(entry, 'Play Count')
    rating = get_it(entry, 'Rating')
    length = get_it(entry, 'Total Time')
    print
    print " ~", counter, "~"
    print "\tSong:\t\t", name
    print "\tArtist:\t\t", artist
    print "\tAlbum:\t\t", album
    print "\tCount:\t\t", count
    print "\tRating:\t\t", rating
    print "\tTotal Time:\t", length
    print
    counter += 1

conn.close()
