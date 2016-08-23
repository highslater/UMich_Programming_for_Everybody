"""Retrieving web pages with urllib.

While we can manually send and receive data over HTTP using the socket library,
there is a much simpler way to perform this common task in Python by using the
urllib library.
Using urllib, you can treat a web page much like a file. You simply indicate
which web page you would like to retrieve and urllib handles all of the HTTP
protocol and header details.
The equivalent code to read the romeo.txt file from the web using urllib is as
follows.

"""
import urllib

counts = dict()
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

val = list(counts.values())
key = list(counts.keys())
w_max = max(val)
max_words = list()

for k, v in counts.iteritems():
    print k, v
    if v == w_max:
        max_words.append(k)

if len(max_words) > 1:
    print "The words at a maximum count of", w_max, "are: ",
    x = len(max_words)
    for word in max_words:
        if (x == 1):
            print '&', word + '.'
        else:
            print word + ',',
            x = x - 1
else:
    print "The word at a maximum count of", w_max, "is:", max_words[0]
