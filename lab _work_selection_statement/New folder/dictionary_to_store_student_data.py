"""
-------------------------------------------Problem Statement---------------------------------------------------
Create a dictionary to store the marks of 5 students, where the key is the student's name and the 
value is their marks. 
Perform the following operations: 
* Display all student names and marks.  
* Add a new student with marks.  
* Update the marks of an existing student.  
* Delete a student by name.  
* Display the student who scored the highest marks.
  """
# Dictionary to store marks of 5 students
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Emma": 78
}

# 1. Display all student names and marks
def display_students():
    print("\n--- Student Marks ---")
    for name, marks in students.items():
        print(f"{name}: {marks}")

# 2. Add a new student with marks
def add_student(name, marks):
    if name in students:
        print(f"{name} already exists. Use update instead.")
    else:
        students[name] = marks
        print(f"{name} added with marks {marks}.")

# 3. Update marks of an existing student
def update_marks(name, new_marks):
    if name in students:
        students[name] = new_marks
        print(f"{name}'s marks updated to {new_marks}.")
    else:
        print(f"{name} not found.")

# 4. Delete a student by name
def delete_student(name):
    if name in students:
        del students[name]
        print(f"{name} deleted from records.")
    else:
        print(f"{name} not found.")

# 5. Display the student with highest marks
def highest_scorer():
    if students:
        top_student = max(students, key=students.get)
        print(f"Highest scorer: {top_student} with {students[top_student]} marks.")
    else:
        print("No students in the record.")

# ----------- Demonstration -----------
display_students()

add_student("Farhan", 88)
display_students()

update_marks("Bob", 95)
display_students()

delete_student("David")
display_students()

highest_scorer()