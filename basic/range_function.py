"""
The range() Function in Python
==============================

The range() function is a built-in function that generates a sequence of numbers.
It's commonly used in for loops and when you need to create a sequence of integers.

Key Points:
- range() returns a range object (which is an iterable)
- It doesn't store all values in memory (memory efficient)
- It generates values on-demand (lazy evaluation)
- It's immutable (cannot be modified after creation)

Syntax:
- range(stop)                    # 0 to stop-1
- range(start, stop)             # start to stop-1
- range(start, stop, step)       # start to stop-1 with step size
"""

# ============================================
# 1. BASIC RANGE SYNTAX
# ============================================

print("=" * 50)
print("1. BASIC RANGE SYNTAX")
print("=" * 50)

# range(stop) - generates numbers from 0 to stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")

# range(start, stop) - generates numbers from start to stop-1
print("range(2, 8):")
for i in range(2, 8):
    print(i, end=" ")
print("\n")

# range(start, stop, step) - generates numbers with step size
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

# Negative step (counting backwards)
print("range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

print()

# ============================================
# 2. RANGE OBJECT PROPERTIES
# ============================================

print("=" * 50)
print("2. RANGE OBJECT PROPERTIES")
print("=" * 50)

# Creating range objects
r1 = range(5)
r2 = range(1, 10)
r3 = range(0, 20, 3)

print(f"range(5): {r1}")
print(f"Type: {type(r1)}")
print(f"Start: {r1.start}")
print(f"Stop: {r1.stop}")
print(f"Step: {r1.step}")
print()

print(f"range(1, 10): {r2}")
print(f"Start: {r2.start}")
print(f"Stop: {r2.stop}")
print(f"Step: {r2.step}")
print()

print(f"range(0, 20, 3): {r3}")
print(f"Start: {r3.start}")
print(f"Stop: {r3.stop}")
print(f"Step: {r3.step}")
print()

# ============================================
# 3. CONVERTING RANGE TO OTHER DATA TYPES
# ============================================

print("=" * 50)
print("3. CONVERTING RANGE TO OTHER DATA TYPES")
print("=" * 50)

# Convert to list
numbers_list = list(range(5))
print(f"list(range(5)): {numbers_list}")

# Convert to tuple
numbers_tuple = tuple(range(1, 6))
print(f"tuple(range(1, 6)): {numbers_tuple}")

# Convert to set
numbers_set = set(range(0, 10, 2))
print(f"set(range(0, 10, 2)): {numbers_set}")

print()

# ============================================
# 4. COMMON USE CASES
# ============================================

print("=" * 50)
print("4. COMMON USE CASES")
print("=" * 50)

# Use Case 1: Simple counting
print("Counting 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

print()

# Use Case 2: Iterating through list indices
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits with indices:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

print()

# Use Case 3: Creating patterns
print("Creating a pattern:")
for i in range(5):
    print("*" * (i + 1))

print()

# Use Case 4: Reverse iteration
print("Reverse counting:")
for i in range(5, 0, -1):
    print(f"Countdown: {i}")

print()

# Use Case 5: Even/odd numbers
print("Even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print("\n")

print("Odd numbers from 1 to 10:")
for i in range(1, 11, 2):
    print(i, end=" ")
print("\n")

# ============================================
# 5. ADVANCED RANGE OPERATIONS
# ============================================

print("=" * 50)
print("5. ADVANCED RANGE OPERATIONS")
print("=" * 50)

# Checking if a number is in range
r = range(1, 10)
print(f"Is 5 in range(1, 10)? {5 in r}")
print(f"Is 15 in range(1, 10)? {15 in r}")

# Getting the length of a range
print(f"Length of range(1, 10): {len(r)}")

# Getting the minimum and maximum
print(f"Min of range(1, 10): {min(r)}")
print(f"Max of range(1, 10): {max(r)}")

# Indexing and slicing
print(f"First element: {r[0]}")
print(f"Last element: {r[-1]}")
print(f"First 3 elements: {r[:3]}")

print()

# ============================================
# 6. RANGE WITH NEGATIVE NUMBERS
# ============================================

print("=" * 50)
print("6. RANGE WITH NEGATIVE NUMBERS")
print("=" * 50)

# Negative start
print("range(-5, 0):")
for i in range(-5, 0):
    print(i, end=" ")
print("\n")

# Negative step
print("range(10, 0, -2):")
for i in range(10, 0, -2):
    print(i, end=" ")
print("\n")

# All negative
print("range(-10, -1, 2):")
for i in range(-10, -1, 2):
    print(i, end=" ")
print("\n")

print()

# ============================================
# 7. RANGE IN LIST COMPREHENSIONS
# ============================================

print("=" * 50)
print("7. RANGE IN LIST COMPREHENSIONS")
print("=" * 50)

# Creating lists with range
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Creating even numbers
evens = [x for x in range(0, 11, 2)]
print(f"Even numbers: {evens}")

# Creating multiplication table
table_5 = [5 * x for x in range(1, 11)]
print(f"5 times table: {table_5}")

# Creating pairs
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"Pairs: {pairs}")

print()

# ============================================
# 8. RANGE vs OTHER METHODS
# ============================================

print("=" * 50)
print("8. RANGE vs OTHER METHODS")
print("=" * 50)

import sys

# Memory comparison
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_range = range(10)

print(f"List size: {sys.getsizeof(numbers_list)} bytes")
print(f"Range size: {sys.getsizeof(numbers_range)} bytes")
print(
    f"Range is {sys.getsizeof(numbers_list) / sys.getsizeof(numbers_range):.1f}x more memory efficient!"
)

print()

# Performance comparison
import time

# Using list
start_time = time.time()
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    pass
list_time = time.time() - start_time

# Using range
start_time = time.time()
for i in range(10):
    pass
range_time = time.time() - start_time

print(f"List iteration time: {list_time:.6f} seconds")
print(f"Range iteration time: {range_time:.6f} seconds")

print()

# ============================================
# 9. PRACTICAL EXAMPLES
# ============================================

print("=" * 50)
print("9. PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Creating a simple timer
print("Simple countdown timer:")
for i in range(5, 0, -1):
    print(f"Time remaining: {i} seconds")
print("Time's up!")

print()

# Example 2: Creating a multiplication table
print("Multiplication table for 7:")
for i in range(1, 11):
    print(f"7 × {i:2d} = {7 * i:2d}")

print()

# Example 3: Processing data in chunks
data = list(range(20))  # Sample data
chunk_size = 5

print("Processing data in chunks:")
for i in range(0, len(data), chunk_size):
    chunk = data[i : i + chunk_size]
    print(f"Chunk {i//chunk_size + 1}: {chunk}")

print()

# Example 4: Creating a grid
print("Creating a 3x3 grid:")
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row

print()


# Example 5: Fibonacci sequence using range
def fibonacci_with_range(n):
    """Generate Fibonacci sequence using range"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


print("First 10 Fibonacci numbers:")
fib_sequence = fibonacci_with_range(10)
for i, num in enumerate(fib_sequence):
    print(f"F({i}) = {num}")

print()

# ============================================
# 10. COMMON MISTAKES AND TIPS
# ============================================

print("=" * 50)
print("10. COMMON MISTAKES AND TIPS")
print("=" * 50)

# Mistake 1: Forgetting that range is exclusive of stop
print("Mistake: range(5) gives 0,1,2,3,4 (not 5)")
print("Correct: range(6) gives 0,1,2,3,4,5")

# Mistake 2: Using range with floats (doesn't work)
try:
    # This will cause a TypeError
    # for i in range(1.5, 5.5):
    #     print(i)
    print("range() only works with integers, not floats")
except TypeError as e:
    print(f"Error: {e}")

# Tip 1: Use range with enumerate for index and value
print("\nUsing range with enumerate:")
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Tip 2: Use range for creating empty loops
print("\nEmpty loop with range:")
for _ in range(3):
    print("Hello!")

# Tip 3: Use range for creating sequences of specific length
print("\nCreating sequences:")
zeros = [0] * 5  # [0, 0, 0, 0, 0]
ones = [1 for _ in range(5)]  # [1, 1, 1, 1, 1]
print(f"Zeros: {zeros}")
print(f"Ones: {ones}")

print()

# ============================================
# 11. RANGE WITH OTHER BUILT-IN FUNCTIONS
# ============================================

print("=" * 50)
print("11. RANGE WITH OTHER BUILT-IN FUNCTIONS")
print("=" * 50)

# sum() with range
total = sum(range(1, 11))
print(f"Sum of 1 to 10: {total}")

# min() and max() with range
r = range(5, 15, 2)
print(f"Min: {min(r)}, Max: {max(r)}")

# sorted() with range (though range is already sorted)
r = range(10, 0, -1)
print(f"Reversed range: {list(r)}")
print(f"Sorted: {sorted(r)}")

# any() and all() with range
print(f"Any number > 5 in range(1, 10)? {any(x > 5 for x in range(1, 10))}")
print(f"All numbers > 0 in range(1, 10)? {all(x > 0 for x in range(1, 10))}")

print()

"""
SUMMARY
=======

Key Points about range():
1. Syntax: range(stop), range(start, stop), range(start, stop, step)
2. Returns a range object (iterable, not a list)
3. Memory efficient - doesn't store all values
4. Works only with integers
5. Stop value is exclusive (not included)
6. Default start is 0, default step is 1

When to use range():
- For loops with specific number of iterations
- Creating sequences of numbers
- List comprehensions
- When you need memory efficiency
- Working with indices
- Creating patterns or grids

When NOT to use range():
- When you need floating point numbers (use numpy.arange)
- When you need to modify the sequence (use list)
- When you need random numbers (use random module)

Performance Benefits:
- Memory efficient for large ranges
- Fast iteration
- Lazy evaluation
- Immutable and thread-safe
"""

print("=" * 50)
print("END OF RANGE() FUNCTION EXPLANATION")
print("=" * 50)
