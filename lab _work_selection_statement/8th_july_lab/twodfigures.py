#Problem Statement: Geometry Calculator Using Python Module 

'''Develop a menu-driven Python application that demonstrates the use of User-Defined Modules and Functions''' 


'''Requirements You are required to create a Python module named  
-----twodfigures.py-----

 that contains functions to perform the following calculations for different two-dimensional shapes:


• Triangle 
Calculate Area 
Calculate Perimeter
 
• Circle 
 Calculate Area 
 Calculate Circumference (Perimeter) 
 
 • Square 
Calculate Area 
Calculate Perimeter 

• Rectangle 
 Calculate Area 
 Calculate Perimeter '''

# twodfigures.py


# This module contains functions for calculating
# area and perimeter of different 2D figures.

import math

# ------------------ Square ------------------

# Function to calculate area of a square
def square_area(side):
    return side * side

# Function to calculate perimeter of a square
def square_perimeter(side):
    return 4 * side


# ------------------ Circle ------------------

# Function to calculate area of a circle
def circle_area(radius):
    return math.pi * radius * radius

# Function to calculate circumference of a circle
def circle_perimeter(radius):
    return 2 * math.pi * radius


# ---------------- Rectangle -----------------

# Function to calculate area of a rectangle
def rectangle_area(length, breadth):
    return length * breadth

# Function to calculate perimeter of a rectangle
def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


# ---------------- Triangle ------------------

# Function to calculate area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Function to calculate perimeter of a triangle
def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3