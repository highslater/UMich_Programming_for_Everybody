"""Extracting Data from XML.

In this assignment you will write a Python program somewhat similar to
http://www.pythonlearn.com/code/geoxml.py.
"""

from urllib import urlopen as u
from xml.etree.ElementTree import fromstring as fs
default = 'http://python-data.dr-chuck.net/comments_297292.xml'
url = raw_input('Enter location: ') or default
data = u(url).read()
print 'Retrieving', url, "\nRetrieved", len(data), 'characters'
counts = fs(data).findall('.//count')
kounts = list()
for count in counts:
    kounts.append(int(count.text))
Sum = reduce(lambda c, s: c + s, kounts)
print "Count: ", len(counts), "\nSum: "
