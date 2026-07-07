"""-----------------------Problem Statement---------------------------- 
A government tax portal calculates tax based on the following conditions: 
• Income up to ₹5,00,000 → No tax  
• ₹5,00,001 to ₹10,00,000 → 10%  
• ₹10,00,001 to ₹20,00,000 → 20%  
• Above ₹20,00,000 → 30%  
Additional Benefits: 
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
• Women taxpayers receive an additional 2% rebate on tax.  
Write a Python program to calculate the final tax amount payable.
------------------------------------------------------------------- 
Sample Input 
Enter Annual Income: 1200000 
Enter Age: 65 
Enter Gender (M/F): F 
Sample Output 
Tax before rebate: ₹240000.0 
Senior Citizen Rebate: ₹12000.0 
Women Rebate: ₹4800.0 
Final Tax Payable: ₹223200.0
-------------------------------------------------------------------
 """
# Smart Income Tax Calculator
print ("--------------------------------------------")
income = float(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ").upper()
print ("--------------------------------------------")

# Input Validation
if income < 0:
    print ("--------------------------------------------")
    print("Error: Income cannot be negative.")
    print ("--------------------------------------------")
elif age < 0:
    print ("--------------------------------------------")
    print("Error: Age cannot be negative.")
    print ("--------------------------------------------")
elif gender !="M" and gender !="F":
    print ("--------------------------------------------")
    print("Error: Enter Gender as M or F.")
    print ("--------------------------------------------")
else:
    # Calculate Tax
    if income <= 500000:
        tax = 0
    elif income <= 1000000:
        tax = income * 0.10
    elif income <= 2000000:
        tax = income * 0.20
    else:
        tax = income * 0.30
        print ("--------------------------------------------")

    print("Tax before rebate: ₹", tax)
    print ("--------------------------------------------")

    # Senior Citizen Rebate
    senior_rebate = 0
    if age >= 60:
        senior_rebate = tax * 0.05
        print ("--------------------------------------------")
        print("Senior Citizen Rebate: ₹", senior_rebate)
        print ("--------------------------------------------")

    # Women Rebate
    women_rebate = 0
    if gender == "F":
        women_rebate = tax * 0.02
        print ("--------------------------------------------")
        print("Women Rebate: ₹", women_rebate)
        print ("--------------------------------------------")

    # Final Tax
    final_tax = tax - senior_rebate - women_rebate
    print ("--------------------------------------------")

    print("Final Tax Payable: ₹", final_tax)
    print ("--------------------------------------------")
"""Output :
--------------------------------------------
Enter Annual Income: 12000000000         
Enter Age: 65
Enter Gender (M/F): f
--------------------------------------------
--------------------------------------------
Tax before rebate: ₹ 3600000000.0
--------------------------------------------
--------------------------------------------
Senior Citizen Rebate: ₹ 180000000.0
--------------------------------------------
--------------------------------------------
Women Rebate: ₹ 72000000.0
--------------------------------------------
--------------------------------------------
Final Tax Payable: ₹ 3348000000.0
--------------------------------------------
"""