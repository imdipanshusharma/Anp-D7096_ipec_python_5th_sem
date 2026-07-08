#this is another file 

'''Create another Python file named 
-----operations.py----- 
that imports the twodfigures module and performs the following tasks:

1. Display a menu for selecting one the following figures:

▪square
▪rectangle
▪triangle 
▪circle


2. Based on the user's choice, ask for the required dimensions of the selected figure:
 
 Example: 
 ▪ Circle → Radius 
 ▪ Square → Side 
 ▪ Rectangle → Length and Breadth 
 ▪ Triangle → Three sides (for perimeter) and Base & Height (for area) 

 
 3. Display a second menu to choose the required operation:

 ▪Area 
 ▪Perimeter

 4. Call the appropriate function from the twodfigures module based on the user's selections. 
 
 
 5. Display the calculated result in a user-friendly format. 
 
 
 6. Allow the user to perform multiple calculations until they choose to exit the application'''

#-----------------coding----------------------------
# operations.py
# This program imports the twodfigures module
# and performs area and perimeter calculations.

# Import the user-defined module
import twodfigures

# Repeat until the user chooses Exit
while True:

    # Display Main Menu
    print("\n========== GEOMETRY CALCULATOR ==========")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    # Accept user's choice
    choice = int(input("Enter your choice: "))

    # Exit the program
    if choice == 5:
        print("Thank You for using Geometry Calculator!")
        break

    # Display Operation Menu
    print("\nChoose Operation")
    print("1. Area")
    print("2. Perimeter")

    operation = int(input("Enter your choice: "))

    # ---------------- Square ----------------
    if choice == 1:

        side = float(input("Enter side of square: "))

        if operation == 1:
            area = twodfigures.square_area(side)
            print("Area of Square =", area)

        elif operation == 2:
            perimeter = twodfigures.square_perimeter(side)
            print("Perimeter of Square =", perimeter)

        else:
            print("Invalid Operation!")

    # ---------------- Circle ----------------
    elif choice == 2:

        radius = float(input("Enter radius of circle: "))

        if operation == 1:
            area = twodfigures.circle_area(radius)
            print("Area of Circle =", round(area, 2))

        elif operation == 2:
            circumference = twodfigures.circle_perimeter(radius)
            print("Circumference of Circle =", round(circumference, 2))

        else:
            print("Invalid Operation!")

    # ---------------- Triangle ----------------
    elif choice == 3:

        if operation == 1:

            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            area = twodfigures.triangle_area(base, height)
            print("Area of Triangle =", area)

        elif operation == 2:

            side1 = float(input("Enter Side 1: "))
            side2 = float(input("Enter Side 2: "))
            side3 = float(input("Enter Side 3: "))

            perimeter = twodfigures.triangle_perimeter(side1, side2, side3)
            print("Perimeter of Triangle =", perimeter)

        else:
            print("Invalid Operation!")

    # ---------------- Rectangle ----------------
    elif choice == 4:

        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        if operation == 1:
            area = twodfigures.rectangle_area(length, breadth)
            print("Area of Rectangle =", area)

        elif operation == 2:
            perimeter = twodfigures.rectangle_perimeter(length, breadth)
            print("Perimeter of Rectangle =", perimeter)

        else:
            print("Invalid Operation!")

    # Invalid Main Menu Choice
    else:
        print("Invalid Choice! Please try again.")