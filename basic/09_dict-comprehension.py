"""
Python Basics - Dictionary Comprehensions
This file demonstrates how dictionary comprehensions work in Python.
Dictionary comprehensions are a concise way to create dictionaries from existing iterables.
"""

print("=== Python Dictionary Comprehensions Tutorial ===\n")

# =============================================================================
# WHAT ARE DICTIONARY COMPREHENSIONS?
# =============================================================================
print("1. WHAT ARE DICTIONARY COMPREHENSIONS?")
print("-" * 45)

print("Dictionary comprehensions are a concise way to create dictionaries in Python.")
print("They allow you to:")
print("• Create dictionaries from existing iterables")
print("• Apply transformations to keys and values")
print("• Filter key-value pairs based on conditions")
print("• Write more readable and often faster code")
print("\nBasic syntax: {key_expression: value_expression for item in iterable}")
print(
    "With condition: {key_expression: value_expression for item in iterable if condition}\n"
)

# =============================================================================
# BASIC DICTIONARY COMPREHENSIONS
# =============================================================================
print("2. BASIC DICTIONARY COMPREHENSIONS")
print("-" * 40)

# Traditional way vs Dictionary comprehension
print("Traditional way vs Dictionary comprehension:")

# Traditional way
print("Traditional way:")
squares_traditional = {}
for i in range(1, 6):
    squares_traditional[i] = i**2
print(f"Traditional: {squares_traditional}")

# Dictionary comprehension way
print("Dictionary comprehension way:")
squares_comprehension = {i: i**2 for i in range(1, 6)}
print(f"Comprehension: {squares_comprehension}")
print("Same result, but much more concise!\n")

# More basic examples
print("More basic examples:")

# From range
number_dict = {x: x * 2 for x in range(1, 6)}
print(f"Number to double: {number_dict}")

# From string
char_positions = {char: i for i, char in enumerate("Python")}
print(f"Character positions: {char_positions}")

