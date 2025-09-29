"""
Python Basics - Control Flow
This file demonstrates if-else statements, loops, and other control structures.
"""

# If-Else Statements
print("=== If-Else Statements ===")

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-Elif-Else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Nested If statements
weather = "sunny"
temperature = 25

if weather == "sunny":
    if temperature > 30:
        print("Hot sunny day!")
    else:
        print("Nice sunny day!")
else:
    print("Not a sunny day")

# For Loops
print("\\n=== For Loops ===")

# Loop through a range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Loop through a list
fruits = ["apple", "banana", "orange"]
print("\\nFruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with enumerate
print("\\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# While Loops
print("\\n=== While Loops ===")

counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# Break and Continue
print("\\n=== Break and Continue ===")

# Break example
for num in range(1, 11):
    if num == 6:
        break
    print(num)

print("Loop ended with break at 6")

# Continue example
print("\\nSkipping even numbers:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# Nesting loops
print("\\n=== Nested Loops ===")
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")
    print("---")

# Pass statement (placeholder)
print("\\n=== Pass Statement ===")
for num in range(1, 6):
    if num == 3:
        pass  # Do nothing, placeholder for future code
    else:
        print(num)
