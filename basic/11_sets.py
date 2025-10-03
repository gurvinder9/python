"""
Python Basics - Sets
This file demonstrates how sets work in Python.
Sets are unordered collections of unique elements, perfect for membership testing and removing duplicates.
"""

print("=== Python Sets Tutorial ===\n")

# =============================================================================
# WHAT ARE SETS?
# =============================================================================
print("1. WHAT ARE SETS?")
print("-" * 20)

print(
    "Sets are unordered collections of unique elements with these key characteristics:"
)
print("• Sets contain only UNIQUE elements (no duplicates)")
print("• Sets are UNORDERED (no indexing)")
print("• Sets are MUTABLE (can be changed after creation)")
print("• Sets are created with curly braces {} or set() constructor")
print("• Sets are perfect for membership testing and mathematical operations")
print("• Sets are very fast for checking if an element exists")
print("• Sets can contain only immutable data types (numbers, strings, tuples)\n")

# =============================================================================
# CREATING SETS
# =============================================================================
print("2. CREATING SETS")
print("-" * 20)

# Method 1: Using curly braces {}
print("Method 1: Using curly braces {}")
fruits = {"apple", "banana", "orange", "grape"}
print(f"Fruits set: {fruits}")

# Method 2: Using set() constructor
print("\nMethod 2: Using set() constructor")
numbers = set([1, 2, 3, 4, 5])
print(f"Numbers set: {numbers}")

# Method 3: Empty set (note: {} creates empty dict, not set!)
print("\nMethod 3: Empty set (note: {} creates empty dict, not set!)")
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type: {type(empty_set)}")

# This creates a dictionary, not a set!
empty_dict = {}
print(f"Empty dict: {empty_dict}")
print(f"Type: {type(empty_dict)}")

# Method 4: Set from string
print("\nMethod 4: Set from string")
word_set = set("Python")
print(f"Word as set: {word_set}")

# Method 5: Set from list (removes duplicates automatically)
print("\nMethod 5: Set from list (removes duplicates automatically)")
duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(duplicates)
print(f"Original list: {duplicates}")
print(f"Set (no duplicates): {unique_numbers}")

# =============================================================================
# SET OPERATIONS
# =============================================================================
print("\n\n3. SET OPERATIONS")
print("-" * 20)

# Length
print("Length:")
print(f"len(fruits): {len(fruits)}")

# Membership testing (very fast!)
print(f"\nMembership testing (very fast!):")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'kiwi' in fruits: {'kiwi' in fruits}")
print(f"'kiwi' not in fruits: {'kiwi' not in fruits}")

# Iterating through sets
print(f"\nIterating through sets:")
for fruit in fruits:
    print(f"  {fruit}")

# Note: Order is not guaranteed!
print("Note: Order is not guaranteed!")

# =============================================================================
# ADDING AND REMOVING ELEMENTS
# =============================================================================
print("\n\n4. ADDING AND REMOVING ELEMENTS")
print("-" * 35)

# Adding elements
print("Adding elements:")
fruits.add("kiwi")
print(f"After add('kiwi'): {fruits}")

# Adding multiple elements
fruits.update(["mango", "pineapple"])
print(f"After update(['mango', 'pineapple']): {fruits}")

# Removing elements
print(f"\nRemoving elements:")
fruits.remove("banana")  # Raises KeyError if not found
print(f"After remove('banana'): {fruits}")

fruits.discard("orange")  # Doesn't raise error if not found
print(f"After discard('orange'): {fruits}")

# Pop random element
popped = fruits.pop()
print(f"Popped element: {popped}")
print(f"After pop(): {fruits}")

# Clear all elements
fruits.clear()
print(f"After clear(): {fruits}")

# =============================================================================
# SET METHODS
# =============================================================================
print("\n\n5. SET METHODS")
print("-" * 20)

# Reset sets for demonstration
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2, 3}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set3: {set3}")

# Union (all elements from both sets)
print(f"\nUnion (all elements from both sets):")
union = set1.union(set2)
print(f"set1.union(set2): {union}")
print(f"set1 | set2: {set1 | set2}")

# Intersection (common elements)
print(f"\nIntersection (common elements):")
intersection = set1.intersection(set2)
print(f"set1.intersection(set2): {intersection}")
print(f"set1 & set2: {set1 & set2}")

# Difference (elements in set1 but not in set2)
print(f"\nDifference (elements in set1 but not in set2):")
difference = set1.difference(set2)
print(f"set1.difference(set2): {difference}")
print(f"set1 - set2: {set1 - set2}")

# Symmetric difference (elements in either set but not both)
print(f"\nSymmetric difference (elements in either set but not both):")
symmetric_diff = set1.symmetric_difference(set2)
print(f"set1.symmetric_difference(set2): {symmetric_diff}")
print(f"set1 ^ set2: {set1 ^ set2}")