# From existing list
fruits = ["apple", "banana", "orange"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(f"Fruit lengths: {fruit_lengths}")

# From existing dictionary
original = {"a": 1, "b": 2, "c": 3}
doubled = {key: value * 2 for key, value in original.items()}
print(f"Doubled values: {doubled}")

# =============================================================================
# DICTIONARY COMPREHENSIONS WITH CONDITIONS
# =============================================================================
print("\n\n3. DICTIONARY COMPREHENSIONS WITH CONDITIONS")
print("-" * 50)

# Filtering with if condition
print("Filtering with if condition:")

# Even numbers and their squares
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Long words and their lengths
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = {word: len(word) for word in words if len(word) > 3}
print(f"Long words: {long_words}")

# Positive numbers and their absolute values
numbers = [-2, -1, 0, 1, 2, 3, -4, 5]
positive_dict = {x: abs(x) for x in numbers if x > 0}
print(f"Positive numbers: {positive_dict}")

# Vowels in a word
word = "programming"
vowel_positions = {char: i for i, char in enumerate(word) if char in "aeiou"}
print(f"Vowel positions in '{word}': {vowel_positions}")

# =============================================================================
# DICTIONARY COMPREHENSIONS WITH TRANSFORMATIONS
# =============================================================================
print("\n\n4. DICTIONARY COMPREHENSIONS WITH TRANSFORMATIONS")
print("-" * 55)

# String transformations
print("String transformations:")
names = ["alice", "bob", "charlie", "diana"]
name_dict = {name: name.capitalize() for name in names}
print(f"Capitalized names: {name_dict}")

# Key and value transformations
words = ["hello", "world", "python", "programming"]
word_info = {word.upper(): len(word) for word in words}
print(f"Word info: {word_info}")

# Mathematical transformations
numbers = [1, 2, 3, 4, 5]
math_dict = {x: {"square": x**2, "cube": x**3} for x in numbers}
print(f"Math operations: {math_dict}")

# Type conversions
string_numbers = ["1", "2", "3", "4", "5"]
number_dict = {x: int(x) for x in string_numbers}
print(f"String to integers: {number_dict}")

# =============================================================================
# COMBINING TRANSFORMATION AND FILTERING
# =============================================================================
print("\n\n5. COMBINING TRANSFORMATION AND FILTERING")
print("-" * 55)

# Square of even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Square of even numbers 1-10: {even_squares}")

# Uppercase long words
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_upper_words = {word.upper(): len(word) for word in words if len(word) > 3}
print(f"Uppercase long words: {long_upper_words}")

# Length of words that start with 'p'
words = ["python", "programming", "list", "comprehension", "practice"]
p_word_info = {word: len(word) for word in words if word.startswith("p")}
print(f"Words starting with 'p': {p_word_info}")

# First letter of words longer than 4 characters
words = ["apple", "banana", "cat", "elephant", "dog"]
first_letter_dict = {word: word[0] for word in words if len(word) > 4}
print(f"First letters of long words: {first_letter_dict}")

# =============================================================================
# DICTIONARY COMPREHENSIONS WITH MULTIPLE CONDITIONS
# =============================================================================
print("\n\n6. DICTIONARY COMPREHENSIONS WITH MULTIPLE CONDITIONS")
print("-" * 55)

# Multiple if conditions
print("Multiple if conditions:")
numbers = range(1, 21)
divisible_dict = {x: x**2 for x in numbers if x % 2 == 0 and x % 3 == 0}
print(f"Numbers divisible by both 2 and 3: {divisible_dict}")

# Complex conditions
words = ["apple", "banana", "cherry", "date", "elderberry"]
complex_dict = {
    word: len(word)
    for word in words
    if len(word) > 4 and any(vowel in word for vowel in "aeiou")
}
print(f"Long words with vowels: {complex_dict}")

# Range conditions
numbers = range(1, 31)
range_dict = {x: x**2 for x in numbers if 10 <= x <= 20}
print(f"Numbers between 10 and 20: {range_dict}")

# =============================================================================
# DICTIONARY COMPREHENSIONS WITH ELSE CLAUSE
# =============================================================================
print("\n\n7. DICTIONARY COMPREHENSIONS WITH ELSE CLAUSE")
print("-" * 50)

# Conditional expressions (ternary operator)
print("Conditional expressions (ternary operator):")
numbers = range(1, 11)
even_odd_dict = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print(f"Even/odd classification: {even_odd_dict}")

# Grade classification
scores = [85, 92, 78, 96, 88, 65, 72, 90]
grade_dict = {
    score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    for score in scores
}
print(f"Score to grade: {grade_dict}")

# Positive/negative/zero
numbers = [-2, -1, 0, 1, 2, 3, -4, 5]
classification_dict = {
    x: "positive" if x > 0 else "negative" if x < 0 else "zero" for x in numbers
}
print(f"Number classification: {classification_dict}")

# =============================================================================
# NESTED DICTIONARY COMPREHENSIONS
# =============================================================================
print("\n\n8. NESTED DICTIONARY COMPREHENSIONS")
print("-" * 40)

# Creating nested dictionaries
print("Creating nested dictionaries:")
matrix_dict = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(f"Multiplication table: {matrix_dict}")

# Flattening nested dictionaries
print("\nFlattening nested dictionaries:")
nested = {"group1": {"a": 1, "b": 2}, "group2": {"c": 3, "d": 4}}
flattened = {
    f"{outer_key}_{inner_key}": value
    for outer_key, inner_dict in nested.items()
    for inner_key, value in inner_dict.items()
}
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

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

# Create name to grade mapping
name_to_grade = {student["name"]: student["grade"] for student in students}
print(f"Name to grade: {name_to_grade}")

# Create grade to name mapping for top students
top_students = {
    student["grade"]: student["name"] for student in students if student["grade"] >= 90
}
print(f"Top students (grade >= 90): {top_students}")

# Example 2: Text processing
print("\nExample 2: Text processing")
text = "Python is a great programming language for beginners"
words = text.split()

# Word to length mapping for long words
long_word_lengths = {word: len(word) for word in words if len(word) > 4}
print(f"Long word lengths: {long_word_lengths}")

# Word to first letter mapping
word_first_letters = {word: word[0] for word in words}
print(f"Word first letters: {word_first_letters}")

# Example 3: Number processing
print("\nExample 3: Number processing")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Number to its properties
number_properties = {
    x: {
        "even": x % 2 == 0,
        "square": x**2,
        "prime": x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)),
    }
    for x in numbers
}
print(f"Number properties: {number_properties}")

