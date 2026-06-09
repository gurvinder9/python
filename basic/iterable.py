"""
Iterables in Python
===================

An iterable is any Python object capable of returning its members one at a time,
permitting it to be iterated over in a for-loop.

Key Concepts:
- An iterable is an object that implements the __iter__() method
- The __iter__() method returns an iterator object
- An iterator implements the __next__() method
- Common iterables: lists, tuples, strings, dictionaries, sets, files, generators

When to use:
- When you need to process elements one at a time
- When working with large datasets (memory efficient)
- When you want to create custom iteration behavior
- When using for loops, list comprehensions, or unpacking
"""

# ============================================
# 1. BUILT-IN ITERABLES
# ============================================

print("=" * 50)
print("1. BUILT-IN ITERABLES")
print("=" * 50)

# Lists are iterables
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(f"List item: {item}")

print()

# Strings are iterables
my_string = "Hello"
for char in my_string:
    print(f"Character: {char}")

print()

# Tuples are iterables
my_tuple = (10, 20, 30)
for item in my_tuple:
    print(f"Tuple item: {item}")

print()

# Dictionaries are iterables (iterate over keys by default)
my_dict = {"name": "Alice", "age": 30, "city": "NYC"}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

print()

# Sets are iterables
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(f"Set item: {item}")

print()

# ============================================
# 2. ITERABLES vs ITERATORS
# ============================================

print("=" * 50)
print("2. ITERABLES vs ITERATORS")
print("=" * 50)

# An iterable is an object that can return an iterator
my_list = [1, 2, 3]
print(f"Is my_list iterable? {hasattr(my_list, '__iter__')}")

# Getting an iterator from an iterable
my_iterator = iter(my_list)
print(f"Iterator object: {my_iterator}")

# Using next() to get items from iterator
print(f"First item: {next(my_iterator)}")
print(f"Second item: {next(my_iterator)}")
print(f"Third item: {next(my_iterator)}")

# Next call would raise StopIteration exception
try:
    print(next(my_iterator))
except StopIteration:
    print("No more items in iterator!")

print()

# ============================================
# 3. CREATING CUSTOM ITERABLES
# ============================================

print("=" * 50)
print("3. CREATING CUSTOM ITERABLES")
print("=" * 50)


class CountDown:
    """Custom iterable that counts down from a number"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """Returns an iterator object"""
        self.current = self.start
        return self

    def __next__(self):
        """Returns the next item"""
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


# Using the custom iterable
countdown = CountDown(5)
for num in countdown:
    print(f"Countdown: {num}")

print()


class EvenNumbers:
    """Custom iterable that generates even numbers up to a limit"""

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


evens = EvenNumbers(10)
for num in evens:
    print(f"Even number: {num}")

print()

# ============================================
# 4. GENERATOR FUNCTIONS (Easy way to create iterables)
# ============================================

print("=" * 50)
print("4. GENERATOR FUNCTIONS")
print("=" * 50)


def count_up_to(n):
    """Generator function that yields numbers up to n"""
    count = 1
    while count <= n:
        yield count
        count += 1


# Generators are iterables
counter = count_up_to(5)
for num in counter:
    print(f"Count: {num}")

print()


def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print("Fibonacci sequence:")
for num in fibonacci(10):
    print(num, end=" ")
print("\n")

# ============================================
# 5. GENERATOR EXPRESSIONS
# ============================================

print("=" * 50)
print("5. GENERATOR EXPRESSIONS")
print("=" * 50)

# Generator expressions are like list comprehensions but lazy
# They don't create the entire list in memory

# List comprehension (creates entire list)
squares_list = [x**2 for x in range(10)]
print(f"List comprehension: {squares_list}")
print(f"Type: {type(squares_list)}")

# Generator expression (creates items on demand)
squares_gen = (x**2 for x in range(10))
print(f"Generator expression: {squares_gen}")
print(f"Type: {type(squares_gen)}")

# Iterating over generator
print("Generator values:")
for square in squares_gen:
    print(square, end=" ")
print("\n")

# ============================================
# 6. PRACTICAL USE CASES
# ============================================

print("=" * 50)
print("6. PRACTICAL USE CASES")
print("=" * 50)


# Use Case 1: Reading large files (memory efficient)
def read_large_file(file_path):
    """Generator to read large files line by line"""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


# Use Case 2: Infinite sequences
def infinite_sequence():
    """Generator for infinite sequence"""
    num = 0
    while True:
        yield num
        num += 1


# Getting first 10 numbers from infinite sequence
print("First 10 numbers from infinite sequence:")
gen = infinite_sequence()
for _ in range(10):
    print(next(gen), end=" ")
print("\n")


# Use Case 3: Pipeline processing
def get_numbers():
    """Generate numbers"""
    for i in range(1, 11):
        yield i


def square_numbers(numbers):
    """Square each number"""
    for num in numbers:
        yield num**2


def filter_even(numbers):
    """Filter even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num


