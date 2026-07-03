# Pizza Distribution Scenario

total_slices = int(input("Enter total pizza slices: "))
children = int(input("Enter number of children: "))

# Calculate remaining slices
remaining_slices = total_slices % children

# Display result
print("Remaining Slices =", remaining_slices)