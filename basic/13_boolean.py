"""
13. Boolean Values in Python

Boolean values represent truth values: True and False.
In Python, many values can be evaluated as True or False in boolean context.
Understanding truthy and falsy values is crucial for effective programming.

BOOLEAN BASICS:
- True: Represents a true condition
- False: Represents a false condition
- bool(): Function to convert values to boolean
- All values have a "truthiness" - they evaluate to either True or False
"""

print("=" * 60)
print("BOOLEAN VALUES IN PYTHON")
print("=" * 60)

# =============================================================================
# 1. BASIC BOOLEAN VALUES
# =============================================================================
print("\n1. BASIC BOOLEAN VALUES")
print("-" * 30)

# Direct boolean values
is_python_fun = True
is_learning_hard = False

print(f"is_python_fun = {is_python_fun}")
print(f"is_learning_hard = {is_learning_hard}")
print(f"Type of True: {type(True)}")
print(f"Type of False: {type(False)}")

# Boolean operations
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")
print(f"not False = {not False}")

# =============================================================================
# 2. FALSY VALUES IN PYTHON
# =============================================================================
print("\n2. FALSY VALUES IN PYTHON")
print("-" * 30)
print("These values evaluate to False in boolean context:")

# None
print(f"bool(None) = {bool(None)}")

# False
print(f"bool(False) = {bool(False)}")

# Zero values
print(f"bool(0) = {bool(0)}")
print(f"bool(0.0) = {bool(0.0)}")
print(f"bool(0j) = {bool(0j)}")  # Complex zero

# Empty sequences
print(f"bool('') = {bool('')}")  # Empty string
print(f"bool([]) = {bool([])}")  # Empty list
print(f"bool(()) = {bool(())}")  # Empty tuple
print(f"bool({{}}) = {bool({})}")  # Empty dictionary
print(f"bool(set()) = {bool(set())}")  # Empty set

# range(0) - empty range
print(f"bool(range(0)) = {bool(range(0))}")

print("\nFALSY VALUES SUMMARY:")
falsy_values = [None, False, 0, 0.0, 0j, "", [], (), {}, set(), range(0)]

for value in falsy_values:
    print(f"  {repr(value):15} -> {bool(value)}")

# =============================================================================
# 3. TRUTHY VALUES IN PYTHON
# =============================================================================
print("\n3. TRUTHY VALUES IN PYTHON")
print("-" * 30)
print("These values evaluate to True in boolean context:")

# Non-zero numbers
print(f"bool(1) = {bool(1)}")
print(f"bool(-1) = {bool(-1)}")
print(f"bool(3.14) = {bool(3.14)}")
print(f"bool(-2.5) = {bool(-2.5)}")
print(f"bool(1+2j) = {bool(1+2j)}")

# Non-empty strings
print(f"bool('hello') = {bool('hello')}")
print(f"bool(' ') = {bool(' ')}")  # Even a space is truthy
print(f"bool('0') = {bool('0')}")  # String '0' is truthy (not the number 0)

# Non-empty sequences
print(f"bool([1, 2, 3]) = {bool([1, 2, 3])}")
print(f"bool((1,)) = {bool((1,))}")
print(f"bool({{'key': 'value'}}) = {bool({'key': 'value'})}")
print(f"bool({{1, 2, 3}}) = {bool({1, 2, 3})}")

# Non-empty ranges
print(f"bool(range(1)) = {bool(range(1))}")
print(f"bool(range(5)) = {bool(range(5))}")

print("\nTRUTHY VALUES EXAMPLES:")
truthy_values = [
    1,
    -1,
    3.14,
    -2.5,
    1 + 2j,
    "hello",
    " ",
    "0",
    [1],
    (1,),
    {"key": "value"},
    {1},
    range(1),
]

for value in truthy_values:
    print(f"  {repr(value):15} -> {bool(value)}")

# =============================================================================
# 4. BOOLEAN CONVERSION WITH bool()
# =============================================================================
print("\n4. BOOLEAN CONVERSION WITH bool()")
print("-" * 30)


def test_boolean_conversion(value, description):
    """Test boolean conversion of a value."""
    result = bool(value)
    print(f"bool({repr(value):15}) = {result:5} # {description}")


# Test various values
test_boolean_conversion(0, "Zero is falsy")
test_boolean_conversion(1, "Non-zero is truthy")
test_boolean_conversion(-1, "Negative numbers are truthy")
test_boolean_conversion(0.0, "Zero float is falsy")
test_boolean_conversion(0.1, "Non-zero float is truthy")

test_boolean_conversion("", "Empty string is falsy")
test_boolean_conversion("hello", "Non-empty string is truthy")
test_boolean_conversion(" ", "String with space is truthy")
test_boolean_conversion("0", "String '0' is truthy")

test_boolean_conversion([], "Empty list is falsy")
test_boolean_conversion([0], "List with falsy element is truthy")
test_boolean_conversion([False], "List with False is truthy")

test_boolean_conversion({}, "Empty dict is falsy")
test_boolean_conversion({False: True}, "Dict with falsy key is truthy")

