#  3.3 Write a program to prompt for a score between 0.0 and 1.0.
#  If the score is out of range, print an error.
#  If the score is between 0.0 and 1.0,
#  print a grade using the following table:
#
#  Score Grade
#  >= 0.9 A
#  >= 0.8 B
#  >= 0.7 C
#  >= 0.6 D
#  < 0.6 F
#
#  If the user enters a value out of range,
#  print a suitable error message and exit
#  For the test, enter a score of 0.85.


def get_score():
    try:
        score = float(raw_input("Please Enter Score between 0.0 and 1.0: "))
    except:
        print "ERROR: Non numerical data."
        print "Please Enter Score between 0.0 and 1.0."
        quit()
    return score


def grade(score):
        if 0.9 <= score <= 1.0:
            grade = "A"
        elif 0.8 <= score < 0.9:
            grade = "B"
        elif 0.7 <= score < 0.8:
            grade = "C"
        elif 0.6 <= score < 0.7:
            grade = "D"
        elif 0.0 <= score < 0.6:
            grade = "F"
        try:
            return grade
        except:
            print "ERROR, Out of RANGE."
            print "Please Enter Score between 0.0 and 1.0."
            quit()

score = get_score()
grade = grade(score)
print grade