# Chaining generators
print("Pipeline processing:")
pipeline = filter_even(square_numbers(get_numbers()))
for result in pipeline:
    print(result, end=" ")
print("\n")

# ============================================
# 7. BUILT-IN FUNCTIONS THAT WORK WITH ITERABLES
# ============================================

print("=" * 50)
print("7. BUILT-IN FUNCTIONS WITH ITERABLES")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

# map() - returns an iterator
squared = map(lambda x: x**2, numbers)
print(f"map() result: {list(squared)}")

# filter() - returns an iterator
evens = filter(lambda x: x % 2 == 0, numbers)
print(f"filter() result: {list(evens)}")

# zip() - returns an iterator
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = zip(names, ages)
print(f"zip() result: {list(combined)}")

# enumerate() - returns an iterator
fruits = ["apple", "banana", "cherry"]
indexed = enumerate(fruits)
print(f"enumerate() result: {list(indexed)}")

# sum(), min(), max() - work with iterables
print(f"sum: {sum(numbers)}")
print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")

# any() and all() - work with iterables
print(f"any() - at least one True: {any([False, False, True])}")
print(f"all() - all True: {all([True, True, True])}")

print()

# ============================================
# 8. CHECKING IF OBJECT IS ITERABLE
# ============================================

print("=" * 50)
print("8. CHECKING IF OBJECT IS ITERABLE")
print("=" * 50)

from collections.abc import Iterable


def is_iterable(obj):
    """Check if object is iterable"""
    return isinstance(obj, Iterable)


print(f"Is [1,2,3] iterable? {is_iterable([1, 2, 3])}")
print(f"Is 'hello' iterable? {is_iterable('hello')}")
print(f"Is 123 iterable? {is_iterable(123)}")
print(f"Is {{'a': 1}} iterable? {is_iterable({'a': 1})}")

print()

# ============================================
# 9. ITERTOOLS MODULE - POWERFUL ITERATORS
# ============================================

print("=" * 50)
print("9. ITERTOOLS MODULE")
print("=" * 50)

import itertools

# count() - infinite counter
print("count():")
counter = itertools.count(start=10, step=2)
for _ in range(5):
    print(next(counter), end=" ")
print("\n")

# cycle() - infinite cycling through iterable
print("cycle():")
colors = itertools.cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors), end=" ")
print("\n")

# repeat() - repeat an element
print("repeat():")
repeated = itertools.repeat("Hello", 3)
print(list(repeated))

# chain() - chain multiple iterables
print("chain():")
chained = itertools.chain([1, 2], [3, 4], [5, 6])
print(list(chained))

# islice() - slice an iterator
print("islice():")
numbers = itertools.count()
sliced = itertools.islice(numbers, 5, 10)
print(list(sliced))

print()

# ============================================
# 10. PERFORMANCE BENEFITS
# ============================================

print("=" * 50)
print("10. PERFORMANCE BENEFITS")
print("=" * 50)

import sys

# Memory comparison
list_comp = [x for x in range(1000)]
gen_exp = (x for x in range(1000))

print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")
print(f"Generator expression size: {sys.getsizeof(gen_exp)} bytes")
print(f"Generator is {sys.getsizeof(list_comp) / sys.getsizeof(gen_exp):.2f}x smaller!")

print()
print("Key Takeaway: Generators are memory efficient for large datasets!")

"""
SUMMARY
=======

When to use Iterables:
1. Processing large datasets (memory efficient with generators)
2. When you need lazy evaluation (compute on demand)
3. Creating infinite sequences
4. Building data processing pipelines
5. When using for loops, comprehensions, or unpacking
6. File processing (reading line by line)
7. Working with streams of data

Best Practices:
- Use generators for large datasets
- Use list comprehensions for small datasets that fit in memory
- Create custom iterables for domain-specific iteration patterns
- Use itertools for complex iteration patterns
- Remember: all iterators are iterables, but not all iterables are iterators

Benefits:
- Memory efficiency
- Lazy evaluation
- Clean, readable code
- Composability (chaining operations)
- Works seamlessly with Python's iteration protocol
"""