# Subset and superset
print(f"\nSubset and superset:")
print(f"set3.issubset(set1): {set3.issubset(set1)}")
print(f"set3 <= set1: {set3 <= set1}")
print(f"set1.issuperset(set3): {set1.issuperset(set3)}")
print(f"set1 >= set3: {set1 >= set3}")

# Disjoint (no common elements)
print(f"\nDisjoint (no common elements):")
disjoint_set = {9, 10, 11}
print(f"set1.isdisjoint(disjoint_set): {set1.isdisjoint(disjoint_set)}")

# =============================================================================
# WHEN TO USE SETS
# =============================================================================
print("\n\n6. WHEN TO USE SETS")
print("-" * 25)

print("✅ Use sets when:")
print("• You need to remove duplicates from a collection")
print("• You need fast membership testing")
print("• You need mathematical set operations")
print("• You don't care about order")
print("• You want to ensure uniqueness")
print("• You need to find common/different elements")

print("\n❌ Don't use sets when:")
print("• You need to maintain order")
print("• You need indexing (sets don't support indexing)")
print("• You need to store mutable objects")
print("• You need duplicate elements")
print("• You need to access elements by position")

# Example 1: Removing duplicates
print("\nExample 1: Removing duplicates")
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
unique_names = set(names)
print(f"Original: {names}")
print(f"Unique: {unique_names}")

# Example 2: Fast membership testing
print("\nExample 2: Fast membership testing")
valid_users = {"alice", "bob", "charlie", "diana"}
user_input = "alice"
if user_input in valid_users:
    print(f"User '{user_input}' is valid!")
else:
    print(f"User '{user_input}' is not valid!")

# Example 3: Finding common elements
print("\nExample 3: Finding common elements")
students_math = {"Alice", "Bob", "Charlie", "Diana"}
students_science = {"Bob", "Charlie", "Eve", "Frank"}
both_subjects = students_math.intersection(students_science)
print(f"Math students: {students_math}")
print(f"Science students: {students_science}")
print(f"Both subjects: {both_subjects}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n\n7. PRACTICAL EXAMPLES")
print("-" * 25)

# Example 1: Tag system
print("Example 1: Tag system")
article_tags = {"python", "programming", "tutorial", "beginner"}
user_interests = {"python", "data-science", "machine-learning", "tutorial"}
recommended_tags = article_tags.intersection(user_interests)
print(f"Article tags: {article_tags}")
print(f"User interests: {user_interests}")
print(f"Recommended: {recommended_tags}")

# Example 2: Survey analysis
print("\nExample 2: Survey analysis")
survey_responses = ["yes", "no", "yes", "maybe", "no", "yes", "no", "yes"]
unique_responses = set(survey_responses)
response_count = {
    response: survey_responses.count(response) for response in unique_responses
}
print(f"Survey responses: {survey_responses}")
print(f"Unique responses: {unique_responses}")
print(f"Response count: {response_count}")

# Example 3: Permission system
print("\nExample 3: Permission system")
admin_permissions = {"read", "write", "delete", "admin"}
user_permissions = {"read", "write"}
guest_permissions = {"read"}


def check_permission(user_perms, required_perm):
    return required_perm in user_perms


print(f"Admin can delete: {check_permission(admin_permissions, 'delete')}")
print(f"User can delete: {check_permission(user_permissions, 'delete')}")
print(f"Guest can write: {check_permission(guest_permissions, 'write')}")

# Example 4: Data validation
print("\nExample 4: Data validation")
valid_colors = {"red", "green", "blue", "yellow", "purple", "orange"}
user_color = "red"
if user_color in valid_colors:
    print(f"'{user_color}' is a valid color!")
else:
    print(f"'{user_color}' is not a valid color!")

# =============================================================================
# SET COMPREHENSIONS
# =============================================================================
print("\n\n8. SET COMPREHENSIONS")
print("-" * 30)

# Basic set comprehension
print("Basic set comprehension:")
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Set comprehension with condition
print(f"\nSet comprehension with condition:")
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Set comprehension from string
print(f"\nSet comprehension from string:")
vowels = {char for char in "programming" if char in "aeiou"}
print(f"Vowels in 'programming': {vowels}")

# Set comprehension with transformation
print(f"\nSet comprehension with transformation:")
words = ["hello", "world", "python", "programming"]
word_lengths = {len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# =============================================================================
# FROZEN SETS
# =============================================================================
print("\n\n9. FROZEN SETS")
print("-" * 20)

print("Frozen sets are immutable versions of sets:")
print("• Created with frozenset() constructor")
print("• Cannot be modified after creation")
print("• Can be used as dictionary keys")
print("• Can be used in other sets")

# Creating frozen sets
print("\nCreating frozen sets:")
frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen_set}")
print(f"Type: {type(frozen_set)}")

