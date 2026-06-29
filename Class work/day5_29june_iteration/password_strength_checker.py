'''Password Strength Checker
 Problem Statement: A website requires users to create a password having at least 8 characters.
 Keep asking the user to enter a password until the entered password satisfies the minimum length requirement.

-------Sample Output Enter Password: hello Password too short-------
 Enter Password: python@123 Password Accepted'''

# WAP to Check Password Strength

while True:
    # Accept password from the user
    password = input("Enter Password: ")

    # Check the length of the password
    if len(password) >= 8:
        print("Password Accepted.")
        break      # Exit the loop
    else:
        print("Password too short.")