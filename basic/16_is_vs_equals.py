"""
16. 'is' vs '==' in Python

Understanding the difference between 'is' and '==' is crucial in Python.
These operators serve different purposes and are often confused by beginners.

KEY DIFFERENCES:
- 'is' checks for IDENTITY (same object in memory)
- '==' checks for EQUALITY (same value/content)

IDENTITY vs EQUALITY:
- Identity: Two variables refer to the same object
- Equality: Two objects have the same value/content
"""

print("=" * 60)
print("'is' vs '==' IN PYTHON")
print("=" * 60)

# =============================================================================
# 1. BASIC CONCEPT AND DIFFERENCE
# =============================================================================
print("\n1. BASIC CONCEPT AND DIFFERENCE")
print("-" * 30)

print("'is' OPERATOR:")
print("- Checks if two variables refer to the SAME OBJECT in memory")
print("- Returns True only if both variables point to the same memory location")
print("- Also called 'identity operator'")

print("\n'==' OPERATOR:")
print("- Checks if two objects have the SAME VALUE/CONTENT")
print("- Returns True if the values are equal, regardless of memory location")
print("- Also called 'equality operator'")

# Basic example
a = [1, 2, 3]
b = [1, 2, 3]  # Same content, different objects

print(f"\nExample with lists:")
print(f"a = {a}")
print(f"b = {b}")
print(f"a == b: {a == b}")  # True - same content
print(f"a is b: {a is b}")  # False - different objects

# =============================================================================
# 2. IDENTITY OPERATOR ('is')
# =============================================================================
print("\n2. IDENTITY OPERATOR ('is')")
print("-" * 30)

print("'is' OPERATOR EXAMPLES:")

# Same object
x = [1, 2, 3]
y = x  # y refers to the same object as x
print(f"x = {x}")
print(f"y = x")
print(f"x is y: {x is y}")  # True - same object
print(f"x == y: {x == y}")  # True - same content

# Different objects with same content
list1 = [1, 2, 3]
list2 = [1, 2, 3]  # New object with same content
print(f"\nlist1 = {list1}")
print(f"list2 = {list2}")
print(f"list1 is list2: {list1 is list2}")  # False - different objects
print(f"list1 == list2: {list1 == list2}")  # True - same content

# Memory addresses (id function)
print(f"\nMemory addresses:")
print(f"id(list1): {id(list1)}")
print(f"id(list2): {id(list2)}")
print(f"list1 is list2: {list1 is list2}")  # False - different memory addresses

# =============================================================================
# 3. EQUALITY OPERATOR ('==')
# =============================================================================
print("\n3. EQUALITY OPERATOR ('==')")
print("-" * 30)

print("'==' OPERATOR EXAMPLES:")

# Numbers
num1 = 5
num2 = 5
print(f"num1 = {num1}")
print(f"num2 = {num2}")
print(f"num1 == num2: {num1 == num2}")  # True - same value
print(f"num1 is num2: {num1 is num2}")  # True - Python optimizes small integers

# Strings
str1 = "hello"
str2 = "hello"
print(f"\nstr1 = '{str1}'")
print(f"str2 = '{str2}'")
print(f"str1 == str2: {str1 == str2}")  # True - same content
print(f"str1 is str2: {str1 is str2}")  # True - Python optimizes string literals

# Different string objects
str3 = "hello"
str4 = "h" + "ello"  # Different object, same content
print(f"\nstr3 = '{str3}'")
print(f"str4 = 'h' + 'ello' = '{str4}'")
print(f"str3 == str4: {str3 == str4}")  # True - same content
print(f"str3 is str4: {str3 is str4}")  # True - Python optimizes this case too

# =============================================================================
# 4. PYTHON'S INTERNING AND OPTIMIZATION
# =============================================================================
print("\n4. PYTHON'S INTERNING AND OPTIMIZATION")
print("-" * 30)

print("PYTHON OPTIMIZES CERTAIN OBJECTS:")
print("- Small integers (-5 to 256) are interned")
print("- String literals are often interned")
print("- This can make 'is' and '==' return the same result")

# Small integers (interned)
a = 100
b = 100
print(f"\nSmall integers:")
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # True
print(f"a is b: {a is b}")  # True - same object due to interning

