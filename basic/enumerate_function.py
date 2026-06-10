"""
The enumerate() Function in Python
===================================

enumerate() is a built-in function that adds a counter to an iterable and returns
it as an enumerate object. This enumerate object yields pairs containing a count
(from start, which defaults to 0) and the values from the iterable.

Key Points:
- Returns an enumerate object (which is an iterator)
- Automatically tracks the index while looping through an iterable
- More Pythonic than using range(len(iterable))
- Can start counting from any number
- Works with any iterable (lists, tuples, strings, etc.)

Syntax:
    enumerate(iterable, start=0)

Parameters:
- iterable: Any iterable object (list, tuple, string, etc.)
- start: The starting value of the counter (default is 0)
"""

# ============================================
# 1. BASIC ENUMERATE USAGE
# ============================================

print("=" * 50)
print("1. BASIC ENUMERATE USAGE")
print("=" * 50)

# Simple enumeration of a list
fruits = ["apple", "banana", "cherry", "date"]

print("Using enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print()

# Without enumerate (the old way - not recommended)
print("Without enumerate (not recommended):")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print()

# ============================================
# 2. ENUMERATE WITH DIFFERENT START VALUES
# ============================================

print("=" * 50)
print("2. ENUMERATE WITH DIFFERENT START VALUES")
print("=" * 50)

# Start counting from 0 (default)
print("Starting from 0 (default):")
for index, fruit in enumerate(fruits):
    print(f"{index}. {fruit}")

print()

# Start counting from 1
print("Starting from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

print()

# Start counting from 10
print("Starting from 10:")
for index, fruit in enumerate(fruits, start=10):
    print(f"{index}. {fruit}")

print()

# Start counting from negative numbers
print("Starting from -5:")
for index, fruit in enumerate(fruits, start=-5):
    print(f"{index}. {fruit}")

print()

# ============================================
# 3. ENUMERATE OBJECT PROPERTIES
# ============================================

print("=" * 50)
print("3. ENUMERATE OBJECT PROPERTIES")
print("=" * 50)

# Creating an enumerate object
enum_obj = enumerate(fruits)
print(f"Enumerate object: {enum_obj}")
print(f"Type: {type(enum_obj)}")

# Converting to list to see all pairs
enum_list = list(enumerate(fruits))
print(f"As list: {enum_list}")

# Converting to list with start parameter
enum_list_start = list(enumerate(fruits, start=1))
print(f"As list (start=1): {enum_list_start}")

# Converting to tuple
enum_tuple = tuple(enumerate(fruits))
print(f"As tuple: {enum_tuple}")

# Converting to dictionary
enum_dict = dict(enumerate(fruits))
print(f"As dictionary: {enum_dict}")

print()

# ============================================
# 4. ENUMERATE WITH DIFFERENT ITERABLES
# ============================================

print("=" * 50)
print("4. ENUMERATE WITH DIFFERENT ITERABLES")
print("=" * 50)

# Enumerate a string
print("Enumerating a string:")
text = "Python"
for index, char in enumerate(text):
    print(f"Position {index}: '{char}'")

print()

# Enumerate a tuple
print("Enumerating a tuple:")
colors = ("red", "green", "blue")
for index, color in enumerate(colors):
    print(f"{index}: {color}")

print()

# Enumerate a set (note: sets are unordered)
print("Enumerating a set:")
numbers_set = {10, 20, 30, 40}
for index, num in enumerate(numbers_set):
    print(f"{index}: {num}")

print()

# Enumerate a dictionary
print("Enumerating a dictionary (keys):")
person = {"name": "Alice", "age": 30, "city": "NYC"}
for index, key in enumerate(person):
    print(f"{index}: {key} = {person[key]}")

print()

# Enumerate dictionary items
print("Enumerating dictionary items:")
for index, (key, value) in enumerate(person.items()):
    print(f"{index}: {key} = {value}")

print()

# Enumerate a range
print("Enumerating a range:")
for index, num in enumerate(range(5, 10)):
    print(f"Position {index}: value {num}")

print()

# ============================================
# 5. PRACTICAL USE CASES
# ============================================

print("=" * 50)
print("5. PRACTICAL USE CASES")
print("=" * 50)

# Use Case 1: Creating numbered lists
print("Use Case 1: Numbered List")
tasks = ["Buy groceries", "Clean house", "Write code", "Exercise"]
for num, task in enumerate(tasks, start=1):
    print(f"{num}. {task}")

print()

# Use Case 2: Finding index of elements that meet a condition
print("Use Case 2: Finding indices of even numbers")
numbers = [1, 4, 7, 8, 10, 13, 16]
even_indices = []
for index, num in enumerate(numbers):
    if num % 2 == 0:
        even_indices.append((index, num))
        print(f"Even number {num} found at index {index}")

print()

# Use Case 3: Comparing two lists element by element
print("Use Case 3: Comparing two lists")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 4, 4, 6]

for index, (val1, val2) in enumerate(zip(list1, list2)):
    if val1 != val2:
        print(f"Difference at index {index}: {val1} != {val2}")

print()

# Use Case 4: Tracking progress
print("Use Case 4: Processing with progress indicator")
files = ["file1.txt", "file2.txt", "file3.txt"]
total = len(files)

for index, filename in enumerate(files, start=1):
    print(f"Processing {filename} ({index}/{total})")
    # Simulate processing
    import time

    time.sleep(0.1)

print()

# Use Case 5: Modifying list elements based on index
print("Use Case 5: Modifying list elements")
scores = [85, 90, 75, 88, 92]
print(f"Original scores: {scores}")

# Add bonus points to first 3 students
for index, score in enumerate(scores):
    if index < 3:
        scores[index] = score + 5

print(f"After bonus: {scores}")

print()

# ============================================
# 6. ENUMERATE IN COMPREHENSIONS
# ============================================

print("=" * 50)
print("6. ENUMERATE IN COMPREHENSIONS")
print("=" * 50)

# List comprehension with enumerate
words = ["hello", "world", "python", "code"]

# Create list of tuples
indexed_words = [(i, word) for i, word in enumerate(words)]
print(f"Indexed words: {indexed_words}")

# Create list with conditional
long_words = [(i, word) for i, word in enumerate(words) if len(word) > 4]
print(f"Long words with indices: {long_words}")

# Dictionary comprehension with enumerate
word_dict = {i: word for i, word in enumerate(words)}
print(f"Word dictionary: {word_dict}")

# Create reverse dictionary (word to index)
index_dict = {word: i for i, word in enumerate(words)}
print(f"Index dictionary: {index_dict}")

print()

# ============================================
# 7. NESTED ENUMERATE
# ============================================

print("=" * 50)
print("7. NESTED ENUMERATE")
print("=" * 50)

# Creating a grid with enumerate
print("Creating a coordinate grid:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        print(f"matrix[{row_index}][{col_index}] = {value}")

print()

# Finding specific element in 2D list
print("Finding element '5' in matrix:")
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == 5:
            print(f"Found 5 at position ({i}, {j})")

print()

# ============================================
# 8. ENUMERATE WITH UNPACKING
# ============================================

print("=" * 50)
print("8. ENUMERATE WITH UNPACKING")
print("=" * 50)

# List of tuples
students = [
    ("Alice", 85, "A"),
    ("Bob", 78, "B"),
    ("Charlie", 92, "A"),
]

print("Student records:")
for index, (name, score, grade) in enumerate(students, start=1):
    print(f"{index}. {name}: Score={score}, Grade={grade}")

print()

# List of lists
coordinates = [[1, 2], [3, 4], [5, 6]]

print("Coordinates:")
for index, [x, y] in enumerate(coordinates):
    print(f"Point {index}: x={x}, y={y}")

print()

# ============================================
# 9. ENUMERATE VS OTHER METHODS
# ============================================

print("=" * 50)
print("9. ENUMERATE VS OTHER METHODS")
print("=" * 50)

data = ["a", "b", "c", "d", "e"]

# Method 1: Using enumerate (Best - Most Pythonic)
print("Method 1: Using enumerate (RECOMMENDED):")
for i, item in enumerate(data):
    print(f"{i}: {item}", end=" ")
print("\n")

# Method 2: Using range and len (Not recommended)
print("Method 2: Using range(len()) - Not Pythonic:")
for i in range(len(data)):
    print(f"{i}: {data[i]}", end=" ")
print("\n")

# Method 3: Manual counter (Worst - Not recommended)
print("Method 3: Manual counter - Avoid this:")
counter = 0
for item in data:
    print(f"{counter}: {item}", end=" ")
    counter += 1
print("\n")

print()

# ============================================
# 10. ADVANCED PATTERNS
# ============================================

print("=" * 50)
print("10. ADVANCED PATTERNS")
print("=" * 50)

# Pattern 1: Skip first element
print("Pattern 1: Skip first element")
items = ["header", "item1", "item2", "item3"]
for index, item in enumerate(items):
    if index == 0:
        continue
    print(f"{index}. {item}")

print()

# Pattern 2: Process every nth element
print("Pattern 2: Process every 2nd element")
numbers = [10, 20, 30, 40, 50, 60]
for index, num in enumerate(numbers):
    if index % 2 == 0:
        print(f"Index {index}: {num}")

print()

# Pattern 3: Get first and last elements differently
print("Pattern 3: Special handling for first and last")
items = ["Start", "Middle1", "Middle2", "End"]
for index, item in enumerate(items):
    if index == 0:
        print(f"FIRST: {item}")
    elif index == len(items) - 1:
        print(f"LAST: {item}")
    else:
        print(f"Middle {index}: {item}")

print()

# Pattern 4: Creating alternating patterns
print("Pattern 4: Alternating colors")
rows = ["Row 1", "Row 2", "Row 3", "Row 4", "Row 5"]
for index, row in enumerate(rows):
    color = "white" if index % 2 == 0 else "gray"
    print(f"{row} - Background: {color}")

print()

# ============================================
# 11. ENUMERATE WITH BUILT-IN FUNCTIONS
# ============================================

print("=" * 50)
print("11. ENUMERATE WITH BUILT-IN FUNCTIONS")
print("=" * 50)

# Using enumerate with map
print("Using enumerate with map:")
words = ["hello", "world", "python"]
# Create formatted strings
formatted = list(map(lambda x: f"{x[0]}. {x[1]}", enumerate(words, 1)))
print(formatted)

print()

# Using enumerate with filter
print("Using enumerate with filter:")
numbers = [10, 25, 30, 45, 50, 65]
# Get elements at even indices
even_indexed = list(filter(lambda x: x[0] % 2 == 0, enumerate(numbers)))
print(f"Even indexed elements: {even_indexed}")

print()

# Using enumerate with sorted
print("Using enumerate with sorted:")
scores = [85, 92, 78, 95, 88]
# Sort by score but keep original index
sorted_with_index = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
print("Ranking:")
for rank, (original_index, score) in enumerate(sorted_with_index, 1):
    print(f"Rank {rank}: Student {original_index} with score {score}")

print()

# ============================================
# 12. COMMON MISTAKES AND TIPS
# ============================================

print("=" * 50)
print("12. COMMON MISTAKES AND TIPS")
print("=" * 50)

# Mistake 1: Forgetting to unpack the tuple
print("Mistake 1: Not unpacking properly")
colors = ["red", "green", "blue"]

# Wrong way (accessing tuple directly)
print("Wrong way:")
for item in enumerate(colors):
    print(f"Type: {type(item)}, Value: {item}")

print()

# Right way (unpacking the tuple)
print("Right way:")
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

print()

# Tip 1: Use _ for unused variables
print("Tip 1: Use _ for unused index")
names = ["Alice", "Bob", "Charlie"]
# If you don't need the index
for _, name in enumerate(names):
    print(f"Hello, {name}!")

print()

# Tip 2: enumerate returns an iterator (use it once)
print("Tip 2: Enumerate returns an iterator")
colors = ["red", "green", "blue"]
color_enum = enumerate(colors)

print("First iteration:")
for i, color in color_enum:
    print(f"{i}: {color}")

print("Second iteration (empty - iterator exhausted):")
for i, color in color_enum:
    print(f"{i}: {color}")

print("No output above because iterator is exhausted!")
print()

# Tip 3: Convert to list if you need to use it multiple times
print("Tip 3: Convert to list for multiple uses")
color_list = list(enumerate(colors))
print(f"First use: {color_list}")
print(f"Second use: {color_list}")

print()

# ============================================
# 13. REAL-WORLD EXAMPLES
# ============================================

print("=" * 50)
print("13. REAL-WORLD EXAMPLES")
print("=" * 50)

# Example 1: CSV-like data processing
print("Example 1: Processing CSV data")
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"],
    ["Charlie", "35", "Chicago"],
]

for row_num, row in enumerate(csv_data):
    if row_num == 0:
        print(f"Header: {', '.join(row)}")
    else:
        print(f"Row {row_num}: {', '.join(row)}")

print()

# Example 2: Menu system
print("Example 2: Menu system")
menu_items = ["New File", "Open", "Save", "Exit"]

print("Main Menu:")
for index, item in enumerate(menu_items, start=1):
    print(f"  {index}. {item}")

print()

# Example 3: Table generation
print("Example 3: Generating HTML-like table")
headers = ["ID", "Name", "Score"]
data = [[1, "Alice", 95], [2, "Bob", 87], [3, "Charlie", 92]]

# Print headers
print("| " + " | ".join(headers) + " |")
print("-" * 30)

# Print data rows
for row_num, row in enumerate(data, start=1):
    print("| " + " | ".join(map(str, row)) + " |")

print()

# Example 4: Error logging with line numbers
print("Example 4: Code review with line numbers")
code_lines = [
    "def calculate(x, y):",
    "    result = x + y",
    "    return result",
    "",
    "print(calculate(5, 3))",
]

for line_num, code in enumerate(code_lines, start=1):
    print(f"{line_num:3d} | {code}")

print()

"""
SUMMARY
=======

What is enumerate()?
- A built-in function that adds an automatic counter to an iterable
- Returns an enumerate object (iterator) that yields (index, value) pairs
- More Pythonic than using range(len(iterable))

Syntax:
    enumerate(iterable, start=0)

When to use enumerate():
1. When you need both index and value in a loop
2. Creating numbered lists or menus
3. Tracking position while iterating
4. Comparing elements with their indices
5. Processing CSV or tabular data
6. Finding positions of elements that meet conditions
7. Creating coordinate systems or grids

Advantages:
- More readable and Pythonic
- Automatic counter management
- Works with any iterable
- Flexible starting point
- Less error-prone than manual counters

Best Practices:
- Always use enumerate instead of range(len())
- Unpack the tuple (index, value) properly
- Use meaningful variable names
- Set appropriate start value (often 1 for human-readable lists)
- Use _ for unused index if you don't need it
- Convert to list if you need to use it multiple times

Common Patterns:
- enumerate(iterable) → start from 0
- enumerate(iterable, start=1) → start from 1 (numbered lists)
- for i, val in enumerate(data) → basic unpacking
- dict(enumerate(list)) → create index dictionary
- enumerate(zip(list1, list2)) → enumerate multiple lists
"""

print("=" * 50)
print("END OF ENUMERATE() FUNCTION EXPLANATION")
print("=" * 50)
