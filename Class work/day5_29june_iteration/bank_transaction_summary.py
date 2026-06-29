''' Bank Transaction Summary 
Problem Statement: A customer keeps entering transaction amounts.
 Positive numbers indicate deposits, while negative numbers indicate withdrawals. 

 -----The customer enters 0 to finish Display:----
   • Total Deposit
   • Total Withdrawal  
   • Final Balance  '''



# Bank Transaction Summary Program

total_deposit = 0
total_withdrawal = 0
balance = 0

while True:
    amount = float(input("Enter transaction amount (0 to finish): "))

    if amount == 0:
        break
    elif amount > 0:
        total_deposit += amount
    else:
        total_withdrawal += abs(amount)

    balance += amount

print("\nTransaction Summary")
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", balance)