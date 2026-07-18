'''Problem 2: Bank Account System 
Problem Statement Create a simple Bank Account class that allows users to deposit and withdraw money

Requirements 
1. Create a class BankAccount.  

2. Define the following instance variables:  
account_number   
customer_name  
balance  

3. Create the following methods:  
accept_details() – Accept account details from the user.   
deposit(amount) – Add the amount to the balance.  
withdraw(amount) – Deduct the amount if sufficient balance is available; 
otherwise display "Insufficient Balance".  
display_balance() – Display account details and current balance.  

4. Create an object of the class.  

5. Accept a deposit amount and a withdrawal amount from the user and perform both operations.  

Sample Input 
Enter Account Number : 1001 
Enter Customer Name : Anjali 
Enter Initial Balance : 5000  
Enter Deposit Amount : 2000 
Enter Withdrawal Amount : 4500 

Expected Output 
Deposit Successful.  
Withdrawal Successful.  

------ Account Details ------ 
Account Number : 1001 
Customer Name  : Anjali 
Current Balance: 2500 

Sample Output (Insufficient Balance) 
Enter Withdrawal Amount : 9000  
Insufficient Balance. 
------ Account Details ------ 
Account Number : 1001 
Customer Name  : Anjali 
Current Balance: 7000'''

#--------------------------------coding-----------------------------------
class BankAccount:

    def __init__(self):
        self.account_number = 0
        self.customer_name = ""
        self.balance = 0

    def accept_details(self):
        self.account_number = int(input("Enter Account Number: "))
        self.customer_name = input("Enter Customer Name: ")
        self.balance = int(input("Enter Initial Balance: "))

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    def display_balance(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Customer Name :", self.customer_name)
        print("Current Balance :", self.balance)


# Object creation
b1 = BankAccount()

b1.accept_details()

deposit_amount = int(input("Enter Deposit Amount: "))
b1.deposit(deposit_amount)

withdraw_amount = int(input("Enter Withdrawal Amount: "))
b1.withdraw(withdraw_amount)

b1.display_balance()