

'''Problem Statement 3: Password Strength Checker Write a
 function check_password(password) that checks whether a
   password is strong. A password is considered Strong if: 
   • It contains at least 8 characters.  
   • It contains at least one uppercase letter. 
     • It contains at least one lowercase letter. 
       • It contains at least one digit. 
         The function should return: 
         • "Strong Password" or  
         • "Weak Password"  
         The main program should accept a password from the user and display the result. '''


'''---------------------------coding---------------------------'''






# Function to check password strength
def check_password(password):

    # Check if password has at least 8 characters
    if len(password) < 8:
        return "Weak Password"

    # Initialize flags
    has_upper = False
    has_lower = False
    has_digit = False

    # Check each character in the password
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    # Check all conditions
    if has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"

# Main program

# Take password as input from the user
password = input("Enter your password: ")

# Call the function
result = check_password(password)

# Display the result
print(result)


'''---------------------------output---------------------------
Enter your password: python789#Q
Strong Password'''