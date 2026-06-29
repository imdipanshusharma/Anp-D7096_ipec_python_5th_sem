'''Multiplication Table Generator
 Problem Statement: Write a Python program that accepts a number from the user and displays its multiplication table up to 20.
---- Sample Output Enter Number: 8  8 x 1 = 8 8 x 2 = 16 ... 8 x 20 = 160'''

# WAP to Generate Multiplication Table up to 20

while True:
    try:
        # Accept a number from the user
        num = int(input("Enter Number: "))

        # Display multiplication table
        print("\nMultiplication Table of", num)

        for i in range(1, 21):
            print(num, "x", i, "=", num * i)

        # Exit the loop after successful execution
        break

    except ValueError:
        # Handle invalid input
        print("Invalid Input! Please enter an integer only.")
