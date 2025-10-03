"""
Python Basics - Loops
This file demonstrates different types of loops in Python and how they work.
Loops allow you to repeat code multiple times efficiently.
"""

print("=== Python Loops Tutorial ===\n")

# =============================================================================
# FOR LOOPS
# =============================================================================
print("1. FOR LOOPS")
print("-" * 20)

# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(1, 6) gives 1, 2, 3, 4, 5
    print(f"  Count: {i}")

print("\nCounting backwards from 5 to 1:")
for i in range(5, 0, -1):  # range(5, 0, -1) gives 5, 4, 3, 2, 1
    print(f"  Count: {i}")

# For loop with a list
print("\nIterating through a list of fruits:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"  I like {fruit}")

# For loop with enumerate (gets both index and value)
print("\nFruits with their positions:")
for index, fruit in enumerate(fruits):
    print(f"  {index + 1}. {fruit}")

# For loop with string
print("\nIterating through characters in a word:")
word = "Python"
for char in word:
    print(f"  Character: {char}")

# =============================================================================
# WHILE LOOPS
# =============================================================================
print("\n\n2. WHILE LOOPS")
print("-" * 20)

# Basic while loop
print("Counting from 1 to 5 using while loop:")
count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1  # Important: increment the counter!

# While loop with user input simulation
print("\nSimulating a simple counter (stops at 3):")
counter = 0
while counter < 3:
    print(f"  Counter is at: {counter}")
    counter += 1
print("  Loop finished!")

# =============================================================================
# NESTED LOOPS
# =============================================================================
print("\n\n3. NESTED LOOPS")
print("-" * 20)

print("Multiplication table (2x2):")
for i in range(1, 3):  # Outer loop
    for j in range(1, 3):  # Inner loop
        result = i * j
        print(f"  {i} x {j} = {result}")
    print()  # Empty line after each row

# =============================================================================
# LOOP CONTROL STATEMENTS
# =============================================================================
print("\n4. LOOP CONTROL STATEMENTS")
print("-" * 20)

# BREAK statement - exits the loop completely
print("Using BREAK to stop at 3:")
for i in range(1, 6):
    if i == 3:
        print(f"  Found {i}! Breaking out of loop.")
        break
    print(f"  Current number: {i}")

# CONTINUE statement - skips current iteration
print("\nUsing CONTINUE to skip even numbers:")
for i in range(1, 6):
    if i % 2 == 0:  # If number is even
        print(f"  Skipping even number: {i}")
        continue
    print(f"  Odd number: {i}")

# =============================================================================
# ELSE CLAUSE WITH LOOPS
# =============================================================================
print("\n\n5. ELSE CLAUSE WITH LOOPS")
print("-" * 20)

# Else with for loop
print("For loop with else (runs when loop completes normally):")
for i in range(1, 4):
    print(f"  Processing: {i}")
else:
    print("  Loop completed successfully!")

# Else with while loop
print("\nWhile loop with else:")
num = 1
while num <= 3:
    print(f"  Number: {num}")
    num += 1
else:
    print("  While loop finished normally!")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n\n6. PRACTICAL EXAMPLES")
print("-" * 20)

# Example 1: Finding the sum of numbers
print("Finding sum of numbers 1 to 5:")
total = 0
for num in range(1, 6):
    total += num
    print(f"  Adding {num}, total so far: {total}")
print(f"Final sum: {total}")

# Example 2: Finding the largest number in a list
print("\nFinding the largest number:")
numbers = [3, 7, 2, 9, 1, 5]
largest = numbers[0]  # Start with first number
for num in numbers:
    if num > largest:
        largest = num
    print(f"  Checking {num}, largest so far: {largest}")
print(f"Largest number: {largest}")

# Example 3: Building a pattern
print("\nBuilding a pattern with loops:")
for i in range(1, 5):
    stars = "*" * i  # Create string with i asterisks
    print(f"  {stars}")

# =============================================================================
# COMMON LOOP PATTERNS
# =============================================================================
print("\n\n7. COMMON LOOP PATTERNS")
print("-" * 20)

# Pattern 1: Loop until condition is met
print("Loop until we find a specific value:")
target = 7
numbers = [1, 3, 5, 7, 9, 11]
found = False
for num in numbers:
    print(f"  Checking: {num}")
    if num == target:
        print(f"  Found target {target}!")
        found = True
        break

if not found:
    print(f"  Target {target} not found!")

# Pattern 2: Accumulator pattern
print("\nAccumulator pattern - counting items:")
items = ["apple", "banana", "apple", "orange", "apple"]
apple_count = 0
for item in items:
    if item == "apple":
        apple_count += 1
print(f"Found {apple_count} apples in the list")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n9. KEY CONCEPTS SUMMARY")
print("-" * 20)
print("✓ FOR loops: Use when you know how many times to repeat")
print("✓ WHILE loops: Use when you want to repeat until a condition is met")
print("✓ BREAK: Exit the loop immediately")
print("✓ CONTINUE: Skip to the next iteration")
print("✓ ELSE: Runs when loop completes normally (not with break)")
print("✓ NESTED loops: Loops inside other loops")
print("✓ range(): Creates a sequence of numbers for for loops")
print("✓ enumerate(): Gets both index and value when iterating")
print("\nLoops are powerful tools for making your code efficient and repetitive! 🚀")
