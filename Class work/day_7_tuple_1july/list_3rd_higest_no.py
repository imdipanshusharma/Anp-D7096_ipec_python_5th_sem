numbers = []

print("Enter 20 numbers:")
for i in range(20):
    numbers.append(int(input(f"Number {i+1}: ")))

first = second = third = float('-inf')

for num in numbers:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != second:
        third = num

print("3rd largest number is:", third)