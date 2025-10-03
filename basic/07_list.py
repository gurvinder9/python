"""
Python Basics - Lists
This file demonstrates how lists work in Python.
Lists are ordered collections of items that can be modified.
"""

print("=== Python Lists Tutorial ===\n")

# =============================================================================
# WHAT ARE LISTS?
# =============================================================================
print("1. WHAT ARE LISTS?")
print("-" * 20)

print("Lists are ordered collections of items.")
print("Think of them like a shopping list:")
print("- Items are in a specific order")
print("- You can add, remove, or change items")
print("- Items can be of different data types")
print("- Lists are mutable (can be changed)")
print("- Lists can contain duplicates\n")

# =============================================================================
# CREATING LISTS
# =============================================================================
print("2. CREATING LISTS")
print("-" * 20)

# Method 1: Using square brackets []
print("Method 1: Using square brackets []")
fruits = ["apple", "banana", "orange", "grape"]
print(f"Fruits list: {fruits}")

# Method 2: Using list() constructor
print("\nMethod 2: Using list() constructor")
numbers = list([1, 2, 3, 4, 5])
print(f"Numbers list: {numbers}")

# Method 3: Empty list
print("\nMethod 3: Empty list")
empty_list = []
print(f"Empty list: {empty_list}")

# Method 4: List with different data types
print("\nMethod 4: List with mixed data types")
mixed_list = ["Hello", 42, 3.14, True, [1, 2, 3]]
print(f"Mixed list: {mixed_list}")

# Method 5: List from string
print("\nMethod 5: List from string")
word_list = list("Python")
print(f"Word as list: {word_list}")

# Method 6: List from range
print("\nMethod 6: List from range")
range_list = list(range(1, 6))
print(f"Range list: {range_list}")

# =============================================================================
# ACCESSING LIST ELEMENTS
# =============================================================================
print("\n\n3. ACCESSING LIST ELEMENTS")
print("-" * 30)

# Accessing elements by index
print("Accessing elements by index:")
print(f"fruits[0]: {fruits[0]}")  # First element
print(f"fruits[1]: {fruits[1]}")  # Second element
print(f"fruits[-1]: {fruits[-1]}")  # Last element
print(f"fruits[-2]: {fruits[-2]}")  # Second to last element

# Accessing nested lists
print("\nAccessing nested lists:")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Nested list: {nested_list}")
print(f"nested_list[0]: {nested_list[0]}")
print(f"nested_list[0][1]: {nested_list[0][1]}")

# Slicing lists
print("\nSlicing lists:")
print(f"fruits[1:3]: {fruits[1:3]}")  # Elements from index 1 to 2
print(f"fruits[:2]: {fruits[:2]}")  # First 2 elements
print(f"fruits[2:]: {fruits[2:]}")  # From index 2 to end
print(f"fruits[:]: {fruits[:]}")  # All elements (copy)
print(f"fruits[::2]: {fruits[::2]}")  # Every 2nd element

# =============================================================================
# MODIFYING LISTS
# =============================================================================
print("\n\n4. MODIFYING LISTS")
print("-" * 20)

# Modifying elements by index
print("Modifying elements by index:")
fruits[1] = "blueberry"
print(f"After changing index 1: {fruits}")

# Adding elements
print("\nAdding elements:")
fruits.append("strawberry")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "mango")  # Insert at specific position
print(f"After insert: {fruits}")

# Removing elements
print("\nRemoving elements:")
removed = fruits.pop()  # Remove last element
print(f"Removed: {removed}")
print(f"After pop(): {fruits}")

fruits.remove("orange")  # Remove specific element
print(f"After remove('orange'): {fruits}")

# =============================================================================
# LIST OPERATIONS
# =============================================================================
print("\n\n5. LIST OPERATIONS")
print("-" * 20)

