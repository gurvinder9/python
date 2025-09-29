"""
Python Basics - Input and Output
This file demonstrates how to get input from users and display output.
"""

# Basic output
print("Hello World!")
print("This is a Python program")

# Formatted output
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

# Multiple values
print("Python", "is", "awesome", sep="-")  # Python-is-awesome

# Getting input from user
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print(f"Hello {user_name}! You are {user_age} years old.")

# Converting input to different types
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
    print(f"Twice your number: {number * 2}")
except ValueError:
    print("Please enter a valid number!")

# Reading multiple inputs
print("Enter two numbers:")
try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    sum_result = num1 + num2
    product = num1 * num2

    print(f"Sum: {sum_result}")
    print(f"Product: {product}")
except ValueError:
    print("Please enter valid numbers!")
