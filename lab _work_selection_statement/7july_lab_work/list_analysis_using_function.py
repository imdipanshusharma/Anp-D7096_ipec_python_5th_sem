'''Problem Statement 2: List Analysis using Functions Write a Python
 program that defines the following functions:
   • find_max(numbers) 
     • find_min(numbers)
         • find_average(numbers) 
           The program should:
             • Accept a list of 10 integers from the user. 
               • Call all three functions. 
                 • Display the maximum value, 
                 minimum value, and average of the list.  '''




'''---------------------------coding---------------------------'''






# Function to find the maximum number in the list
def find_max(numbers):
    return max(numbers)

# Function to find the minimum number in the list
def find_min(numbers):
    return min(numbers)

# Function to calculate the average of the list
def find_average(numbers):
    return sum(numbers) / len(numbers)

# Main program

# Create an empty list
numbers = []

# Take 10 integer inputs from the user
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

# Call the functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display the results
print("\nList:", numbers)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Average:", average)



'''---------------------------output---------------------------Enter integer 1: 10
Enter integer 2: 20
Enter integer 3: 85
Enter integer 4: 55
Enter integer 5: 95
Enter integer 6: 85
Enter integer 7: 75
Enter integer 8: 95
Enter integer 9: 62
Enter integer 10: 12

List: [10, 20, 85, 55, 95, 85, 75, 95, 62, 12]
Maximum Value: 95
Minimum Value: 10
Average: 59.4'''