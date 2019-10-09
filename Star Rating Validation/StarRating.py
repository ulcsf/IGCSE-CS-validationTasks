'''
Star Rating Validation - www.101computing.net/flowchart-to-python-code-star-rating-validation/

The aim of this Python challenge is to validate a user input using a range check.

In this program, the user will be asked to enter a star rating by entering a number value between 0 and 5.
This could for instance be used to rate a movie (5 Stars = Excellent , 0 Star = Disappointing).

The program will check that the end-user has entered a number between 0 and 5 and if not, it will display
an error message and repeat the question until a valid rating between 0 and 5 is entered

'''

starRating = int(input("Enter a star rating between 0 and 5: "))

while starRating < 0 or starRating > 5:
  print("Invalid star rating - try again!")
  starRating = int(input("Enter a star rating between 0 and 5: "))
print("Thank you!")
