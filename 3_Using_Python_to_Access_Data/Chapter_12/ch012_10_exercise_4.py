"""Extract and count paragraph (p) tags from the retrieved HTML document.

Python program that makes a connection to a web server and follows the rules
of the HTTP protocol to requests a document and display what the server sends
back.

Exercise 4:
Change the urllinks.py program to extract and count paragraph (p)
tags from the retrieved HTML document and display the count of the paragraphs
as the output of your program. Do not display the paragraph text, only count
them. Test your program on several small web pages as well as some larger web
pages.


"""

from urllib import urlopen as uo
from BeautifulSoup import BeautifulSoup as bS

default = 'http://www.py4inf.com/book.htm'
url = raw_input('Enter URL: ') or default
html = uo(url).read()
soup = bS(html)

# Retrieve all of the p tags
tags = soup('p')
count = 0
for tag in tags:
    count += 1
    print count
print 'total p tags:', count
