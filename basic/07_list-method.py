"""
Python Basics - List Methods
This file demonstrates all the important list methods in Python.
List methods help you manipulate and work with lists efficiently.
"""

print("=== Python List Methods Tutorial ===\n")

# =============================================================================
# SAMPLE LISTS FOR DEMONSTRATION
# =============================================================================
print("Sample lists for demonstration:")
fruits = ["apple", "banana", "orange", "grape", "apple"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
mixed = ["hello", 42, 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}\n")

# =============================================================================
# ADDING ELEMENTS
# =============================================================================
print("1. ADDING ELEMENTS")
print("-" * 20)

# append() - Add element to end
print("append() - Add element to end:")
fruits.append("strawberry")
print(f"After append('strawberry'): {fruits}")

# insert() - Insert element at specific position
print(f"\ninsert() - Insert element at specific position:")
fruits.insert(1, "mango")
print(f"After insert(1, 'mango'): {fruits}")

# extend() - Add multiple elements from another iterable
print(f"\nextend() - Add multiple elements from another iterable:")
new_fruits = ["kiwi", "pineapple"]
fruits.extend(new_fruits)
print(f"After extend(['kiwi', 'pineapple']): {fruits}")

# += operator (similar to extend)
print(f"\n+= operator (similar to extend):")
fruits += ["cherry", "blueberry"]
print(f"After += ['cherry', 'blueberry']: {fruits}")

# =============================================================================
# REMOVING ELEMENTS
# =============================================================================
print("\n\n2. REMOVING ELEMENTS")
print("-" * 20)

# pop() - Remove and return element by index
print("pop() - Remove and return element by index:")
removed = fruits.pop()  # Remove last element
print(f"Removed: {removed}")
print(f"After pop(): {fruits}")

removed = fruits.pop(2)  # Remove element at index 2
print(f"Removed at index 2: {removed}")
print(f"After pop(2): {fruits}")

# remove() - Remove first occurrence of value
print(f"\nremove() - Remove first occurrence of value:")
fruits.remove("apple")  # Remove first "apple"
print(f"After remove('apple'): {fruits}")

# clear() - Remove all elements
print(f"\nclear() - Remove all elements:")
temp_list = [1, 2, 3, 4, 5]
print(f"Before clear: {temp_list}")
temp_list.clear()
print(f"After clear: {temp_list}")

# =============================================================================
# SEARCHING AND COUNTING
# =============================================================================
print("\n\n3. SEARCHING AND COUNTING")
print("-" * 30)

# Reset fruits list for demonstration
fruits = ["apple", "banana", "orange", "grape", "apple", "kiwi"]

# index() - Find index of first occurrence
print("index() - Find index of first occurrence:")
apple_index = fruits.index("apple")
print(f"Index of 'apple': {apple_index}")

# index() with start and end
print(f"\nindex() with start and end:")
apple_index_2 = fruits.index("apple", 2)  # Start searching from index 2
print(f"Index of 'apple' from index 2: {apple_index_2}")

# count() - Count occurrences of value
print(f"\ncount() - Count occurrences of value:")
apple_count = fruits.count("apple")
print(f"Count of 'apple': {apple_count}")

# in operator - Check if element exists
print(f"\nin operator - Check if element exists:")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")

# =============================================================================
# SORTING AND REVERSING
# =============================================================================
print("\n\n4. SORTING AND REVERSING")
print("-" * 30)

# sort() - Sort list in place
print("sort() - Sort list in place:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Before sort: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")

# sort() with reverse parameter
print(f"\nsort() with reverse parameter:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sort() with key function
print(f"\nsort() with key function:")
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)  # Sort by length
print(f"After sort(key=len): {words}")

# reverse() - Reverse list in place
print(f"\nreverse() - Reverse list in place:")
numbers = [1, 2, 3, 4, 5]
print(f"Before reverse: {numbers}")
numbers.reverse()
print(f"After reverse(): {numbers}")

# =============================================================================
# COPYING AND CONCATENATION
# =============================================================================
print("\n\n5. COPYING AND CONCATENATION")
print("-" * 35)

# copy() - Create shallow copy
print("copy() - Create shallow copy:")
original = [1, 2, 3, [4, 5]]
shallow_copy = original.copy()
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")
print(f"Are they the same object? {original is shallow_copy}")

# Modify nested list to show shallow copy behavior
original[3][0] = 99
print(f"After modifying nested list:")
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# =============================================================================
# LIST COMPREHENSIONS
# =============================================================================
print("\n\n6. LIST COMPREHENSIONS")
print("-" * 30)

# Basic list comprehension
print("Basic list comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# List comprehension with condition
print(f"\nList comprehension with condition:")
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# List comprehension with transformation
print(f"\nList comprehension with transformation:")
words = ["hello", "world", "python"]
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")

# Nested list comprehension
print(f"\nNested list comprehension:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# List comprehension with multiple conditions
print(f"\nList comprehension with multiple conditions:")
numbers = range(1, 21)
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {filtered}")

# =============================================================================
# PRACTICAL EXAMPLES WITH METHODS
# =============================================================================
print("\n\n7. PRACTICAL EXAMPLES WITH METHODS")
print("-" * 40)

# Example 1: Building a list from user input
print("Example 1: Building a list from user input")
shopping_list = []
items = ["milk", "bread", "eggs", "butter", "cheese"]

for item in items:
    shopping_list.append(item)

print(f"Shopping list: {shopping_list}")

# Example 2: Removing duplicates while preserving order
print(f"\nExample 2: Removing duplicates while preserving order")
duplicates = ["apple", "banana", "apple", "orange", "banana", "apple"]
unique_items = []
for item in duplicates:
    if item not in unique_items:
        unique_items.append(item)
print(f"Original: {duplicates}")
print(f"Unique items: {unique_items}")

# Example 3: Sorting with custom key
print(f"\nExample 3: Sorting with custom key")
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 96},
]

# Sort by grade (descending)
students.sort(key=lambda x: x["grade"], reverse=True)
print("Students sorted by grade (descending):")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

# Example 4: List as stack operations
print(f"\nExample 4: List as stack operations")
stack = []
operations = ["push(1)", "push(2)", "push(3)", "pop()", "push(4)"]

for op in operations:
    if "push" in op:
        value = int(op.split("(")[1].split(")")[0])
        stack.append(value)
        print(f"  {op}: {stack}")
    elif "pop" in op:
        if stack:
            popped = stack.pop()
            print(f"  {op}: popped {popped}, stack: {stack}")
        else:
            print(f"  {op}: stack is empty")

# =============================================================================
# COMMON METHOD PATTERNS
# =============================================================================
print("\n\n8. COMMON METHOD PATTERNS")
print("-" * 30)

# Pattern 1: Safe list access
print("Pattern 1: Safe list access")


def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default


test_list = [1, 2, 3]
print(f"safe_get(test_list, 1): {safe_get(test_list, 1)}")
print(f"safe_get(test_list, 10, 'Not found'): {safe_get(test_list, 10, 'Not found')}")

# Pattern 2: List rotation
print(f"\nPattern 2: List rotation")


def rotate_list(lst, n):
    n = n % len(lst)  # Handle negative and large values
    return lst[n:] + lst[:n]


original = [1, 2, 3, 4, 5]
rotated = rotate_list(original, 2)
print(f"Original: {original}")
print(f"Rotated by 2: {rotated}")

# Pattern 3: Chunking a list
print(f"\nPattern 3: Chunking a list")


def chunk_list(lst, chunk_size):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


numbers = list(range(1, 11))
chunks = chunk_list(numbers, 3)
print(f"Numbers: {numbers}")
print(f"Chunks of 3: {chunks}")

# Pattern 4: Flattening nested lists
print(f"\nPattern 4: Flattening nested lists")


def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


nested = [1, [2, 3], [4, [5, 6]], 7]
flattened = flatten_list(nested)
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

# =============================================================================
# PERFORMANCE CONSIDERATIONS
# =============================================================================
print("\n\n9. PERFORMANCE CONSIDERATIONS")
print("-" * 35)

# append() vs insert()
print("append() vs insert() performance:")
import time

# Test append() - O(1) operation
start_time = time.time()
test_list = []
for i in range(10000):
    test_list.append(i)
append_time = time.time() - start_time

# Test insert(0) - O(n) operation
start_time = time.time()
test_list = []
for i in range(1000):  # Smaller number due to slowness
    test_list.insert(0, i)
insert_time = time.time() - start_time

print(f"append() 10000 elements: {append_time:.4f} seconds")
print(f"insert(0) 1000 elements: {insert_time:.4f} seconds")
print("Note: insert(0) is much slower for large lists!")

# =============================================================================
# METHOD CHAINING AND COMBINATIONS
# =============================================================================
print("\n\n10. METHOD CHAINING AND COMBINATIONS")
print("-" * 40)

# Combining multiple methods
print("Combining multiple methods:")
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Remove duplicates, sort, and reverse
unique_sorted = sorted(set(data), reverse=True)
print(f"Original: {data}")
print(f"Unique, sorted, reversed: {unique_sorted}")

# Filter, transform, and sort
words = ["apple", "banana", "cherry", "date", "elderberry"]
result = sorted([word.upper() for word in words if len(word) > 4])
print(f"Words: {words}")
print(f"Long words (>4 chars), uppercase, sorted: {result}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n11. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ append() - Add element to end (O(1))")
print("✓ insert() - Insert at position (O(n))")
print("✓ extend() - Add multiple elements")
print("✓ pop() - Remove and return by index")
print("✓ remove() - Remove first occurrence of value")
print("✓ clear() - Remove all elements")
print("✓ index() - Find index of value")
print("✓ count() - Count occurrences")
print("✓ sort() - Sort in place")
print("✓ reverse() - Reverse in place")
print("✓ copy() - Create shallow copy")
print("✓ List comprehensions - Create lists efficiently")
print("✓ Method chaining - Combine operations")
print("✓ Performance matters - choose appropriate methods")
print("\nList methods make working with lists powerful and efficient! 🛠️")
