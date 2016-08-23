"""Parsing HTML using BeautifulSoup.

Parse HTML and extract data from the pages.
Parse some HTML input and extract links using the BeautifulSoup library.
Use urllib to read the page and then use BeautifulSoup to extract the href
attributes from the anchor (a) tags.
The program prompts for a web address, then opens the web page, reads the data
and passes the data to the BeautifulSoup parser, and then retrieves all of the
anchor tags and prints out the href attribute for each tag.


"""

from urllib import urlopen as uo
from BeautifulSoup import BeautifulSoup as bS

default = 'http://www.py4inf.com/book.html'
url = raw_input('Enter URL: ') or default
html = uo(url).read()
soup = bS(html)

# Retrieve all the anchor tags
tags = soup('a')
print
print len(tags)
print
i = 1
for tag in tags:
    print "LINK:", i
    i = i + 1
    print "The tag is: ", tag
    print "The URL is: ", tag.get('href', None).strip()
    print "The target is: ", tag.get('target', None).strip()
    print "The content is: ", tag.contents[0].strip()
    print "The attributes are: ", (tag.attrs)
    print "The text is: ", tag.text.strip()
    print
