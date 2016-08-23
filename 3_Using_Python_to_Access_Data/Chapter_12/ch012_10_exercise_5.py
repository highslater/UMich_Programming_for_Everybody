"""Extract and count paragraph (p) tags from the retrieved HTML document.

Python program that makes a connection to a web server and follows the rules
of the HTTP protocol to requests a document and display what the server sends
back.

Exercise 5:
(Advanced) Change the socket program so that it only shows data
after the headers and a blank line have been received. Remember that recv is
receiving characters (newlines and all), not lines.

"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(1024)
    pos = data.find('\r\n\r\n')
    if (len(data) < 1):
        break
    # print headers
    # print data[:pos]
    # print text
    print (data[pos + 4:])
mysock.close()
