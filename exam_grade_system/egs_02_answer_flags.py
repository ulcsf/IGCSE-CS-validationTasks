#Create the initial lists
students = ["Bill","Ben","Katie","Sam","Jane"]
finalExamGrades = [0]*len(students)

#input the final grades
'''
TASK 1: Presence Check
Ensure that a grade must be entered, even if it is 0.
If the user tries to press return without entering a value they should be asked to try again
'''
for i in students:
    validInput = False
    print("Enter the final grade for",i)
    while not validInput:
        grade = input()
        if grade == "":
            print("You must enter a value")
        else:
            finalExamGrades[students.index(i)] = grade
            validInput = True

#output the final results:
print()
for i in students:
    print(i, "scored",finalExamGrades[students.index(i)])