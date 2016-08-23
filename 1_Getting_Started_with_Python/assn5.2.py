# 5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number
# catch it with a try/except
# and put out an appropriate message and ignore the number.
# Enter the numbers from the book for problem 5.1 and Match
# the desired output as shown.


def user_prompt():
    int_numbers = (raw_input("Please enter an integer: "))
    if int_numbers == 'done':
        return int_numbers
    try:
        return int(int_numbers)
    except:
        print "Invalid input"


largest = None
smallest = None

while True:
    num = user_prompt()
    if num is None:
        continue
    if num == 'done':
        break
    if smallest is None:
        smallest = num
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print "Maximum is", largest
print "Minimum is", smallest
