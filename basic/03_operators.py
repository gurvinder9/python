"""
Python Basics - Operators
This file covers arithmetic, comparison, logical, and other operators in Python.
"""

# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print(f"{a} + {b} = {a + b}")  # Addition: 13
print(f"{a} - {b} = {a - b}")  # Subtraction: 7
print(f"{a} * {b} = {a * b}")  # Multiplication: 30
print(f"{a} / {b} = {a / b}")  # Division: 3.333...
print(f"{a} // {b} = {a // b}")  # Floor division: 3
print(f"{a} % {b} = {a % b}")  # Modulo: 1
print(f"{a} ** {b} = {a ** b}")  # Exponentiation: 1000

# Comparison Operators
x = 5
y = 10

print("\\nComparison Operators:")
print(f"{x} == {y} : {x == y}")  # Equal to: False
print(f"{x} != {y} : {x != y}")  # Not equal to: True
print(f"{x} < {y} : {x < y}")  # Less than: True
print(f"{x} > {y} : {x > y}")  # Greater than: False
print(f"{x} <= {y} : {x <= y}")  # Less than or equal: True
print(f"{x} >= {y} : {x >= y}")  # Greater than or equal: False

# Logical Operators
p = True
q = False

print("\\nLogical Operators:")
print(f"p = {p}, q = {q}")
print(f"p and q : {p and q}")  # False
print(f"p or q : {p or q}")  # True
print(f"not p : {not p}")  # False
print(f"not q : {not q}")  # True

# Assignment Operators
num = 5
print(f"\\nOriginal num: {num}")

num += 3  # num = num + 3
print(f"num += 3: {num}")

num -= 2  # num = num - 2
print(f"num -= 2: {num}")

num *= 4  # num = num * 4
print(f"num *= 4: {num}")

num /= 2  # num = num / 2
print(f"num /= 2: {num}")

# Identity and Membership Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\\nIdentity Operators:")
print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is list3: {list1 is list3}")  # True (same object)

print("\\nMembership Operators:")
print(f"2 in list1: {2 in list1}")  # True
print(f"5 not in list1: {5 not in list1}")  # True
