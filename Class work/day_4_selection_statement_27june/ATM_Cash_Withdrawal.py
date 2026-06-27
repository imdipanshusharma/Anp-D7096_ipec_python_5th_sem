"""
Problem Statement 
A customer can withdraw money only if the requested amount does not exceed the available balance. 
Accept the account balance and withdrawal amount. 
• If withdrawal amount is less than or equal to balance, display: 
Transaction Successful 
• Otherwise display: 
Insufficient Balance 
-----------------------------------------------------
Sample Input 
5000 
4500 
---------------------------------------------------------
Sample Output 
Transaction Successful 
"""
#--------------------------Coding section------------------------------
# ATM Cash Withdrawal
print("--------------------------------------------------------")
balance = float(input("Enter account balance: ₹"))
#---------------------Chacking validation of balance--------------------
if balance<0:
    exit("Balance must be positive number")
withdraw = float(input("Enter withdrawal amount: ₹"))
#--------------------Chacking validation of withdraw-----------------------------
if  withdraw<0:
    exit("withdrawal must be positive number")
#--------------------Chacking condition--------------------------------
if withdraw <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")

print("--------------------------------------------------------")
#-------------------------------------------------------------------
"""
Output:
--------------------------------------------------------
Enter account balance: ₹5000000
Enter withdrawal amount: ₹6000
Transaction Successful
---------------------------------------------------------
"""