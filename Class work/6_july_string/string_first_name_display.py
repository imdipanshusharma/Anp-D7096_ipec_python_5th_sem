'''write a program to ask user to input his full name and display only first name without using any library function.'''

# without using any library function

# Take full name as input from the user
name = input("Enter your full name: ")

# Initialize an empty string to store the first name
first_name = ""

# Traverse each character of the name
for ch in name:

    # Stop when a space is encountered
    if ch == " ":
        break

    # Add the character to first_name
    first_name += ch

# Display the first name
print("First Name =", first_name)