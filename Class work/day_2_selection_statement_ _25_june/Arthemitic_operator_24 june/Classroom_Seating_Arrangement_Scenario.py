# Input from user
#update

total_students = int(input("Enter total number of students: "))
students_per_row = int(input("Enter number of students per row: "))

# Calculate complete rows
complete_rows = total_students // students_per_row

# Display result
print("Number of Complete Rows =", complete_rows)