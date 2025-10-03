"""
Python Basics - List Comprehensions
This file demonstrates how list comprehensions work in Python.
List comprehensions are a concise way to create lists from existing iterables.
"""

print("=== Python List Comprehensions Tutorial ===\n")

# =============================================================================
# WHAT ARE LIST COMPREHENSIONS?
# =============================================================================
print("1. WHAT ARE LIST COMPREHENSIONS?")
print("-" * 40)

print("List comprehensions are a concise way to create lists in Python.")
print("They allow you to:")
print("• Create lists from existing iterables (lists, strings, ranges)")
print("• Apply transformations to each element")
print("• Filter elements based on conditions")
print("• Write more readable and often faster code")
print("\nBasic syntax: [expression for item in iterable]")
print("With condition: [expression for item in iterable if condition]\n")

# =============================================================================
# BASIC LIST COMPREHENSIONS
# =============================================================================
print("2. BASIC LIST COMPREHENSIONS")
print("-" * 35)

# Traditional way vs List comprehension
print("Traditional way vs List comprehension:")

# Traditional way
print("Traditional way:")
squares_traditional = []
for i in range(1, 6):
    squares_traditional.append(i**2)
print(f"Traditional: {squares_traditional}")

# List comprehension way
print("List comprehension way:")
squares_comprehension = [i**2 for i in range(1, 6)]
print(f"Comprehension: {squares_comprehension}")
print("Same result, but much more concise!\n")

# More basic examples
print("More basic examples:")

# From range
numbers = [x for x in range(1, 6)]
print(f"Numbers 1-5: {numbers}")

# From string
letters = [char for char in "Python"]
print(f"Letters from 'Python': {letters}")

# From existing list
fruits = ["apple", "banana", "orange"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {upper_fruits}")

# Mathematical operations
doubles = [x * 2 for x in range(1, 6)]
print(f"Doubles: {doubles}")

# =============================================================================
# LIST COMPREHENSIONS WITH CONDITIONS
# =============================================================================
print("\n\n3. LIST COMPREHENSIONS WITH CONDITIONS")
print("-" * 45)

# Filtering with if condition
print("Filtering with if condition:")

# Even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {even_numbers}")

# Long words
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = [word for word in words if len(word) > 3]
print(f"Words longer than 3 characters: {long_words}")

# Positive numbers
numbers = [-2, -1, 0, 1, 2, 3, -4, 5]
positive_numbers = [x for x in numbers if x > 0]
print(f"Positive numbers: {positive_numbers}")

# Vowels in a word
word = "programming"
vowels = [char for char in word if char in "aeiou"]
print(f"Vowels in '{word}': {vowels}")

# =============================================================================
# LIST COMPREHENSIONS WITH TRANSFORMATIONS
# =============================================================================
print("\n\n4. LIST COMPREHENSIONS WITH TRANSFORMATIONS")
print("-" * 50)

# String transformations
print("String transformations:")
names = ["alice", "bob", "charlie", "diana"]
capitalized_names = [name.capitalize() for name in names]
print(f"Capitalized names: {capitalized_names}")

# Length of words
words = ["hello", "world", "python", "programming"]
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")

# Mathematical transformations
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
cubes = [x**3 for x in numbers]
print(f"Squares: {squares}")
print(f"Cubes: {cubes}")

# Type conversions
string_numbers = ["1", "2", "3", "4", "5"]
integers = [int(x) for x in string_numbers]
print(f"String to integers: {integers}")

# =============================================================================
# COMBINING TRANSFORMATION AND FILTERING
# =============================================================================
print("\n\n5. COMBINING TRANSFORMATION AND FILTERING")
print("-" * 50)

# Square of even numbers
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Square of even numbers 1-10: {even_squares}")

# Uppercase long words
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_upper_words = [word.upper() for word in words if len(word) > 3]
print(f"Uppercase long words: {long_upper_words}")

# Length of words that start with 'p'
words = ["python", "programming", "list", "comprehension", "practice"]
p_word_lengths = [len(word) for word in words if word.startswith("p")]
print(f"Length of words starting with 'p': {p_word_lengths}")

# First letter of words longer than 4 characters
words = ["apple", "banana", "cat", "elephant", "dog"]
first_letters = [word[0] for word in words if len(word) > 4]
print(f"First letters of long words: {first_letters}")

# =============================================================================
# NESTED LIST COMPREHENSIONS
# =============================================================================
print("\n\n6. NESTED LIST COMPREHENSIONS")
print("-" * 35)

# Flattening a nested list
print("Flattening a nested list:")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(f"Nested: {nested_list}")
print(f"Flattened: {flattened}")

# Creating a matrix
print("\nCreating a matrix:")
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"3x3 matrix: {matrix}")

# Cartesian product
print("\nCartesian product:")
colors = ["red", "blue"]
sizes = ["small", "large"]
combinations = [f"{color} {size}" for color in colors for size in sizes]
print(f"Color-size combinations: {combinations}")

# =============================================================================
# LIST COMPREHENSIONS WITH MULTIPLE CONDITIONS
# =============================================================================
print("\n\n7. LIST COMPREHENSIONS WITH MULTIPLE CONDITIONS")
print("-" * 50)

# Multiple if conditions
print("Multiple if conditions:")
numbers = range(1, 21)
divisible_by_2_and_3 = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {divisible_by_2_and_3}")

# Complex conditions
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_vowel_words = [
    word for word in words if len(word) > 4 and any(vowel in word for vowel in "aeiou")
]
print(f"Long words with vowels: {long_vowel_words}")

# Range conditions
numbers = range(1, 31)
in_range = [x for x in numbers if 10 <= x <= 20]
print(f"Numbers between 10 and 20: {in_range}")

