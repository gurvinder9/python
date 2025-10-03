"""
Python Basics - Dictionary Methods
This file demonstrates all the important dictionary methods in Python.
Dictionary methods help you manipulate and work with dictionaries efficiently.
"""

print("=== Python Dictionary Methods Tutorial ===\n")

# =============================================================================
# SAMPLE DICTIONARIES FOR DEMONSTRATION
# =============================================================================
print("Sample dictionaries for demonstration:")
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "city": "New York",
    "subjects": ["Math", "Science", "English"],
}

scores = {"Math": 95, "Science": 87, "English": 92}

print(f"Student: {student}")
print(f"Scores: {scores}\n")

# =============================================================================
# ACCESSING METHODS
# =============================================================================
print("1. ACCESSING METHODS")
print("-" * 25)

# get() - Safe way to access values
print("get() - Safe way to access values:")
print(f"student.get('name'): {student.get('name')}")
print(f"student.get('phone'): {student.get('phone')}")  # Returns None
print(f"student.get('phone', 'Not provided'): {student.get('phone', 'Not provided')}")

# keys() - Get all keys
print(f"\nkeys() - Get all keys:")
print(f"student.keys(): {student.keys()}")
print(f"list(student.keys()): {list(student.keys())}")

# values() - Get all values
print(f"\nvalues() - Get all values:")
print(f"student.values(): {student.values()}")
print(f"list(student.values()): {list(student.values())}")

# items() - Get all key-value pairs
print(f"\nitems() - Get all key-value pairs:")
print(f"student.items(): {student.items()}")
print(f"list(student.items()): {list(student.items())}")

# =============================================================================
# MODIFYING METHODS
# =============================================================================
print("\n\n2. MODIFYING METHODS")
print("-" * 25)

# copy() - Create a shallow copy
print("copy() - Create a shallow copy:")
student_copy = student.copy()
print(f"Original: {student}")
print(f"Copy: {student_copy}")
print(f"Are they the same object? {student is student_copy}")

# update() - Update dictionary with another dictionary
print(f"\nupdate() - Update dictionary with another dictionary:")
student.update({"phone": "555-1234", "email": "alice@example.com"})
print(f"After update: {student}")

# Update with keyword arguments
student.update(age=21, grade="A+")
print(f"After keyword update: {student}")

# =============================================================================
# ADDING AND REMOVING METHODS
# =============================================================================
print("\n\n3. ADDING AND REMOVING METHODS")
print("-" * 30)

# setdefault() - Set default value if key doesn't exist
print("setdefault() - Set default value if key doesn't exist:")
print(
    f"student.setdefault('address', 'Unknown'): {student.setdefault('address', 'Unknown')}"
)
print(
    f"student.setdefault('name', 'Bob'): {student.setdefault('name', 'Bob')}"
)  # Won't change existing
print(f"After setdefault: {student}")

# pop() - Remove and return value
print(f"\npop() - Remove and return value:")
removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")
print(f"After pop('grade'): {student}")

# pop() with default value
removed_phone = student.pop("phone", "No phone")
print(f"Removed phone: {removed_phone}")

# popitem() - Remove and return last key-value pair
print(f"\npopitem() - Remove and return last key-value pair:")
last_item = student.popitem()
print(f"Removed last item: {last_item}")
print(f"After popitem(): {student}")

# clear() - Remove all items
print(f"\nclear() - Remove all items:")
temp_dict = {"a": 1, "b": 2, "c": 3}
print(f"Before clear: {temp_dict}")
temp_dict.clear()
print(f"After clear: {temp_dict}")

# =============================================================================
# CHECKING METHODS
# =============================================================================
print("\n\n4. CHECKING METHODS")
print("-" * 25)

# Reset student dictionary for demonstration
student = {"name": "Alice", "age": 20, "grade": "A", "city": "New York"}

# len() - Get number of key-value pairs
print("len() - Get number of key-value pairs:")
print(f"len(student): {len(student)}")

# in operator - Check if key exists
print(f"\nin operator - Check if key exists:")
print(f"'name' in student: {'name' in student}")
print(f"'phone' in student: {'phone' in student}")

# not in operator - Check if key doesn't exist
print(f"\nnot in operator - Check if key doesn't exist:")
print(f"'phone' not in student: {'phone' not in student}")

# =============================================================================
# ADVANCED METHODS
# =============================================================================
print("\n\n5. ADVANCED METHODS")
print("-" * 25)

# fromkeys() - Create dictionary from keys with default value
print("fromkeys() - Create dictionary from keys with default value:")
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "Unknown")
print(f"Keys: {keys}")
print(f"fromkeys result: {default_dict}")

# fromkeys() with different default values
print(f"\nfromkeys() with different default values:")
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"fromkeys with 0: {default_dict}")

# =============================================================================
# DICTIONARY COMPREHENSIONS
# =============================================================================
print("\n\n6. DICTIONARY COMPREHENSIONS")
print("-" * 35)

