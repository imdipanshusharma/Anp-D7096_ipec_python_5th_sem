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

'''Enter Number: 25
Enter Number: 52
Enter Number: 25
Enter Number: 25
Enter Number: 25
Enter Number: 05
Enter Number: 25
Enter Number: 65
Enter Number: 68
Enter Number: 582
Enter Number: 55
Enter Number: 6
Enter Number: 55
Enter Number: 55456
Enter Number: 35
Tuple = (25, 52, 25, 25, 25, 5, 25, 65, 68, 582, 55, 6, 55, 55456, 35)
Odd Numbers are:
25
25
25
25
5
25
65
55
55
35'''