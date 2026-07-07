"""--------------Problem Statement---------------------------------
Calculate electricity bill using: 
Units      |    Rate 
0-100      |   ₹5/unit 
101-300    |   ₹7/unit 
Above 300  |   ₹10/unit 
Additional Rules: 
• Commercial consumers pay 20% extra.  
• Bills above ₹5000 attract 5% surcharge.  
• Senior citizens receive 10% discount.
------------------------------------------------------------  
Sample Input: 
Units Consumed: 450 
Consumer Type (Residential/Commercial): Commercial 
Senior Citizen (Y/N): Y
-------------------------------------------------------------- 
Sample Output: 
Base Bill: ₹4500 
Commercial Charge: ₹900 
Surcharge: ₹270 
Senior Citizen Discount: ₹567 
Final Bill Amount: ₹5103
----------------------------------------------------------------
 """
#-------------------------Coding---------------------------------
# Smart Electricity Billing System
print("--------------------------------------------------------")
units = int(input("Enter Units Consumed: "))
consumer = input("Consumer Type (Residential/Commercial): ")
senior = input("Senior Citizen (Y/N): ")
print("---------------------------------------------------------")

# Validation
if units < 0:
    print("Invalid Input")

else:

    # Calculate Base Bill
    if units <= 100:
        bill = units * 5

    elif units <= 300:
        bill = units * 7

    else:
        bill = units * 10

    print("Base Bill: ₹", bill)

    # Commercial Charge
    commercial = 0

    if consumer == "Commercial" or consumer == "commercial":
        commercial = bill * 20 / 100
        bill = bill + commercial
        print("Commercial Charge: ₹", commercial)

    # Surcharge
    surcharge = 0

    if bill > 5000:
        surcharge = bill * 5 / 100
        bill = bill + surcharge
        print("Surcharge: ₹", surcharge)

    # Senior Citizen Discount
    discount = 0

    if senior == "Y" or senior == "y":
        discount = bill * 10 / 100
        bill = bill - discount
        print("Senior Citizen Discount: ₹", discount)

    print("Final Bill Amount: ₹", bill)
    print("------------------------------------------------------------")