# Using frozen set as dictionary key
print(f"\nUsing frozen set as dictionary key:")
frozen_set_dict = {frozen_set: "This is a frozen set"}
print(f"Dictionary with frozen set key: {frozen_set_dict}")

# Frozen set in another set
print(f"\nFrozen set in another set:")
set_with_frozen = {frozen_set, frozenset([6, 7, 8])}
print(f"Set containing frozen sets: {set_with_frozen}")

# =============================================================================
# SETS VS LISTS VS TUPLES
# =============================================================================
print("\n\n10. SETS VS LISTS VS TUPLES")
print("-" * 35)

print("Comparison between sets, lists, and tuples:")
print("┌─────────────┬─────────────┬─────────────┬─────────────┐")
print("│ Feature     │ Set         │ List        │ Tuple       │")
print("├─────────────┼─────────────┼─────────────┼─────────────┤")
print("│ Order       │ No          │ Yes         │ Yes         │")
print("│ Duplicates  │ No          │ Yes         │ Yes         │")
print("│ Mutability  │ Mutable     │ Mutable     │ Immutable   │")
print("│ Indexing    │ No          │ Yes         │ Yes         │")
print("│ Syntax      │ {}          │ []          │ ()          │")
print("│ Membership  │ Very Fast   │ Slow        │ Slow        │")
print("│ Use case    │ Unique data │ Ordered data│ Fixed data  │")
print("└─────────────┴─────────────┴─────────────┴─────────────┘")

# Performance comparison for membership testing
print("\nPerformance comparison for membership testing:")
import time

# Test data
test_list = list(range(10000))
test_set = set(range(10000))
test_tuple = tuple(range(10000))

# Test membership in list
start_time = time.time()
for i in range(1000):
    _ = 5000 in test_list
list_time = time.time() - start_time

# Test membership in set
start_time = time.time()
for i in range(1000):
    _ = 5000 in test_set
set_time = time.time() - start_time

# Test membership in tuple
start_time = time.time()
for i in range(1000):
    _ = 5000 in test_tuple
tuple_time = time.time() - start_time

print(f"List membership time: {list_time:.4f} seconds")
print(f"Set membership time: {set_time:.4f} seconds")
print(f"Tuple membership time: {tuple_time:.4f} seconds")
print(f"Sets are {list_time/set_time:.1f}x faster than lists for membership testing!")

# =============================================================================
# COMMON SET PATTERNS
# =============================================================================
print("\n\n11. COMMON SET PATTERNS")
print("-" * 30)

# Pattern 1: Removing duplicates while preserving order
print("Pattern 1: Removing duplicates while preserving order")


def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


original = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_ordered = remove_duplicates_preserve_order(original)
print(f"Original: {original}")
print(f"Unique ordered: {unique_ordered}")

# Pattern 2: Finding differences between collections
print("\nPattern 2: Finding differences between collections")
old_features = {"login", "register", "profile", "settings"}
new_features = {"login", "register", "profile", "settings", "chat", "notifications"}
added_features = new_features - old_features
removed_features = old_features - new_features
print(f"Added features: {added_features}")
print(f"Removed features: {removed_features}")

# Pattern 3: Set-based validation
print("\nPattern 3: Set-based validation")


def validate_input(user_input, valid_options):
    return user_input in valid_options


valid_choices = {"yes", "no", "maybe"}
user_choice = "yes"
print(f"Valid choice: {validate_input(user_choice, valid_choices)}")

# Pattern 4: Set operations for data analysis
print("\nPattern 4: Set operations for data analysis")
customers_jan = {"Alice", "Bob", "Charlie", "Diana"}
customers_feb = {"Bob", "Charlie", "Eve", "Frank"}
customers_mar = {"Alice", "Charlie", "Eve", "Grace"}

# Customers who shopped in all three months
all_months = customers_jan.intersection(customers_feb).intersection(customers_mar)
print(f"Customers in all months: {all_months}")

# Customers who shopped in any month
any_month = customers_jan.union(customers_feb).union(customers_mar)
print(f"Customers in any month: {any_month}")

# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================
print("\n\n12. KEY CONCEPTS SUMMARY")
print("-" * 30)
print("✓ Sets are unordered collections of unique elements")
print("✓ Created with {} or set() constructor")
print("✓ Empty set is created with set(), not {}")
print("✓ Very fast for membership testing")
print("✓ Support mathematical set operations")
print("✓ Can contain only immutable data types")
print("✓ Perfect for removing duplicates")
print("✓ Use when you need uniqueness and fast lookups")
print("✓ Don't use when you need order or indexing")
print("✓ Frozen sets are immutable and can be used as keys")
print("✓ Set comprehensions create sets efficiently")
print("✓ Great for mathematical operations and data analysis")
print("\nSets are perfect for unique data and fast membership testing! 🎯")
