"""Demonstrate high quality docstrings.

Repeatedly search for and extract substrings that match a particular pattern.
Construct a well-formed regular expression to match and extract the link values
"""

from urllib import urlopen as uo
from re import findall as f

default = 'http://www.py4inf.com/book.html'
url = raw_input('Enter URL: ') or default
html = uo(url).read()
links = f('href="(http://.*?)"', html)
for link in links:
    print link
