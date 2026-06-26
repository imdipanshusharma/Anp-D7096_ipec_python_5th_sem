''' Electricity Bill Discount
Problem Statement: An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 or more. Otherwise,
---------- no discount is applied------------
----- Write a Python program to accept the total bill amount from the user and display the final amount to be paid-----------

------ Sample Input 1 Enter the electricity bill amount: 6200-----
------ Sample Output 1 Discount Applied! Final Bill Amount: ₹5580.0-----


------ Sample Input 2 Enter the electricity bill amount: 4200------
------ Sample Output 2 No Discount Applied! Final Bill Amount: ₹4200'''

#--------coding--------------------------
#input of electricty bill amount from user
# Electricity Bill Discount Program

bill = float(input("Enter the electricity bill amount: "))

if bill >= 5000:
    final_bill = bill - (bill * 0.10)
    print("Discount Applied!")
    print("Final Bill Amount: ₹", final_bill)
else:
    print("No Discount Applied!")
    print("Final Bill Amount: ₹", bill)

'''-----Enter the electricity bill amount: 6200---
-----Discount Applied!------
-------Final Bill Amount: ₹ 5580.0------

-------Enter the electricity bill amount: 4200-------
-------No Discount Applied!--------
-------Final Bill Amount: ₹ 4200.0-------'''



