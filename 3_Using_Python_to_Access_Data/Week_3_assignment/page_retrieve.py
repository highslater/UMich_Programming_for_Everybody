"""Exploring the HyperText Transport Protocol.

You are to retrieve the following document using the HTTP protocol
in a way that you can examine the HTTP Response headers.

http://www.pythonlearn.com/code/intro-short.txt
There are three ways that you might retrieve this web page
and look at the response headers:

Preferred: Modify the socket1.py program to retrieve the above URL
and print out the headers and data.
Open the URL in a web browser with a developer console or FireBug
and manually examine the headers that are returned.
Use the telnet program as shown in lecture to retrieve the headers and content.


"""
# import socket
import socket


def browse():
    """Create, Connect, Get, and Close.

    Create the endpoint, connect to the endpoint,
    send application GET request, receive data, close the connection.
    """
    # create the endpoint
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the endpoint
    # the program makes a connection to port 80 on the server www.py4inf.com.
    mysock.connect(('www.py4inf.com', 80))

    # send application GET request
    # Modify the web_browser_v01.py program to retrieve the above URL
    # and print out the headers and data.
    mysock.send(
        'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'
    )

    # receive data
    # a loop that receives data in 512-character chunks from the socket and
    # prints the data out until there is no more data to read
    while True:
        data = mysock.recv(1024)
        pos = data.find('\r\n\r\n')
        if (len(data) < 1):
            break
        # print headers
        print data[:pos]
        # print text
        print data[pos:]
    # close the connection
    mysock.close()

# Call the function browse()
browse()
