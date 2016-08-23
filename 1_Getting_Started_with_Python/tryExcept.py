aString = "Hello Bob"
try:
    intString = int(aString)
except:
    intString = -1

print "First", intString

aString = "123"
try:
    intString = int(aString)
except:
    intString = -1
print "Second", intString
