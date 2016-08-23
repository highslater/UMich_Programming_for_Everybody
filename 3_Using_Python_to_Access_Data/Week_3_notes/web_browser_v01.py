"""Import, Create, Connect, Get, and Close.

Import socket, create the endpoint, connect to the endpoint,
send application GET request, receive data, close the connection.
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
    mysock.connect(('www.py4inf.com', 80))

    # send application GET request
    mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

    # receive data
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print data
    # close the connection
    mysock.close()

# Call the function browse()
browse()
