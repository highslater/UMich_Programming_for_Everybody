#  So here's our exercise.
#  We're supposed to rewrite our pay program and we're
#  going to use try and except
#  in this situation so that we can handle non-numeric input gracefully.
#  And we're supposed to print out an error if there's any
#  non-numeric input and
#  otherwise print out the right thing. So let's get started.


try:
    hours = float(raw_input("Enter Hours: "))
    rate = float(raw_input("Enter rate: "))
except:
    print "Error, please enter numeric input"
    quit()

if hours <= 40:
    pay = rate * hours

else:
    pay = rate * 40 + 1.5 * rate * (hours - 40.0)

print pay
