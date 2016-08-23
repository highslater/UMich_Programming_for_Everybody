"""Scrape web pages with BeautifulSoup.

Enter an url, enter a tag, call function 'scrape(url, tag)',
which:
opens and reads the url, parses html with BeautifulSoup,
retrieves a list of tags, returns the list.
Then:
print out the list of tags.

"""
# import urllib
import urllib
# use BeautifulSoup
from BeautifulSoup import BeautifulSoup


def scrape(url, tag):
    """Scrape web pages with BeautifulSoup.

    open and read the url, parse html with BeautifulSoup,
    retrieve a list of tags, return tags.

    """
    # open and read (read it all) the url
    html = urllib.urlopen(url).read()
    # parse html with BeautifulSoup
    soup = BeautifulSoup(html)
    # retrieve a list of the anchor tags
    tags = soup(tag)
    # return tags
    return tags


# enter the url
url = raw_input('Enter url: ')
# enter the tag
tag = raw_input('Enter tag: ')
# Call the function scrape()
attribute = raw_input('Enter attribute: ')
# Call the function scrape()
tags = scrape(url, tag)
# print out the tags
for tag in tags:
    if not attribute:
        print tag
    print tag.get(attribute, None)

# In this Python code, which line is most like the open() call to read a file:
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# mysock.connect(('www.py4inf.com', 80))

# mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     print data
# mysock.close()
