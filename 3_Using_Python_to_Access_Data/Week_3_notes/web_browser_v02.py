"""Import, Open, Receive and Close.

Import urllib, create the endpoint, connect to the endpoint,
send application GET request, receive data, close the connection.
"""

# import urllib
import urllib


def browse():
    """Open, Receive, and Close.

    Open url, receive data, close the connection.
    """
    # open url
    fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
    # receive data
    for line in fhand:
        print line.strip()


# Call the function browse()
browse()
