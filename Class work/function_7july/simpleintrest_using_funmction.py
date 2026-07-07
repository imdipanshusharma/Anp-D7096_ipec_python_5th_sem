#function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

#main program
principal = float(input("Enter the principal (in rs): "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

#calculate simple interest
print("Simple Interest :rs", calculate_simple_interest(principal, rate, time))