'''Electricity Bill Analysis 
Problem Statement: An electricity department wants to analyze electricity consumption of N houses.
 Accept the monthly units consumed by each house.

------ Calculate and display:------
 • Total units consumed  
 • Average units consumed  
 • Highest consumption 
 • Lowest consumption'''

# Accept the number of houses
n = int(input("Enter Number of Houses: "))

# Read units consumed by the first house
units = int(input("Enter Units Consumed: "))
total = units
highest = units
lowest = units

# Read units for remaining houses
for i in range(2, n + 1):
    units = int(input("Enter Units Consumed: "))
    total += units

    if units > highest:
        highest = units

    if units < lowest:
        lowest = units

# Calculate average
average = total / n

# Display results
print("Total Units Consumed =", total)
print("Average Units Consumed =", average)
print("Highest Consumption =", highest)
print("Lowest Consumption =", lowest)