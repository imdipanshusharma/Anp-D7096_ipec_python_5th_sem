# Create an empty tuple
t = ()

# Take 15 numbers as input from the user
for i in range(15):
    num = int(input("Enter Number: "))

    # Add each number to the tuple
    t = t + (num,)

# Display the complete tuple
print("Tuple =", t)

# Display the odd numbers present in the tuple
print("Odd Numbers are:")

# Traverse each element of the tuple
for i in t:

    # Check whether the number is odd
    if i % 2 != 0:

        # Print the odd number
        print(i)