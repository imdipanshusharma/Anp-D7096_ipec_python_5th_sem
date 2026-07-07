
'''Problem Statement 4: Dictionary Search System Write 
a Python program that defines a function search_student
(student_dict, roll_no). The function should:
 • Accept a dictionary where: 
   o Key = Roll Number
       o Value = Student Name 
         • Search for the given roll number. 
          
            • Return the student name if found;
              otherwise return "Student Not Found".
                  The main program should: 
                  • Create a dictionary of at least 5 students. 
                    • Accept a roll number from the user. 
                      • Display the search result.  '''





'''---------------------------coding---------------------------'''















# Function to search a student by roll number
def search_student(student_dict, roll_no):

    # Check if the roll number exists in the dictionary
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"

# Main program

# Create a dictionary of students
students = {
    101: "Aman",
    102: "Riya",
    103: "Rahul",
    104: "Priya",
    105: "Neha"
}

# Take roll number as input from the user
roll_no = int(input("Enter Roll Number: "))

# Call the function
result = search_student(students, roll_no)

# Display the result
print("Search Result:", result)



'''---------------------------output---------------------------

Enter Roll Number: 103
Search Result: Rahul'''