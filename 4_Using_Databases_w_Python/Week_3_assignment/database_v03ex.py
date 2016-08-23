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
count = 1

for entry in all_short:
    next = False
    for key in entry:
        if key.tag == "key" and key.text == 'Name':
            next = True
            continue
        if next is True:
            name = key.text
            next = False
            continue

    for key in entry:
        if key.tag == "key" and key.text == 'Artist':
            next = True
            continue
        if next is True:
            artist = key.text
            next = False
            continue

    for key in entry:
        if key.tag == "key" and key.text == 'Album':
            next = True
            continue
        if next is True:
            album = key.text
            next = False
            continue

    for key in entry:
        if key.tag == "key" and key.text == 'Play Count':
            next = True
            continue
        if next is True:
            count = key.text
            next = False
            continue

    for key in entry:
        if key.tag == "key" and key.text == 'Rating':
            next = True
            continue
        if next is True:
            rating = key.text
            next = False
            continue

    for key in entry:
        if key.tag == "key" and key.text == 'Total Time':
            next = True
            continue
        if next is True:
            length = key.text
            next = False
            continue

    print name, artist, album, count, rating, length


conn.close()
