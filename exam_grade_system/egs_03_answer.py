#Create the initial lists
students = ["Bill","Ben","Katie","Sam","Jane"]
finalExamGrades = [0]*len(students)


#input the final grades
'''
TASK 2: Type Check
Add a type check so that the user must enter a value between 0 and 100
'''
for i in students:
    print("Enter the final grade for",i)
    while True:
        try:
            grade = int(input())
            while grade < 0 or grade > 100:
                    print("You must enter a value between 0 and 100. Try again:")
                    grade = int(input())
            finalExamGrades[students.index(i)] = grade
            break
        except:
            print("You must enter a whole number")


#output the final results:
print()
for i in students:
    print(i, "scored",finalExamGrades[students.index(i)])