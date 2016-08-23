"""Following Links in Python.

Start at: http://python-data.dr-chuck.net/known_by_Christopher.html

"""

from urllib import urlopen as uo
from BeautifulSoup import BeautifulSoup as bS
u = raw_input('Enter URL: ')
c = int(raw_input('Enter count: '))
p = int(raw_input('Enter position: '))
print "Starting  : ", u
for i in range(c):
    h = uo(u).read()
    s = bS(h)
    t = s('a')
    u = str((t[p - 1]).get('href', None))
    print "Retrieving: ", u
