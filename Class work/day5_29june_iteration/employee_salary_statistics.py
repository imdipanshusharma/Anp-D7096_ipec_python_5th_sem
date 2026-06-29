'''Employee Salary Statistics 

Problem Statement: A company has N employees. Accept the salary of each employee and determine: 
• Highest salary 
• Lowest salary 
• Average salar
• Number of employees earning more than ₹50,000  '''

# Accept the number of employees
n = int(input("Enter Number of Employees: "))

# Read the first employee's salary
salary = int(input("Enter Salary: "))
highest = salary
lowest = salary
total = salary

# Count employees earning more than ₹50,000
count = 0
if salary > 50000:
    count += 1

# Read salaries of remaining employees
for i in range(2, n + 1):
    salary = int(input("Enter Salary: "))
    total += salary

    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

    if salary > 50000:
        count += 1

# Calculate average salary
average = total / n

# Display results
print("Highest Salary =", highest)
print("Lowest Salary =", lowest)
print("Average Salary =", average)
print("Employees Earning More Than ₹50,000 =", count)