# Large integers (not interned)
c = 1000
d = 1000
print(f"\nLarge integers:")
print(f"c = {c}, d = {d}")
print(f"c == d: {c == d}")  # True
print(f"c is d: {c is d}")  # False - different objects

# String interning
s1 = "hello"
s2 = "hello"
print(f"\nString literals:")
print(f"s1 = '{s1}', s2 = '{s2}'")
print(f"s1 == s2: {s1 == s2}")  # True
print(f"s1 is s2: {s1 is s2}")  # True - interned

# String concatenation (may not be interned)
s3 = "hello"
s4 = "hel" + "lo"
print(f"\nString concatenation:")
print(f"s3 = '{s3}', s4 = 'hel' + 'lo' = '{s4}'")
print(f"s3 == s4: {s3 == s4}")  # True
print(f"s3 is s4: {s3 is s4}")  # True - Python optimizes this

# =============================================================================
# 5. 'is not' OPERATOR
# =============================================================================
print("\n5. 'is not' OPERATOR")
print("-" * 30)

print("'is not' OPERATOR:")
print("- Opposite of 'is'")
print("- Returns True if objects are NOT the same")
print("- Equivalent to 'not (a is b)'")

# Examples
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(f"list_a = {list_a}")
print(f"list_b = {list_b}")
print(f"list_c = list_a")

print(f"\nlist_a is not list_b: {list_a is not list_b}")  # True - different objects
print(f"list_a is not list_c: {list_a is not list_c}")  # False - same object

# Common use case with None
value = None
print(f"\nvalue = {value}")
print(f"value is not None: {value is not None}")  # False
print(f"value is None: {value is None}")  # True

value = "something"
print(f"\nvalue = '{value}'")
print(f"value is not None: {value is not None}")  # True
print(f"value is None: {value is None}")  # False

# =============================================================================
# 6. PRACTICAL EXAMPLES SHOWING DIFFERENCES
# =============================================================================
print("\n6. PRACTICAL EXAMPLES SHOWING DIFFERENCES")
print("-" * 30)


# Example 1: Lists
def demonstrate_lists():
    """Demonstrate is vs == with lists."""
    original = [1, 2, 3]
    copy1 = original  # Same object
    copy2 = original.copy()  # Different object, same content
    copy3 = [1, 2, 3]  # Different object, same content

    print("LIST EXAMPLES:")
    print(f"original = {original}")
    print(f"copy1 = original -> {copy1}")
    print(f"copy2 = original.copy() -> {copy2}")
    print(f"copy3 = [1, 2, 3] -> {copy3}")

    print(f"\nComparisons:")
    print(f"original is copy1: {original is copy1}")  # True
    print(f"original == copy1: {original == copy1}")  # True

    print(f"original is copy2: {original is copy2}")  # False
    print(f"original == copy2: {original == copy2}")  # True

    print(f"original is copy3: {original is copy3}")  # False
    print(f"original == copy3: {original == copy3}")  # True


demonstrate_lists()


# Example 2: Dictionaries
def demonstrate_dictionaries():
    """Demonstrate is vs == with dictionaries."""
    dict1 = {"name": "Alice", "age": 25}
    dict2 = {"name": "Alice", "age": 25}
    dict3 = dict1

    print("\nDICTIONARY EXAMPLES:")
    print(f"dict1 = {dict1}")
    print(f"dict2 = {dict2}")
    print(f"dict3 = dict1")

    print(f"\nComparisons:")
    print(f"dict1 is dict2: {dict1 is dict2}")  # False
    print(f"dict1 == dict2: {dict1 == dict2}")  # True

    print(f"dict1 is dict3: {dict1 is dict3}")  # True
    print(f"dict1 == dict3: {dict1 == dict3}")  # True


demonstrate_dictionaries()


