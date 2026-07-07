'''Write a Python program that defines a function calculate_grade(marks). 
The function should: 
* Accept marks (0-100) as a parameter.  
* Return the grade according to the following criteria:  
o 90 and above → A+  
o 75-89 → A  
o 60-74 → B  
o 40-59 → C  
o Below 40 → Fail'''

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# Main Program
for i in range(1, 6):
    marks = float(input(f"Enter marks of Student {i} (0-100): "))

    # Validate input
    while marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")
        marks = float(input(f"Enter marks of Student {i} (0-100): "))

    grade = calculate_grade(marks)

    print(f"Student {i}: Marks = {marks}, Grade = {grade}")

'''output'''
'''Enter marks of Student 1 (0-100): 5
Student 1: Marks = 5.0, Grade = Fail
Enter marks of Student 2 (0-100): 36 
Student 2: Marks = 36.0, Grade = Fail
Enter marks of Student 3 (0-100): 52
Student 3: Marks = 52.0, Grade = C
Enter marks of Student 4 (0-100): 36
Student 4: Marks = 36.0, Grade = Fail
Enter marks of Student 5 (0-100): 85
Student 5: Marks = 85.0, Grade = A'''