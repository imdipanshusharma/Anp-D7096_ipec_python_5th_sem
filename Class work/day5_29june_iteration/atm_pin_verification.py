'''Problem Statement: An ATM allows a user to enter the correct PIN. The correct PIN is 4589.
 The user can keep entering the PIN until it matches the correct one.
 Display "Access Granted" when the correct PIN is entered.

 -------Sample Output Enter PIN: 1234 Incorrect PIN-------- 
Enter PIN: 9876 Incorrect PIN  Enter PIN: 4589 Access Granted '''

# Store the correct PIN
correct_pin = 4589

while True:
    try:
        # Accept PIN from the user
        pin = int(input("Enter PIN: "))

        # Check if the entered PIN is correct
        if pin == correct_pin:
            print("Access Granted")
            break   # Exit the loop
        else:
            print("Incorrect PIN")

    except ValueError:
        # Handle invalid input
        print("Invalid Input! Please enter a 4-digit numeric PIN.")