"""Make a low-level network connection with sockets.

Python program that makes a connection to a web server and follows the rules
of the HTTP protocol to requests a document and display what the server sends
back.

Exercise 1:
Change the socket program to prompt the user for the
URL so it can read any web page. You can use split('/') to break the URL into
its component parts so you can extract the host name for the socket connect
call. Add error checking using try and except to handle the condition where
the user enters an improperly formatted or non-existent URL.

"""

import socket

default = 'http://www.py4inf.com/code/romeo.txt'
url = raw_input('Enter URL: ') or default
address = url.split('/')[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((address, 80))
mysock.send('GET ' + url + ' HTTP/1.0\n\n')

while True:
    data = mysock.recv(1024)
    pos = data.find('\r\n\r\n')
    if (len(data) < 1):
        break
    # print headers
    print data[:pos]
    # print text
    print data[pos:]
mysock.close()
