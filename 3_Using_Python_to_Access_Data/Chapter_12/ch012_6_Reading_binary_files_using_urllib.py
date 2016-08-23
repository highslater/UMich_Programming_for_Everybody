"""Reading binary files using urllib.

Retrieve a non-text (or binary) file.
This program reads all of the data in at once across the network and stores it
in the variable img in the main memory of your computer, then opens the file
cover.jpg and writes the data out to your disk. This will work if the size of
the file is less than the size of the memory of your computer.

However if this is a large audio or video file, this program may crash or at
least run extremely slowly when your computer runs out of memory. In order to
avoid running out of memory, we retrieve the data in blocks (or buffers) and
then write each block to your disk before retrieving the next block. This way
the program can read any size file without using up all of the memory you have
in your computer.
"""

from urllib import urlopen as uo

default = 'http://www.py4inf.com/cover.jpg'
url = raw_input('Enter URL: ') or default
img = uo(url).read()
fhand = open('cover.jpg', 'w')
fhand.write(img)
fhand.close()
