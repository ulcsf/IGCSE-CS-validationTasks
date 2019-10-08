#Create the initial lists
students = ["Bill","Ben","Katie","Sam","Jane"]
finalExamGrades = [0]*len(students)

#input the final grades
for i in students:
    print("Enter the final grade for",i)
    grade = input()
    finalExamGrades[students.index(i)] = grade

#output the final results:
print()
for i in students:
    print(i, "scored",finalExamGrades[students.index(i)])