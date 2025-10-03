"""
Python Basics - Tuples
This file demonstrates how tuples work in Python.
Tuples are immutable sequences that are useful for fixed data and multiple return values.
"""

print("=== Python Tuples Tutorial ===\n")

# =============================================================================
# WHAT ARE TUPLES?
# =============================================================================
print("1. WHAT ARE TUPLES?")
print("-" * 20)

print(
    "Tuples are ordered collections of items, similar to lists, but with key differences:"
)
print("• Tuples are IMMUTABLE (cannot be changed after creation)")
print("• Tuples are created with parentheses () instead of square brackets []")
print("• Tuples can contain different data types")
print("• Tuples are faster than lists for certain operations")
print("• Tuples can be used as dictionary keys (unlike lists)")
print("• Tuples are commonly used for fixed data and multiple return values\n")

# =============================================================================
# CREATING TUPLES
# =============================================================================
print("2. CREATING TUPLES")
print("-" * 20)

# Method 1: Using parentheses
print("Method 1: Using parentheses")
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# Method 2: Using tuple() constructor
print("\nMethod 2: Using tuple() constructor")
numbers = tuple([1, 2, 3, 4, 5])
print(f"Numbers: {numbers}")

# Method 3: Single element tuple (note the comma!)
print("\nMethod 3: Single element tuple (note the comma!)")
single_element = (42,)  # Comma is required!
print(f"Single element: {single_element}")
print(f"Type: {type(single_element)}")

# Without comma (not a tuple)
not_tuple = 42
print(f"Without comma: {not_tuple}")
print(f"Type: {type(not_tuple)}")

# Method 4: Empty tuple
print("\nMethod 4: Empty tuple")
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Method 5: Tuple with different data types
print("\nMethod 5: Tuple with mixed data types")
mixed_tuple = ("Alice", 25, 5.6, True)
print(f"Mixed tuple: {mixed_tuple}")

# Method 6: Tuple from string
print("\nMethod 6: Tuple from string")
word_tuple = tuple("Python")
print(f"Word as tuple: {word_tuple}")

# =============================================================================
# ACCESSING TUPLE ELEMENTS
# =============================================================================
print("\n\n3. ACCESSING TUPLE ELEMENTS")
print("-" * 30)

# Accessing elements by index
print("Accessing elements by index:")
student = ("Alice", 20, "Computer Science", 3.8)
print(f"Student tuple: {student}")
print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Major: {student[2]}")
print(f"GPA: {student[3]}")

# Negative indexing
print("\nNegative indexing:")
print(f"Last element: {student[-1]}")
print(f"Second to last: {student[-2]}")

# Slicing tuples
print("\nSlicing tuples:")
print(f"First two elements: {student[:2]}")
print(f"Last two elements: {student[2:]}")
print(f"Middle elements: {student[1:3]}")

# =============================================================================
# TUPLE OPERATIONS
# =============================================================================
print("\n\n4. TUPLE OPERATIONS")
print("-" * 25)

