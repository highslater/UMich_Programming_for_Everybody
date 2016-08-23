"""7.1 Write a program that prompts for a file name.

Write a program that prompts for a file name, then opens
that file and reads through the file, and print the contents of the
file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at
http://www.pythonlearn.com/code/words.txt

"""


def char_count(fname):
    """Count the number of characters in a file."""
    fh = open(fname, 'r')
    fs = fh.read().replace('\n', ' ')
    count = 0
    for char in fs:
        count = count + 1
    print ""
    print 'The number of characters in "%s" is: %s' % (fname, count)


def line_count(fname):
    """Count the number of lines in a file."""
    fh = open(fname, 'r')
    count = 0
    for line in fh:
        count = count + 1
    print ""
    print 'The number of lines in "%s" is: %s' % (fname, count)


def shout(fname):
    """Return a file as uppercase."""
    fh = open(fname, 'r')
    print ""
    for line in fh:
        print line.upper().rstrip()


# Use words.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = "mbox-short.txt"
line_count(fname)
char_count(fname)
# shout(fname)
