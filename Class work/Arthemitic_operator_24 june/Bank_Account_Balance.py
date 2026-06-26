# Input from user
#input

current_balance = float(input("Enter current balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

# Calculate remaining balance
remaining_balance = current_balance - withdrawal_amount

# Display result
print("Remaining Balance =", remaining_balance)