# Basic dictionary comprehension
print("Basic dictionary comprehension:")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Dictionary comprehension with condition
print(f"\nDictionary comprehension with condition:")
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Dictionary comprehension from existing dictionary
print(f"\nDictionary comprehension from existing dictionary:")
student_upper = {key.upper(): value for key, value in student.items()}
print(f"Student with uppercase keys: {student_upper}")

# Dictionary comprehension with transformation
print(f"\nDictionary comprehension with transformation:")
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(f"Word lengths: {word_lengths}")

# =============================================================================
# PRACTICAL EXAMPLES WITH METHODS
# =============================================================================
print("\n\n7. PRACTICAL EXAMPLES WITH METHODS")
print("-" * 40)

# Example 1: Building a dictionary from user input
print("Example 1: Building a dictionary from user input")
user_info = {}
fields = ["name", "age", "email"]

# Simulate user input
inputs = ["John", "25", "john@example.com"]

for field, value in zip(fields, inputs):
    user_info.setdefault(field, value)

print(f"User info: {user_info}")

# Example 2: Merging multiple dictionaries
print(f"\nExample 2: Merging multiple dictionaries")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

merged = {}
merged.update(dict1)
merged.update(dict2)
merged.update(dict3)
print(f"Merged dictionary: {merged}")

# Example 3: Filtering dictionary
print(f"\nExample 3: Filtering dictionary")
scores = {"Math": 95, "Science": 87, "English": 92, "History": 78, "Art": 88}
high_scores = {subject: score for subject, score in scores.items() if score >= 90}
print(f"All scores: {scores}")
print(f"High scores (>=90): {high_scores}")

# Example 4: Counting with dictionaries
print(f"\nExample 4: Counting with dictionaries")
text = "hello world hello python world python"
words = text.split()

# Method 1: Using get() with default
word_count1 = {}
for word in words:
    word_count1[word] = word_count1.get(word, 0) + 1

# Method 2: Using setdefault()
word_count2 = {}
for word in words:
    word_count2.setdefault(word, 0)
    word_count2[word] += 1

print(f"Text: {text}")
print(f"Word count (method 1): {word_count1}")
print(f"Word count (method 2): {word_count2}")

# =============================================================================
# COMMON METHOD PATTERNS
# =============================================================================
print("\n\n8. COMMON METHOD PATTERNS")
print("-" * 30)

# Pattern 1: Safe dictionary access
print("Pattern 1: Safe dictionary access")
config = {"host": "localhost", "port": 8080}
host = config.get("host", "127.0.0.1")
port = config.get("port", 3000)
debug = config.get("debug", False)
print(f"Host: {host}, Port: {port}, Debug: {debug}")

# Pattern 2: Dictionary as cache
print(f"\nPattern 2: Dictionary as cache")
cache = {}


def expensive_calculation(n):
    if n in cache:
        print(f"  Cache hit for {n}")
        return cache[n]
    else:
        print(f"  Calculating for {n}")
        result = n**2  # Simulate expensive calculation
        cache[n] = result
        return result


print("First call (cache miss):")
result1 = expensive_calculation(5)
print("Second call (cache hit):")
result2 = expensive_calculation(5)
print(f"Cache: {cache}")

# Pattern 3: Grouping with setdefault
print(f"\nPattern 3: Grouping with setdefault")
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
    {"name": "Eve", "grade": "B"},
]

grouped_by_grade = {}
for student in students:
    grade = student["grade"]
    grouped_by_grade.setdefault(grade, []).append(student["name"])

print(f"Students: {students}")
print(f"Grouped by grade: {grouped_by_grade}")

# =============================================================================
# METHOD CHAINING AND COMBINATIONS
# =============================================================================
print("\n\n9. METHOD CHAINING AND COMBINATIONS")
print("-" * 40)

# Combining multiple methods
print("Combining multiple methods:")
data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# Get all keys, convert to list, sort them
sorted_keys = sorted(data.keys())
print(f"Sorted keys: {sorted_keys}")

# Get all values, convert to list, find max
max_value = max(data.values())
print(f"Max value: {max_value}")

# Get items, filter, create new dictionary
filtered_items = {k: v for k, v in data.items() if v > 2}
print(f"Items with value > 2: {filtered_items}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n10. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ get() - Safe access with default values")
print("✓ keys(), values(), items() - Get dictionary components")
print("✓ update() - Merge dictionaries")
print("✓ copy() - Create shallow copy")
print("✓ setdefault() - Set default if key doesn't exist")
print("✓ pop() - Remove and return value")
print("✓ popitem() - Remove and return last item")
print("✓ clear() - Remove all items")
print("✓ fromkeys() - Create dictionary from keys")
print("✓ Dictionary comprehensions - Create dictionaries efficiently")
print("✓ Method chaining - Combine methods for complex operations")
print("\nDictionary methods make working with dictionaries powerful and efficient! 🛠️")
