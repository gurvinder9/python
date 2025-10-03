"""
Python Basics - Dictionaries
This file demonstrates how dictionaries work in Python.
Dictionaries store data in key-value pairs and are very efficient for lookups.
"""

print("=== Python Dictionaries Tutorial ===\n")

# =============================================================================
# WHAT ARE DICTIONARIES?
# =============================================================================
print("1. WHAT ARE DICTIONARIES?")
print("-" * 30)

print("Dictionaries are collections of key-value pairs.")
print("Think of them like a real dictionary:")
print("- Key = word you're looking up")
print("- Value = definition of that word")
print("- Each key must be unique")
print("- Keys are used to access values quickly\n")

# =============================================================================
# CREATING DICTIONARIES
# =============================================================================
print("2. CREATING DICTIONARIES")
print("-" * 30)

# Method 1: Using curly braces {}
print("Method 1: Using curly braces {}")
student = {"name": "Alice", "age": 20, "grade": "A", "city": "New York"}
print(f"Student dictionary: {student}")

# Method 2: Using dict() constructor
print("\nMethod 2: Using dict() constructor")
colors = dict(red="#FF0000", green="#00FF00", blue="#0000FF")
print(f"Colors dictionary: {colors}")

# Method 3: Empty dictionary
print("\nMethod 3: Empty dictionary")
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Method 4: Dictionary with different data types
print("\nMethod 4: Dictionary with mixed data types")
mixed_dict = {
    "name": "Bob",  # String
    "age": 25,  # Integer
    "height": 5.9,  # Float
    "is_student": True,  # Boolean
    "subjects": ["Math", "Science", "English"],  # List
    "grades": {"Math": 95, "Science": 87},  # Nested dictionary
}
print(f"Mixed dictionary: {mixed_dict}")

# =============================================================================
# ACCESSING VALUES
# =============================================================================
print("\n\n3. ACCESSING VALUES")
print("-" * 30)

# Accessing values using square brackets []
print("Accessing values using square brackets []")
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")
print(f"Student grade: {student['grade']}")

# Accessing nested values
print("\nAccessing nested values:")
print(f"Bob's Math grade: {mixed_dict['grades']['Math']}")
print(f"Bob's first subject: {mixed_dict['subjects'][0]}")

# Using get() method (safer way)
print("\nUsing get() method (safer way):")
print(f"Student name: {student.get('name')}")
print(f"Student phone: {student.get('phone')}")  # Returns None if key doesn't exist
print(f"Student phone with default: {student.get('phone', 'Not provided')}")

# =============================================================================
# ADDING AND MODIFYING VALUES
# =============================================================================
print("\n\n4. ADDING AND MODIFYING VALUES")
print("-" * 30)

# Adding new key-value pairs
print("Adding new key-value pairs:")
student["phone"] = "555-1234"
student["email"] = "alice@example.com"
print(f"After adding phone and email: {student}")

# Modifying existing values
print("\nModifying existing values:")
student["age"] = 21  # Alice had a birthday!
student["grade"] = "A+"
print(f"After modifications: {student}")

# =============================================================================
# CHECKING IF KEYS EXIST
# =============================================================================
print("\n\n5. CHECKING IF KEYS EXIST")
print("-" * 30)

# Using 'in' operator
print("Using 'in' operator:")
print(f"'name' in student: {'name' in student}")
print(f"'address' in student: {'address' in student}")

# Using 'not in' operator
print("\nUsing 'not in' operator:")
print(f"'address' not in student: {'address' not in student}")

# =============================================================================
# ITERATING THROUGH DICTIONARIES
# =============================================================================
print("\n\n6. ITERATING THROUGH DICTIONARIES")
print("-" * 30)

# Iterating through keys
print("Iterating through keys:")
for key in student:
    print(f"  Key: {key}")

# Iterating through keys explicitly
print("\nIterating through keys explicitly:")
for key in student.keys():
    print(f"  Key: {key}")

# Iterating through values
print("\nIterating through values:")
for value in student.values():
    print(f"  Value: {value}")

# Iterating through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# =============================================================================
# DICTIONARY LENGTH AND BASIC INFO
# =============================================================================
print("\n\n7. DICTIONARY LENGTH AND BASIC INFO")
print("-" * 30)

print(f"Number of key-value pairs in student: {len(student)}")
print(f"All keys: {list(student.keys())}")
print(f"All values: {list(student.values())}")
print(f"All items: {list(student.items())}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n\n8. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Student grades tracker
print("Example 1: Student grades tracker")
grades = {"Math": 95, "Science": 87, "English": 92, "History": 78}

print("Current grades:")
for subject, grade in grades.items():
    print(f"  {subject}: {grade}")

# Calculate average grade
total = sum(grades.values())
average = total / len(grades)
print(f"Average grade: {average:.1f}")

# Example 2: Phone book
print("\nExample 2: Phone book")
phone_book = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9012"}

print("Phone book:")
for name, phone in phone_book.items():
    print(f"  {name}: {phone}")

# Look up a phone number
name_to_find = "Bob"
if name_to_find in phone_book:
    print(f"\n{name_to_find}'s phone number: {phone_book[name_to_find]}")
else:
    print(f"\n{name_to_find} not found in phone book")

# Example 3: Word frequency counter
print("\nExample 3: Word frequency counter")
text = "hello world hello python world python"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

# =============================================================================
# COMMON DICTIONARY PATTERNS
# =============================================================================
print("\n\n9. COMMON DICTIONARY PATTERNS")
print("-" * 30)

# Pattern 1: Counting occurrences
print("Pattern 1: Counting occurrences")
numbers = [1, 2, 3, 2, 1, 3, 1, 2, 1]
count_dict = {}

for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1

print(f"Numbers: {numbers}")
print(f"Counts: {count_dict}")

# Pattern 2: Grouping items
print("\nPattern 2: Grouping items by category")
items = [
    {"name": "Apple", "category": "Fruit"},
    {"name": "Carrot", "category": "Vegetable"},
    {"name": "Banana", "category": "Fruit"},
    {"name": "Broccoli", "category": "Vegetable"},
    {"name": "Orange", "category": "Fruit"},
]

grouped = {}
for item in items:
    category = item["category"]
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(item["name"])

print("Grouped items:")
for category, names in grouped.items():
    print(f"  {category}: {names}")

# Pattern 3: Dictionary as a switch statement
print("\nPattern 3: Dictionary as a switch statement")


def get_day_type(day):
    day_types = {
        "Monday": "Weekday",
        "Tuesday": "Weekday",
        "Wednesday": "Weekday",
        "Thursday": "Weekday",
        "Friday": "Weekday",
        "Saturday": "Weekend",
        "Sunday": "Weekend",
    }
    return day_types.get(day, "Unknown")


print("Day types:")
for day in ["Monday", "Saturday", "InvalidDay"]:
    print(f"  {day}: {get_day_type(day)}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n10. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ Dictionaries store key-value pairs")
print("✓ Keys must be unique and immutable (strings, numbers, tuples)")
print("✓ Values can be any data type")
print("✓ Access values using square brackets [] or get() method")
print("✓ Use 'in' operator to check if key exists")
print("✓ Iterate with .keys(), .values(), or .items()")
print("✓ Dictionaries are mutable (can be changed)")
print("✓ Very efficient for lookups and data organization")
print("\nDictionaries are powerful tools for organizing and accessing data! 🗂️")