# Concatenation
print("Concatenation:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"list1 + list2: {combined}")

# Repetition
print("\nRepetition:")
repeated = [1, 2] * 3
print(f"[1, 2] * 3: {repeated}")

# Length
print(f"\nLength:")
print(f"len(fruits): {len(fruits)}")

# Membership testing
print(f"\nMembership testing:")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'kiwi' in fruits: {'kiwi' in fruits}")
print(f"'kiwi' not in fruits: {'kiwi' not in fruits}")

# =============================================================================
# ITERATING THROUGH LISTS
# =============================================================================
print("\n\n6. ITERATING THROUGH LISTS")
print("-" * 30)

# Basic iteration
print("Basic iteration:")
for fruit in fruits:
    print(f"  {fruit}")

# Iteration with index
print("\nIteration with index:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# Iteration with range
print("\nIteration with range:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

# List comprehension (preview)
print("\nList comprehension (preview):")
squared = [x**2 for x in range(1, 6)]
print(f"Squared numbers: {squared}")

# =============================================================================
# LIST COMPARISON AND SORTING
# =============================================================================
print("\n\n7. LIST COMPARISON AND SORTING")
print("-" * 35)

# Sorting
print("Sorting:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

sorted_numbers = sorted(numbers)  # Returns new sorted list
print(f"sorted(): {sorted_numbers}")
print(f"Original after sorted(): {numbers}")

numbers.sort()  # Sorts in place
print(f"After sort(): {numbers}")

# Reverse sorting
print("\nReverse sorting:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(f"Sort reverse: {numbers}")

# Reversing
print("\nReversing:")
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"After reverse(): {numbers}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n\n8. PRACTICAL EXAMPLES")
print("-" * 25)

# Example 1: Shopping list
print("Example 1: Shopping list")
shopping_list = ["milk", "bread", "eggs", "butter"]
print(f"Shopping list: {shopping_list}")

# Add items
shopping_list.append("cheese")
shopping_list.insert(1, "apples")
print(f"After adding items: {shopping_list}")

# Check off items (remove)
shopping_list.remove("milk")
print(f"After buying milk: {shopping_list}")

# Example 2: Student grades
print("\nExample 2: Student grades")
grades = [85, 92, 78, 96, 88]
print(f"Grades: {grades}")

# Calculate average
average = sum(grades) / len(grades)
print(f"Average grade: {average:.1f}")

# Find highest and lowest
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")

# Example 3: Temperature tracking
print("\nExample 3: Temperature tracking")
temperatures = [72, 75, 78, 80, 77, 73, 76]
print(f"Temperatures: {temperatures}")

# Find days above average
avg_temp = sum(temperatures) / len(temperatures)
hot_days = [temp for temp in temperatures if temp > avg_temp]
print(f"Average temperature: {avg_temp:.1f}")
print(f"Hot days (above average): {hot_days}")

# Example 4: Word processing
print("\nExample 4: Word processing")
sentence = "Python is a great programming language"
words = sentence.split()
print(f"Sentence: {sentence}")
print(f"Words: {words}")
print(f"Number of words: {len(words)}")
print(f"Longest word: {max(words, key=len)}")

# =============================================================================
# COMMON LIST PATTERNS
# =============================================================================
print("\n\n9. COMMON LIST PATTERNS")
print("-" * 30)

# Pattern 1: Building a list
print("Pattern 1: Building a list")
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(f"Squares: {squares}")

# Pattern 2: Filtering a list
print("\nPattern 2: Filtering a list")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# Pattern 3: Finding elements
print("\nPattern 3: Finding elements")
fruits = ["apple", "banana", "orange", "grape", "apple"]
# Find first occurrence
first_apple = fruits.index("apple")
print(f"First 'apple' at index: {first_apple}")

# Count occurrences
apple_count = fruits.count("apple")
print(f"Number of 'apple': {apple_count}")

# Pattern 4: List as stack (LIFO)
print("\nPattern 4: List as stack (LIFO)")
stack = []
stack.append(1)  # Push
stack.append(2)  # Push
stack.append(3)  # Push
print(f"Stack after pushes: {stack}")

popped = stack.pop()  # Pop
print(f"Popped: {popped}")
print(f"Stack after pop: {stack}")

# Pattern 5: List as queue (FIFO)
print("\nPattern 5: List as queue (FIFO)")
from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)  # Enqueue
queue.append(3)  # Enqueue
print(f"Queue after enqueues: {list(queue)}")

dequeued = queue.popleft()  # Dequeue
print(f"Dequeued: {dequeued}")
print(f"Queue after dequeue: {list(queue)}")

# =============================================================================
# LIST COPYING AND REFERENCES
# =============================================================================
print("\n\n10. LIST COPYING AND REFERENCES")
print("-" * 35)

# Shallow copy
print("Shallow copy:")
original = [1, 2, 3, [4, 5]]
shallow_copy = original.copy()
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# Modify nested list
original[3][0] = 99
print(f"After modifying nested list:")
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# Deep copy
print("\nDeep copy:")
import copy

original = [1, 2, 3, [4, 5]]
deep_copy = copy.deepcopy(original)
original[3][0] = 99
print(f"After modifying nested list:")
print(f"Original: {original}")
print(f"Deep copy: {deep_copy}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n11. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ Lists are ordered, mutable collections")
print("✓ Access elements using index (positive or negative)")
print("✓ Use slicing to get sublists")
print("✓ Lists can contain different data types")
print("✓ Use append() to add to end, insert() to add at position")
print("✓ Use pop() to remove from end, remove() to remove specific value")
print("✓ Use len() to get length, in/not in for membership")
print("✓ Use sort() to sort in place, sorted() to get new sorted list")
print("✓ Lists support concatenation (+) and repetition (*)")
print("✓ Be careful with copying - use copy() or deepcopy() for nested lists")
print("\nLists are versatile and powerful data structures! 📋")
