# create an empty list
numbers = []
# Input elements into the list
for i in range(10):
    #input of element from user 
    num = int(input("Enter element : "))
    #inserting data in list by 
    numbers.append(num)

x=int(input("Enter index of the element to remove :"))
numbers.pop(x)
print(numbers)
""""""

'''
Enter element : 25
Enter element : 36
Enter element : 85
Enter element : 75
Enter element : 13
Enter element : 65
Enter element : 85
Enter element : 78
Enter element : 55
Enter element : 25
Enter index of the element to remove :2
[25, 36, 75, 13, 65, 85, 78, 55, 25]'''