# =============================================================================
# COMMON PATTERNS AND TRICKS
# =============================================================================
print("\n\n10. COMMON PATTERNS AND TRICKS")
print("-" * 35)

# Pattern 1: Inverting a dictionary
print("Pattern 1: Inverting a dictionary")
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Pattern 2: Grouping items
print("\nPattern 2: Grouping items")
items = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
    ("fruit", "orange"),
]
grouped = {}
for category, item in items:
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(item)
print(f"Grouped items: {grouped}")

# Pattern 3: Counting occurrences
print("\nPattern 3: Counting occurrences")
text = "hello world hello python world python"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word count: {word_count}")

# Pattern 4: Dictionary comprehension with function calls
print("\nPattern 4: Dictionary comprehension with function calls")


def square(x):
    return x**2


squares = {x: square(x) for x in range(1, 6)}
print(f"Squares using function: {squares}")

# =============================================================================
# DICTIONARY COMPREHENSIONS VS LIST COMPREHENSIONS
# =============================================================================
print("\n\n11. DICTIONARY COMPREHENSIONS VS LIST COMPREHENSIONS")
print("-" * 55)

# Same data, different structures
print("Same data, different structures:")
numbers = [1, 2, 3, 4, 5]

# List comprehension
squares_list = [x**2 for x in numbers]
print(f"List comprehension: {squares_list}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in numbers}
print(f"Dictionary comprehension: {squares_dict}")

# When to use which
print("\nWhen to use which:")
print("• Use list comprehension when you need an ordered sequence")
print("• Use dictionary comprehension when you need key-value pairs")
print("• Use dictionary comprehension when you need fast lookups")
print("• Use list comprehension when you need to iterate in order")

# =============================================================================
# PERFORMANCE CONSIDERATIONS
# =============================================================================
print("\n\n12. PERFORMANCE CONSIDERATIONS")
print("-" * 35)

# Dictionary comprehension vs traditional loop
print("Dictionary comprehension vs traditional loop:")
import time

# Test data
numbers = list(range(10000))

# Traditional loop
start_time = time.time()
result1 = {}
for x in numbers:
    if x % 2 == 0:
        result1[x] = x**2
traditional_time = time.time() - start_time

# Dictionary comprehension
start_time = time.time()
result2 = {x: x**2 for x in numbers if x % 2 == 0}
comprehension_time = time.time() - start_time

print(f"Traditional loop time: {traditional_time:.4f} seconds")
print(f"Dictionary comprehension time: {comprehension_time:.4f} seconds")
print(f"Dictionary comprehension is {traditional_time/comprehension_time:.1f}x faster!")

# =============================================================================
# WHEN TO USE DICTIONARY COMPREHENSIONS
# =============================================================================
print("\n\n13. WHEN TO USE DICTIONARY COMPREHENSIONS")
print("-" * 45)

print("✅ Use dictionary comprehensions when:")
print("• Creating a new dictionary from an existing iterable")
print("• The logic is simple and readable")
print("• You want to filter and/or transform key-value pairs")
print("• Performance is important")
print("• You need fast lookups by key")

print("\n❌ Avoid dictionary comprehensions when:")
print("• The logic is complex and hard to read")
print("• You need side effects (like printing)")
print("• You need to handle exceptions")
print("• The comprehension becomes too long")
print("• You need to maintain insertion order (use OrderedDict)")

# Example of when NOT to use
print("\nExample of when NOT to use:")
print("Complex logic - better to use traditional loop:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = {}
for x in numbers:
    if x % 2 == 0:
        if x > 5:
            result[x] = x**2
        else:
            result[x] = x
    else:
        result[x] = x * 2
print(f"Complex result: {result}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n14. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ Dictionary comprehensions are concise ways to create dictionaries")
print("✓ Basic syntax: {key_expression: value_expression for item in iterable}")
print("✓ Add conditions: {key: value for item in iterable if condition}")
print("✓ Can combine transformation and filtering")
print("✓ Support nested comprehensions for complex operations")
print("✓ Can use conditional expressions (ternary operator)")
print("✓ Generally faster than traditional loops")
print("✓ Use when logic is simple and readable")
print("✓ Avoid when logic becomes too complex")
print("✓ Great for creating lookup tables and mappings")
print("\nDictionary comprehensions make your code more Pythonic and efficient! 🐍✨")
