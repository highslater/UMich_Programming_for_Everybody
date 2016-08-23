"""Make a low-level network connection with sockets.

Python program that makes a connection to a web server and follows the rules
of the HTTP protocol to requests a document and display what the server sends
back.

Exercise 2:
Change your socket program so that it counts the number of
characters it has received and stops displaying any text after it has shown
3000 characters. The program should retrieve the entire document and count
the total number of characters and display the count of the number of
characters at the end of the document.

"""

import socket

default = 'http://www.py4inf.com/code/romeo.txt'
default_cutoff = '3000'
url = raw_input('Enter URL: ') or default
cutoff = (raw_input('Enter CUTOFF: ')) or default_cutoff
address = url.split('/')[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((address, 80))
mysock.send('GET ' + url + ' HTTP/1.0\n\n')
character_count = 0

while True:
    data = mysock.recv(1024)
    character_count = character_count + len(data)
    pos = data.find('\r\n\r\n')
    if (len(data) < 1):
        break
    print
    print "***** Included Content ***** "
    print
    print data[:int(cutoff)]
    print
    print "Cutoff: ", cutoff
    print
    print "***** Omitted Content ***** "
    print
    print data[int(cutoff) + 1:int(cutoff) + 100], ' >>>  more  <<<'
    print
print character_count
mysock.close()
