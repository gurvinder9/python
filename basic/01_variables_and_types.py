"""
Python Basics - Variables and Data Types
This file covers fundamental concepts of Python variables and data types.
"""

# Variables
name = "John"  # String
age = 25  # Integer
height = 5.9  # Float
is_student = True  # Boolean

# Display variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Type checking
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# Variable assignment
x = 10
y = x  # Both x and y refer to the same value
print(f"x = {x}, y = {y}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Constants (convention: uppercase)
PI = 3.14159
MAX_SIZE = 100
