 #Program to count eligible voters using for loop with validation

ages = []

# Taking input for 10 people
for i in range(10):
    age = int(input(f"Enter age of person {i+1}: "))

    # Validation using for loop logic
    if age < 0:
        print("Invalid age! Setting it to 0.")
        age = 0

    ages.append(age)

# Counting eligible voters using for loop
count = 0
for age in ages:
    if age >= 18:
        count += 1

# Displaying results
print("\n------ Result ------")
print("List of Ages:", ages)
print("Total Eligible for Voting:", count)