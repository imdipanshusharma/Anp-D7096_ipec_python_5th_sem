"""Program to store names and marks of 50 students
and display eligible students (marks > 75)"""

names = []
marks = []

for i in range(10):
    name = input("Enter name of student  ")

    mark = int(input("Enter marks of "))

    # Validation
    if mark < 0 or mark > 100:
        print("Invalid marks! Setting marks to 0.")
        mark = 0

    names.append(name)
    marks.append(mark)

# Display eligible students
print("\n------ Eligible Students ------")

for i in range(10):
    if marks[i] > 75:
        print(names[i], "is eligible for admission with marks:", marks[i])