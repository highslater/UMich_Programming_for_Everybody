"""10.2 Write a program to read through the mbox-short.txt.

Write a program to read through the mbox-short.txt and
figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and
then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour,
print out the counts, sorted by hour as shown below.

"""


def hourly_distribution(fname):
    """Figure out the distribution by hour for each of the messages."""
    distribution = dict()
    hours = list()
    fh = open(fname)
    for line in fh:
        if line.startswith("From:"):
                continue
        if line.startswith("From"):
            hour = line.strip().split()[5].split(":")[0]
            distribution[hour] = distribution.get(hour, 0) + 1
    for k, v in distribution.items():
        hours.append((k, v))
    hours.sort(reverse=False)
    return hours


fname = raw_input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
hours = hourly_distribution(fname)
for k, v in hours:
    print k, v
