"""7.2 Write a program that prompts for a file name.

Write a program that prompts for a file name,
then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each
of the lines and compute the average of those values and produce
an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at
http://www.pythonlearn.com/code/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
num = float(text[pos + 1:])
print num

"""

# Use the file name mbox-short.txt as the file name


def average_spam(fname):
    """Compute the average of values."""
    fh = open(fname)
    count = 0
    total = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        count = count + 1
        pos = line.find(':')
        num = float(line[pos + 1:])
        total = total + num
    return (total) / (count)


fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = "mbox-short.txt"
print "Average spam confidence:", average_spam(fname)
