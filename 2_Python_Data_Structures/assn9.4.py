"""9.4 figure out who has sent the greatest number of mail messages.

Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines
as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary
using a maximum loop to find the most prolific committer..

"""


def greatest_sender(fname):
    """Figure out who has sent the greatest number of mail messages."""
    fh = open(fname)
    senders = dict()
    for line in fh:
        # find line that starts with From not From: and split it.
        if line.startswith("From:"):
                continue
        if line.startswith("From"):
            name = line.split()[1]
            senders[name] = senders.get(name, 0) + 1
    # compute and return maximum
    prolific = None
    for k, v in senders.items():
        if prolific is None or v > prolific[1]:
            prolific = (k, v)
    return prolific


fname = raw_input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
name, number = greatest_sender(fname)
print name, number
