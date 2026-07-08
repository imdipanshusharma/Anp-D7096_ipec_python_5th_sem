#function to calculate the addition of two numbers
def calculate_addition(num1, num2):
    return  (num1 + num2)

    #---------------------------------


#function to calculate the subtraction of two numbers
def calculate_subtraction(num1, num2):
    return  (num1 - num2)

    #---------------------------------

#function to calculate the multiplication of two numbers
def calculate_multiplication(num1, num2):
    return  (num1 * num2)

    #---------------------------------

#function to calculate the division of two numbers
def calculate_division(num1, num2):
    if num2 != 0:
        return  (num1 / num2)
    else:
        return "Error: Division by zero is not allowed."