test_boolean_conversion(None, "None is falsy")
test_boolean_conversion(False, "False is falsy")
test_boolean_conversion(True, "True is truthy")

# =============================================================================
# 5. PRACTICAL EXAMPLES OF TRUTHY/FALSY USAGE
# =============================================================================
print("\n5. PRACTICAL EXAMPLES OF TRUTHY/FALSY USAGE")
print("-" * 30)

# Example 1: Checking if a list has items
shopping_list = []
if shopping_list:
    print("You have items to buy")
else:
    print("Your shopping list is empty")

# Example 2: Checking if a string is not empty
user_input = input("Enter your name (or press Enter to skip): ")
if user_input:
    print(f"Hello, {user_input}!")
else:
    print("No name provided")


# Example 3: Default values using or operator
def get_username(user_data):
    """Get username with fallback."""
    return user_data.get("username") or "Guest"


user1 = {"username": "alice"}
user2 = {}
print(f"User1: {get_username(user1)}")
print(f"User2: {get_username(user2)}")

# Example 4: Counting non-empty items
data = [1, 0, "", "hello", None, [], [1, 2], False, True]
non_empty_count = sum(1 for item in data if item)
print(f"Non-empty items in {data}: {non_empty_count}")

# Example 5: Filtering truthy values
mixed_data = [0, 1, "", "hello", None, [], [1, 2], False, True]
truthy_only = [item for item in mixed_data if item]
print(f"Truthy values only: {truthy_only}")

# =============================================================================
# 6. BOOLEAN OPERATIONS WITH TRUTHY/FALSY VALUES
# =============================================================================
print("\n6. BOOLEAN OPERATIONS WITH TRUTHY/FALSY VALUES")
print("-" * 30)

# AND operation - returns first falsy value or last truthy value
print("AND operation examples:")
print(f"0 and 5 = {0 and 5}")  # Returns 0 (first falsy)
print(f"3 and 5 = {3 and 5}")  # Returns 5 (last truthy)
print(f"'' and 'hello' = {repr('' and 'hello')}")  # Returns '' (first falsy)
print(
    f"'hello' and 'world' = {repr('hello' and 'world')}"
)  # Returns 'world' (last truthy)

# OR operation - returns first truthy value or last falsy value
print("\nOR operation examples:")
print(f"0 or 5 = {0 or 5}")  # Returns 5 (first truthy)
print(f"3 or 5 = {3 or 5}")  # Returns 3 (first truthy)
print(f"'' or 'hello' = {repr('' or 'hello')}")  # Returns 'hello' (first truthy)
print(
    f"'hello' or 'world' = {repr('hello' or 'world')}"
)  # Returns 'hello' (first truthy)
print(f"0 or '' or None = {repr(0 or '' or None)}")  # Returns None (last falsy)

# NOT operation - always returns boolean
print("\nNOT operation examples:")
print(f"not 0 = {not 0}")  # True
print(f"not 1 = {not 1}")  # False
print(f"not '' = {not ''}")  # True
print(f"not 'hello' = {not 'hello'}")  # False
print(f"not [] = {not []}")  # True
print(f"not [1] = {not [1]}")  # False

# =============================================================================
# 7. COMMON PATTERNS USING TRUTHY/FALSY VALUES
# =============================================================================
print("\n7. COMMON PATTERNS USING TRUTHY/FALSY VALUES")
print("-" * 30)


# Pattern 1: Default values
def process_data(data=None):
    """Process data with default empty list."""
    data = data or []  # If data is falsy, use empty list
    return f"Processing {len(data)} items"


print(process_data([1, 2, 3]))
print(process_data(None))
print(process_data([]))


# Pattern 2: Conditional execution
def log_message(message, level="INFO"):
    """Log message if message is not empty."""
    if message:  # Only log if message is truthy
        print(f"[{level}] {message}")


log_message("This will be logged")
log_message("")  # This won't be logged
log_message("   ")  # This will be logged (space is truthy)


# Pattern 3: Validation
def validate_user(user):
    """Validate user data."""
    if not user.get("name"):
        return "Name is required"
    if not user.get("email"):
        return "Email is required"
    if not user.get("age"):
        return "Age is required"
    return "User is valid"


# Test validation
test_users = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "", "email": "bob@example.com", "age": 30},
    {"name": "Charlie", "email": "", "age": 35},
    {"name": "Diana", "email": "diana@example.com", "age": 0},
]

for user in test_users:
    result = validate_user(user)
    print(f"User {user}: {result}")


# Pattern 4: Short-circuit evaluation for safety
def safe_divide(a, b):
    """Safely divide two numbers."""
    return b and a / b  # If b is falsy (0), return b (0), otherwise divide


print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")

# =============================================================================
# 8. BOOLEAN FUNCTIONS AND METHODS
# =============================================================================
print("\n8. BOOLEAN FUNCTIONS AND METHODS")
print("-" * 30)

