'''function to calculate simple interest'''
def simple_interest(p, r, t):
    return (p * r * t) / 100

#main program
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

interest = simple_interest(principal, rate, time)
print(f"The simple interest is: {interest}")