# Concatenation
print("Concatenation:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"tuple1 + tuple2: {combined}")

# Repetition
print("\nRepetition:")
repeated = (1, 2) * 3
print(f"(1, 2) * 3: {repeated}")

# Length
print(f"\nLength:")
print(f"len(student): {len(student)}")

# Membership testing
print(f"\nMembership testing:")
print(f"'Alice' in student: {'Alice' in student}")
print(f"'Bob' in student: {'Bob' in student}")
print(f"'Bob' not in student: {'Bob' not in student}")

# =============================================================================
# TUPLE METHODS
# =============================================================================
print("\n\n5. TUPLE METHODS")
print("-" * 20)

# count() - Count occurrences of value
print("count() - Count occurrences of value:")
numbers = (1, 2, 3, 2, 1, 3, 1, 2, 1)
print(f"Numbers: {numbers}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Count of 5: {numbers.count(5)}")

# index() - Find index of first occurrence
print(f"\nindex() - Find index of first occurrence:")
print(f"Index of 2: {numbers.index(2)}")
print(f"Index of 3: {numbers.index(3)}")

# index() with start and end
print(f"\nindex() with start and end:")
print(f"Index of 2 from position 3: {numbers.index(2, 3)}")

# =============================================================================
# IMMUTABILITY OF TUPLES
# =============================================================================
print("\n\n6. IMMUTABILITY OF TUPLES")
print("-" * 30)

print("Tuples are immutable - you cannot modify them after creation:")
print("This means you CANNOT:")
print("• Change individual elements")
print("• Add elements")
print("• Remove elements")
print("• Sort in place")

# Demonstrating immutability
print("\nDemonstrating immutability:")
my_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {my_tuple}")

# This would cause an error:
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
print("my_tuple[0] = 10  # This would cause a TypeError!")

# But you can create new tuples
new_tuple = my_tuple + (6, 7)
print(f"New tuple: {new_tuple}")

# =============================================================================
# WHEN TO USE TUPLES
# =============================================================================
print("\n\n7. WHEN TO USE TUPLES")
print("-" * 25)

print("✅ Use tuples when:")
print("• Data should not be changed (immutable)")
print("• You need to use data as dictionary keys")
print("• You want better performance for read-only operations")
print("• You need to return multiple values from a function")
print("• You have fixed-size collections")
print("• You want to ensure data integrity")

print("\n❌ Don't use tuples when:")
print("• You need to modify the data frequently")
print("• You need to add or remove elements")
print("• You need list methods like append(), remove(), etc.")

# Example 1: Coordinates (fixed, shouldn't change)
print("\nExample 1: Coordinates (fixed, shouldn't change)")
point = (10, 20)
print(f"Point coordinates: {point}")

# Example 2: RGB color values
print("\nExample 2: RGB color values")
red_color = (255, 0, 0)
green_color = (0, 255, 0)
blue_color = (0, 0, 255)
print(f"Red: {red_color}, Green: {green_color}, Blue: {blue_color}")

# Example 3: Database record
print("\nExample 3: Database record")
user_record = ("john_doe", "John Doe", "john@example.com", "active")
print(f"User record: {user_record}")

# =============================================================================
# TUPLES AS DICTIONARY KEYS
# =============================================================================
print("\n\n8. TUPLES AS DICTIONARY KEYS")
print("-" * 35)

print("Tuples can be used as dictionary keys (unlike lists):")

# Coordinates as keys
print("\nCoordinates as keys:")
locations = {(0, 0): "Origin", (1, 0): "East", (0, 1): "North", (1, 1): "Northeast"}
print(f"Locations: {locations}")
print(f"Location at (1, 1): {locations[(1, 1)]}")

# Multiple values as keys
print("\nMultiple values as keys:")
scores = {
    ("Alice", "Math"): 95,
    ("Alice", "Science"): 87,
    ("Bob", "Math"): 78,
    ("Bob", "Science"): 92,
}
print(f"Student scores: {scores}")
print(f"Alice's Math score: {scores[('Alice', 'Math')]}")

# =============================================================================
# TUPLE UNPACKING
# =============================================================================
print("\n\n9. TUPLE UNPACKING")
print("-" * 25)

# Basic unpacking
print("Basic unpacking:")
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: {coordinates}")
print(f"x: {x}, y: {y}")

# Multiple assignment
print("\nMultiple assignment:")
name, age, city = ("Alice", 25, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")

# Unpacking with * (rest)
print("\nUnpacking with * (rest):")
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"Numbers: {numbers}")
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Swapping variables
print("\nSwapping variables:")
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Tuple unpacking for swapping
print(f"After swap: a={a}, b={b}")

# =============================================================================
# FUNCTIONS RETURNING TUPLES
# =============================================================================
print("\n\n10. FUNCTIONS RETURNING TUPLES")
print("-" * 35)


# Function that returns multiple values
def get_name_and_age():
    return "Alice", 25  # Returns a tuple


def get_coordinates():
    return 10, 20  # Returns a tuple


def get_student_info():
    return "Bob", 22, "Computer Science", 3.5


# Using the functions
print("Functions returning tuples:")
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

x, y = get_coordinates()
print(f"Coordinates: x={x}, y={y}")

name, age, major, gpa = get_student_info()
print(f"Student: {name}, {age}, {major}, {gpa}")


# Returning tuple explicitly
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


numbers = [1, 2, 3, 4, 5]
minimum, maximum, average = get_stats(numbers)
print(f"Stats: min={minimum}, max={maximum}, avg={average}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n\n11. PRACTICAL EXAMPLES")
print("-" * 25)

# Example 1: Configuration settings
print("Example 1: Configuration settings")
database_config = ("localhost", 5432, "myapp", "password123")
host, port, database, password = database_config
print(f"Database: {host}:{port}/{database}")

# Example 2: Date and time
print("\nExample 2: Date and time")
date = (2024, 1, 15)  # Year, Month, Day
time = (14, 30, 0)  # Hour, Minute, Second
print(f"Date: {date[0]}-{date[1]:02d}-{date[2]:02d}")
print(f"Time: {time[0]:02d}:{time[1]:02d}:{time[2]:02d}")

# Example 3: File information
print("\nExample 3: File information")
file_info = ("document.pdf", 1024, "2024-01-15")
filename, size, date_created = file_info
print(f"File: {filename}, Size: {size} bytes, Created: {date_created}")

# Example 4: Game state
print("\nExample 4: Game state")
player_position = (100, 200)
player_health = (100, 100)  # Current, Max
print(f"Player at {player_position} with health {player_health[0]}/{player_health[1]}")

# =============================================================================
# TUPLES VS LISTS
# =============================================================================
print("\n\n12. TUPLES VS LISTS")
print("-" * 25)

print("Comparison between tuples and lists:")
print("┌─────────────┬─────────────┬─────────────┐")
print("│ Feature     │ Tuple       │ List        │")
print("├─────────────┼─────────────┼─────────────┤")
print("│ Mutability  │ Immutable   │ Mutable     │")
print("│ Syntax      │ ()          │ []          │")
print("│ Performance │ Faster      │ Slower      │")
print("│ Memory      │ Less        │ More        │")
print("│ Dictionary  │ Can be key  │ Cannot      │")
print("│ Methods     │ Few (2)     │ Many (11+)  │")
print("│ Use case    │ Fixed data  │ Dynamic data│")
print("└─────────────┴─────────────┴─────────────┘")

# Performance comparison
print("\nPerformance comparison:")
import time

# Test data
data = list(range(10000))

# List creation and access
start_time = time.time()
list_data = list(data)
for i in range(1000):
    _ = list_data[i]
list_time = time.time() - start_time

# Tuple creation and access
start_time = time.time()
tuple_data = tuple(data)
for i in range(1000):
    _ = tuple_data[i]
tuple_time = time.time() - start_time

print(f"List time: {list_time:.4f} seconds")
print(f"Tuple time: {tuple_time:.4f} seconds")
print(f"Tuples are {list_time/tuple_time:.1f}x faster for this operation!")

# =============================================================================
# COMMON TUPLE PATTERNS
# =============================================================================
print("\n\n13. COMMON TUPLE PATTERNS")
print("-" * 30)

# Pattern 1: Multiple return values
print("Pattern 1: Multiple return values")


def divide_with_remainder(a, b):
    return a // b, a % b


quotient, remainder = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")

# Pattern 2: Enumerating with tuples
print("\nPattern 2: Enumerating with tuples")
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Pattern 3: Zipping lists into tuples
print("\nPattern 3: Zipping lists into tuples")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = list(zip(names, ages))
print(f"People: {people}")

# Pattern 4: Tuple as record
print("\nPattern 4: Tuple as record")


def process_student(student_tuple):
    name, age, grade = student_tuple
    return f"{name} (age {age}) has grade {grade}"


student = ("Alice", 20, "A")
result = process_student(student)
print(f"Student info: {result}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n14. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ Tuples are immutable sequences")
print("✓ Created with parentheses () or tuple() constructor")
print("✓ Single element tuples need a trailing comma")
print("✓ Support indexing, slicing, and basic operations")
print("✓ Have only two methods: count() and index()")
print("✓ Can be used as dictionary keys")
print("✓ Support tuple unpacking for multiple assignment")
print("✓ Great for fixed data and multiple return values")
print("✓ Faster than lists for read-only operations")
print("✓ Use when data shouldn't change")
print("✓ Don't use when you need to modify data frequently")
print("\nTuples are perfect for fixed data and multiple return values! 📦")