# Example 3: Custom objects
class Person:
    """Simple Person class for demonstration."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """Define equality based on name and age."""
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age


def demonstrate_custom_objects():
    """Demonstrate is vs == with custom objects."""
    person1 = Person("Alice", 25)
    person2 = Person("Alice", 25)
    person3 = person1

    print("\nCUSTOM OBJECT EXAMPLES:")
    print(f"person1 = Person('Alice', 25)")
    print(f"person2 = Person('Alice', 25)")
    print(f"person3 = person1")

    print(f"\nComparisons:")
    print(f"person1 is person2: {person1 is person2}")  # False
    print(f"person1 == person2: {person1 == person2}")  # True (due to __eq__)

    print(f"person1 is person3: {person1 is person3}")  # True
    print(f"person1 == person3: {person1 == person3}")  # True


demonstrate_custom_objects()

# =============================================================================
# 7. WHEN TO USE 'is' vs '=='
# =============================================================================
print("\n7. WHEN TO USE 'is' vs '=='")
print("-" * 30)

print("USE 'is' WHEN:")
print("1. Checking for None")
print("2. Checking for boolean values (True/False)")
print("3. Checking if two variables refer to the same object")
print("4. Checking for sentinel values")

print("\nUSE '==' WHEN:")
print("1. Comparing values/content")
print("2. Checking if two objects have the same data")
print("3. Most general comparisons")
print("4. Comparing numbers, strings, lists, etc.")


# Example 1: Checking for None (use 'is')
def process_data(data):
    """Process data - use 'is' for None check."""
    if data is None:
        return "No data provided"
    return f"Processing: {data}"


print("\nNONE CHECKING EXAMPLES:")
print(f"process_data(None): {process_data(None)}")
print(f"process_data('hello'): {process_data('hello')}")


# Example 2: Checking for boolean values (use 'is')
def check_status(status):
    """Check status - use 'is' for boolean check."""
    if status is True:
        return "Status is explicitly True"
    elif status is False:
        return "Status is explicitly False"
    else:
        return "Status is not a boolean"


print("\nBOOLEAN CHECKING EXAMPLES:")
print(f"check_status(True): {check_status(True)}")
print(f"check_status(False): {check_status(False)}")
print(f"check_status(1): {check_status(1)}")


# Example 3: Comparing values (use '==')
def compare_numbers(a, b):
    """Compare numbers - use '==' for value comparison."""
    if a == b:
        return "Numbers are equal"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{a} is less than {b}"


print("\nVALUE COMPARISON EXAMPLES:")
print(f"compare_numbers(5, 5): {compare_numbers(5, 5)}")
print(f"compare_numbers(10, 5): {compare_numbers(10, 5)}")
print(f"compare_numbers(3, 7): {compare_numbers(3, 7)}")

# =============================================================================
# 8. COMMON MISTAKES AND BEST PRACTICES
# =============================================================================
print("\n8. COMMON MISTAKES AND BEST PRACTICES")
print("-" * 30)

print("❌ COMMON MISTAKES:")


# Mistake 1: Using '==' with None
def bad_none_check(value):
    """Bad way to check for None."""
    return value == None  # Should use 'is None'


def good_none_check(value):
    """Good way to check for None."""
    return value is None


print("Mistake 1 - None checking:")
print(f"bad_none_check(None): {bad_none_check(None)}")
print(f"good_none_check(None): {good_none_check(None)}")


# Mistake 2: Using 'is' for value comparison
def bad_value_check(a, b):
    """Bad way to check values."""
    return a is b  # Should use '==' for value comparison


def good_value_check(a, b):
    """Good way to check values."""
    return a == b


print("\nMistake 2 - Value comparison:")
print(f"bad_value_check(5, 5): {bad_value_check(5, 5)}")
print(f"good_value_check(5, 5): {good_value_check(5, 5)}")


# Mistake 3: Using 'is' with mutable objects
def bad_list_check(list1, list2):
    """Bad way to check lists."""
    return list1 is list2  # Should use '==' for content comparison


def good_list_check(list1, list2):
    """Good way to check lists."""
    return list1 == list2


print("\nMistake 3 - List comparison:")
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(f"bad_list_check(list_a, list_b): {bad_list_check(list_a, list_b)}")
print(f"good_list_check(list_a, list_b): {good_list_check(list_a, list_b)}")

print("\n✅ BEST PRACTICES:")


# Practice 1: Always use 'is' for None
def validate_input(data):
    """Validate input using 'is' for None check."""
    if data is None:
        raise ValueError("Data cannot be None")
    if not data:
        raise ValueError("Data cannot be empty")
    return True


# Practice 2: Use '==' for value comparison
def find_maximum(numbers):
    """Find maximum using '==' for comparison."""
    if not numbers:
        return None

    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:  # This uses '>' but same principle as '=='
            maximum = num
    return maximum


# Practice 3: Use 'is' for identity checks
def remove_duplicates_preserve_order(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:  # This uses 'not in' but same principle
            seen.add(item)
            result.append(item)
    return result


print("\nBEST PRACTICES EXAMPLES:")
try:
    validate_input("valid data")
    print("validate_input('valid data'): Success")
except ValueError as e:
    print(f"validate_input('valid data'): {e}")

try:
    validate_input(None)
    print("validate_input(None): Success")
except ValueError as e:
    print(f"validate_input(None): {e}")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"find_maximum({numbers}): {find_maximum(numbers)}")

duplicates = [1, 2, 2, 3, 1, 4, 3, 5]
unique = remove_duplicates_preserve_order(duplicates)
print(f"remove_duplicates_preserve_order({duplicates}): {unique}")

# =============================================================================
# 9. ADVANCED EXAMPLES AND EDGE CASES
# =============================================================================
print("\n9. ADVANCED EXAMPLES AND EDGE CASES")
print("-" * 30)

# Edge case 1: Empty containers
empty_list1 = []
empty_list2 = []
print("EMPTY CONTAINERS:")
print(f"empty_list1 = {empty_list1}")
print(f"empty_list2 = {empty_list2}")
print(f"empty_list1 is empty_list2: {empty_list1 is empty_list2}")  # False
print(f"empty_list1 == empty_list2: {empty_list1 == empty_list2}")  # True

# Edge case 2: NaN (Not a Number)
import math

nan1 = float("nan")
nan2 = float("nan")
print(f"\nNaN VALUES:")
print(f"nan1 = {nan1}")
print(f"nan2 = {nan2}")
print(f"nan1 is nan2: {nan1 is nan2}")  # False
print(f"nan1 == nan2: {nan1 == nan2}")  # False (NaN is not equal to itself)
print(f"math.isnan(nan1): {math.isnan(nan1)}")  # True


# Edge case 3: Custom __eq__ method
class SpecialNumber:
    """Custom number class with special equality."""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """Always return True for equality."""
        return True

    def __repr__(self):
        return f"SpecialNumber({self.value})"


num1 = SpecialNumber(5)
num2 = SpecialNumber(10)
print(f"\nCUSTOM EQUALITY:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")
print(f"num1 == num2: {num1 == num2}")  # True (due to __eq__)
print(f"num1 is num2: {num1 is num2}")  # False


# Edge case 4: Mutable default arguments
def bad_function(items=[]):
    """Bad function with mutable default argument."""
    items.append("new_item")
    return items


def good_function(items=None):
    """Good function with immutable default argument."""
    if items is None:
        items = []
    items.append("new_item")
    return items


print(f"\nMUTABLE DEFAULT ARGUMENTS:")
result1 = bad_function()
result2 = bad_function()
print(f"bad_function() first call: {result1}")
print(f"bad_function() second call: {result2}")
print(f"result1 is result2: {result1 is result2}")  # True - same object!

result3 = good_function()
result4 = good_function()
print(f"good_function() first call: {result3}")
print(f"good_function() second call: {result4}")
print(f"result3 is result4: {result3 is result4}")  # False - different objects

print("\n" + "=" * 60)
print("SUMMARY OF 'is' vs '=='")
print("=" * 60)
print("'is' OPERATOR:")
print("  - Checks IDENTITY (same object in memory)")
print("  - Use for: None, True/False, object identity")
print("  - Returns True only if same memory location")
print()
print("'==' OPERATOR:")
print("  - Checks EQUALITY (same value/content)")
print("  - Use for: comparing values, content, data")
print("  - Returns True if values are equal")
print()
print("KEY RULES:")
print("  - Always use 'is' for None: value is None")
print("  - Always use 'is' for booleans: value is True")
print("  - Use '==' for value comparison: a == b")
print("  - Use 'is' for identity check: obj1 is obj2")
print()
print("PYTHON OPTIMIZATIONS:")
print("  - Small integers (-5 to 256) are interned")
print("  - String literals are often interned")
print("  - This can make 'is' and '==' return same result")
print()
print("BEST PRACTICES:")
print("  - Use 'is' for None and boolean checks")
print("  - Use '==' for value comparisons")
print("  - Be aware of Python's interning")
print("  - Don't rely on 'is' for value comparison")
print("\nPractice with these examples to master the difference!")
