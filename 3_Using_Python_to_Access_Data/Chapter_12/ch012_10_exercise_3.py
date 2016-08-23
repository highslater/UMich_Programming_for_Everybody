"""Use urllib to replicate the previous exercise.

Python program that makes a connection to a web server and follows the rules
of the HTTP protocol to requests a document and display what the server sends
back.

Exercise 3:
Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and (3)
counting the overall number of characters in the document. Don't worry about
the headers for this exercise, simply show the first 3000 characters of the
document contents.


"""

import urllib

default = 'http://www.py4inf.com/code/romeo.txt'
url = raw_input('Enter URL: ') or default
default_cutoff = '3000'
cutoff = (raw_input('Enter CUTOFF: ')) or default_cutoff
data = urllib.urlopen(url)
read_data = (data.read())

data_included = read_data[:int(cutoff)].strip()
data_included_lines = data_included.split("\n")
print
print "***** Included Content *****"
print "characters: ", len(data_included)
print "lines: ", len(data_included_lines)
print
for line in data_included_lines:
    print repr(line)
print "****************************"

data_omitted = read_data[int(cutoff):].strip()
data_omitted_lines = data_omitted.split("\n")
print
print "***** Omitted Content ***** "
print "characters: ", len(data_omitted)
print "lines: ", len(data_omitted_lines)
print
for line in data_omitted_lines:
    print repr(line)
print "****************************"
print '>>>  more  <<<'
print 'character_count', len(read_data)