# =============================================================================
# LIST COMPREHENSIONS WITH ELSE CLAUSE
# =============================================================================
print("\n\n8. LIST COMPREHENSIONS WITH ELSE CLAUSE")
print("-" * 45)

# Conditional expressions (ternary operator)
print("Conditional expressions (ternary operator):")
numbers = range(1, 11)
even_odd = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Even/odd classification: {even_odd}")

# Grade classification
scores = [85, 92, 78, 96, 88, 65, 72, 90]
grades = [
    "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    for score in scores
]
print(f"Scores: {scores}")
print(f"Grades: {grades}")

# Positive/negative/zero
numbers = [-2, -1, 0, 1, 2, 3, -4, 5]
classification = [
    "positive" if x > 0 else "negative" if x < 0 else "zero" for x in numbers
]
print(f"Numbers: {numbers}")
print(f"Classification: {classification}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n\n9. PRACTICAL EXAMPLES")
print("-" * 25)

# Example 1: Processing student data
print("Example 1: Processing student data")
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 96},
]

# Get names of students with grade >= 90
top_students = [student["name"] for student in students if student["grade"] >= 90]
print(f"Top students (grade >= 90): {top_students}")

# Get grades of students whose names start with 'A' or 'B'
ab_grades = [student["grade"] for student in students if student["name"][0] in "AB"]
print(f"Grades of students with names starting with A or B: {ab_grades}")

# Example 2: Text processing
print("\nExample 2: Text processing")
text = "Python is a great programming language for beginners"
words = text.split()

# Words longer than 4 characters, converted to uppercase
long_upper_words = [word.upper() for word in words if len(word) > 4]
print(f"Long words in uppercase: {long_upper_words}")

# First letter of each word
first_letters = [word[0] for word in words]
print(f"First letters: {first_letters}")

# Example 3: Number processing
print("\nExample 3: Number processing")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of odd numbers
odd_squares = [x**2 for x in numbers if x % 2 == 1]
print(f"Squares of odd numbers: {odd_squares}")

# Numbers that are perfect squares
perfect_squares = [x for x in range(1, 101) if int(x**0.5) ** 2 == x]
print(f"Perfect squares 1-100: {perfect_squares[:10]}...")  # Show first 10

# =============================================================================
# COMMON PATTERNS AND TRICKS
# =============================================================================
print("\n\n10. COMMON PATTERNS AND TRICKS")
print("-" * 35)

# Pattern 1: Removing duplicates while preserving order
print("Pattern 1: Removing duplicates while preserving order")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = []
[unique_numbers.append(x) for x in numbers if x not in unique_numbers]
print(f"Original: {numbers}")
print(f"Unique: {unique_numbers}")

# Pattern 2: Creating pairs
print("\nPattern 2: Creating pairs")
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
pairs = [(x, y) for x in list1 for y in list2]
print(f"Pairs: {pairs}")

# Pattern 3: Conditional list creation
print("\nPattern 3: Conditional list creation")
condition = True
result = [x**2 for x in range(1, 6) if condition]
print(f"Conditional result: {result}")

# Pattern 4: List comprehension with function calls
print("\nPattern 4: List comprehension with function calls")


def square(x):
    return x**2


squares = [square(x) for x in range(1, 6)]
print(f"Squares using function: {squares}")

# =============================================================================
# PERFORMANCE CONSIDERATIONS
# =============================================================================
print("\n\n11. PERFORMANCE CONSIDERATIONS")
print("-" * 35)

# List comprehension vs traditional loop
print("List comprehension vs traditional loop:")
import time

# Test data
numbers = list(range(10000))

# Traditional loop
start_time = time.time()
result1 = []
for x in numbers:
    if x % 2 == 0:
        result1.append(x**2)
traditional_time = time.time() - start_time

# List comprehension
start_time = time.time()
result2 = [x**2 for x in numbers if x % 2 == 0]
comprehension_time = time.time() - start_time

print(f"Traditional loop time: {traditional_time:.4f} seconds")
print(f"List comprehension time: {comprehension_time:.4f} seconds")
print(f"List comprehension is {traditional_time/comprehension_time:.1f}x faster!")

# =============================================================================
# WHEN TO USE LIST COMPREHENSIONS
# =============================================================================
print("\n\n12. WHEN TO USE LIST COMPREHENSIONS")
print("-" * 40)

print("✅ Use list comprehensions when:")
print("• Creating a new list from an existing iterable")
print("• The logic is simple and readable")
print("• You want to filter and/or transform elements")
print("• Performance is important")

print("\n❌ Avoid list comprehensions when:")
print("• The logic is complex and hard to read")
print("• You need side effects (like printing)")
print("• You need to handle exceptions")
print("• The comprehension becomes too long")

# Example of when NOT to use
print("\nExample of when NOT to use:")
print("Complex logic - better to use traditional loop:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for x in numbers:
    if x % 2 == 0:
        if x > 5:
            result.append(x**2)
        else:
            result.append(x)
    else:
        result.append(x * 2)
print(f"Complex result: {result}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n13. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ List comprehensions are concise ways to create lists")
print("✓ Basic syntax: [expression for item in iterable]")
print("✓ Add conditions: [expression for item in iterable if condition]")
print("✓ Can combine transformation and filtering")
print("✓ Support nested comprehensions for complex operations")
print("✓ Can use conditional expressions (ternary operator)")
print("✓ Generally faster than traditional loops")
print("✓ Use when logic is simple and readable")
print("✓ Avoid when logic becomes too complex")
print("\nList comprehensions make your code more Pythonic and efficient! 🐍✨")
