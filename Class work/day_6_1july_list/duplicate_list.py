'''create a list of 20 numbers given by the user 
ask the user to enter any two numbers if both numbers are present in the list remove all duplicate values from the list'''


# WAP to create a list of 20 numbers given by the user.
# Ask the user to enter any two numbers.
# If both numbers are present in the list,
# remove all duplicate values from the list.

# Create an empty list
num = []

# Input 20 numbers
for i in range(20):
    n = int(input("Enter a number: "))
    num.append(n)

# Display the original list
print("\nOriginal List:", num)

# Input any two numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Check whether both numbers are present in the list
if n1 in num and n2 in num:

    # Create a new list to store unique elements
    unique = []

    # Remove duplicate values
    for i in num:
        if i not in unique:
            unique.append(i)

    print("\nList after removing duplicate values:")
    print(unique)

else:
    print("\nOne or both numbers are not present in the list.")