# any() - returns True if any element is truthy
print("any() function examples:")
print(f"any([False, False, False]) = {any([False, False, False])}")
print(f"any([False, True, False]) = {any([False, True, False])}")
print(f"any([0, 0, 0]) = {any([0, 0, 0])}")
print(f"any([0, 1, 0]) = {any([0, 1, 0])}")
print(f"any([]) = {any([])}")  # Empty iterable is False

# all() - returns True if all elements are truthy
print("\nall() function examples:")
print(f"all([True, True, True]) = {all([True, True, True])}")
print(f"all([True, False, True]) = {all([True, False, True])}")
print(f"all([1, 2, 3]) = {all([1, 2, 3])}")
print(f"all([1, 0, 3]) = {all([1, 0, 3])}")
print(f"all([]) = {all([])}")  # Empty iterable is True


# Practical use of any() and all()
def check_requirements(age, has_license, has_insurance):
    """Check if all requirements are met."""
    requirements = [age >= 18, has_license, has_insurance]
    return all(requirements)


def has_any_qualification(education, experience, certification):
    """Check if person has any qualification."""
    qualifications = [education, experience, certification]
    return any(qualifications)


# Test the functions
print(f"Can drive: {check_requirements(20, True, True)}")
print(f"Can drive: {check_requirements(16, True, True)}")
print(f"Has qualification: {has_any_qualification(False, True, False)}")
print(f"Has qualification: {has_any_qualification(False, False, False)}")

# =============================================================================
# 9. ADVANCED BOOLEAN CONCEPTS
# =============================================================================
print("\n9. ADVANCED BOOLEAN CONCEPTS")
print("-" * 30)

# Boolean arithmetic (True = 1, False = 0)
print("Boolean arithmetic:")
print(f"True + True = {True + True}")
print(f"True + False = {True + False}")
print(f"False + False = {False + False}")
print(f"True * 5 = {True * 5}")
print(f"False * 5 = {False * 5}")


# Using boolean in conditions
def count_truthy_values(data):
    """Count how many truthy values are in the data."""
    return sum(bool(item) for item in data)


test_data = [1, 0, "", "hello", None, [], [1, 2], False, True]
print(f"Truthy count in {test_data}: {count_truthy_values(test_data)}")

# Boolean indexing
import random

numbers = [random.randint(0, 10) for _ in range(10)]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

# =============================================================================
# 10. COMMON MISTAKES AND BEST PRACTICES
# =============================================================================
print("\n10. COMMON MISTAKES AND BEST PRACTICES")
print("-" * 30)


# Mistake 1: Comparing with == True/False unnecessarily
def is_even_bad(number):
    """Bad way to check if number is even."""
    return number % 2 == 0 == True  # Unnecessary comparison


def is_even_good(number):
    """Good way to check if number is even."""
    return number % 2 == 0  # Direct boolean result


print(f"is_even_bad(4): {is_even_bad(4)}")
print(f"is_even_good(4): {is_even_good(4)}")


# Mistake 2: Using == instead of is for None
def check_none_bad(value):
    """Bad way to check for None."""
    return value == None  # Should use 'is'


def check_none_good(value):
    """Good way to check for None."""
    return value is None  # Correct way


print(f"check_none_bad(None): {check_none_bad(None)}")
print(f"check_none_good(None): {check_none_good(None)}")


# Best practice: Use truthy/falsy for simple checks
def process_list_bad(items):
    """Less Pythonic way."""
    if len(items) > 0:
        return f"Processing {len(items)} items"
    else:
        return "No items to process"


def process_list_good(items):
    """More Pythonic way."""
    if items:  # Direct truthy check
        return f"Processing {len(items)} items"
    else:
        return "No items to process"


test_lists = [[1, 2, 3], [], [0]]
for lst in test_lists:
    print(f"Bad: {process_list_bad(lst)}")
    print(f"Good: {process_list_good(lst)}")

print("\n" + "=" * 60)
print("SUMMARY OF BOOLEAN VALUES IN PYTHON")
print("=" * 60)
print("FALSY VALUES:")
print("  - None")
print("  - False")
print("  - Zero: 0, 0.0, 0j")
print("  - Empty sequences: '', [], (), {{}}, set()")
print("  - range(0)")
print()
print("TRUTHY VALUES:")
print("  - Everything else!")
print("  - Non-zero numbers: 1, -1, 3.14, etc.")
print("  - Non-empty strings: 'hello', ' ', '0'")
print("  - Non-empty sequences: [1], (1,), {{'key': 'value'}}, {{1}}")
print("  - Non-empty ranges: range(1), range(5)")
print()
print("KEY FUNCTIONS:")
print("  - bool(value): Convert to boolean")
print("  - any(iterable): True if any element is truthy")
print("  - all(iterable): True if all elements are truthy")
print()
print("BEST PRACTICES:")
print("  - Use truthy/falsy checks: if items: instead of if len(items) > 0:")
print("  - Use 'is None' instead of '== None'")
print("  - Use 'or' for default values: value or default")
print("  - Use 'and' for conditional execution: condition and action()")
print("\nExperiment with these examples to understand boolean behavior!")
