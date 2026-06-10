"""
14. Ternary Operators (Conditional Expressions) in Python

A ternary operator is a concise way to write conditional expressions.
It allows you to assign a value based on a condition in a single line.

SYNTAX:
value_if_true if condition else value_if_false

The ternary operator is also called a "conditional expression" in Python.
It's a one-line alternative to if-else statements for simple assignments.
"""

print("=" * 60)
print("TERNARY OPERATORS IN PYTHON")
print("=" * 60)

# =============================================================================
# 1. BASIC SYNTAX AND CONCEPT
# =============================================================================
print("\n1. BASIC SYNTAX AND CONCEPT")
print("-" * 30)

# Basic syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age: {age}, Status: {status}")

# Another simple example
temperature = 25
weather_advice = "Wear shorts" if temperature > 30 else "Wear pants"
print(f"Temperature: {temperature}°C, Advice: {weather_advice}")

# With numbers
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"Score: {score}, Grade: {grade}")

# =============================================================================
# 2. COMPARISON WITH IF-ELSE STATEMENTS
# =============================================================================
print("\n2. COMPARISON WITH IF-ELSE STATEMENTS")
print("-" * 30)

# Traditional if-else approach
age = 25
if age >= 18:
    can_vote = "Yes"
else:
    can_vote = "No"
print(f"Traditional way - Can vote: {can_vote}")

# Ternary operator approach (same result)
age = 25
can_vote = "Yes" if age >= 18 else "No"
print(f"Ternary way - Can vote: {can_vote}")

# Another comparison
number = 7
# Traditional way
if number % 2 == 0:
    parity = "even"
else:
    parity = "odd"
print(f"Traditional way - {number} is {parity}")

# Ternary way
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(f"Ternary way - {number} is {parity}")

# =============================================================================
# 3. BASIC EXAMPLES
# =============================================================================
print("\n3. BASIC EXAMPLES")
print("-" * 30)

# Example 1: Simple comparison
x = 10
y = 20
max_value = x if x > y else y
print(f"Max of {x} and {y}: {max_value}")

# Example 2: String operations
name = "Alice"
greeting = f"Hello {name}" if name else "Hello Guest"
print(f"Greeting: {greeting}")

# Example 3: List operations
numbers = [1, 2, 3, 4, 5]
has_even = "Yes" if any(num % 2 == 0 for num in numbers) else "No"
print(f"List {numbers} has even numbers: {has_even}")

# Example 4: Boolean conversion
value = 0
result = "Truthy" if value else "Falsy"
print(f"Value {value} is: {result}")

# Example 5: Mathematical operations
a = 15
b = 10
operation = "addition" if a > b else "subtraction"
result = a + b if a > b else a - b
print(f"Operation: {operation}, Result: {result}")

# =============================================================================
# 4. NESTED TERNARY OPERATORS
# =============================================================================
print("\n4. NESTED TERNARY OPERATORS")
print("-" * 30)

# Multiple conditions using nested ternary operators
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score: {score}, Grade: {grade}")

# Temperature classification
temp = 15
weather = (
    "Hot" if temp > 30 else "Warm" if temp > 20 else "Cool" if temp > 10 else "Cold"
)
print(f"Temperature: {temp}°C, Weather: {weather}")

# Age classification
age = 25
category = (
    "Senior"
    if age >= 65
    else "Adult"
    if age >= 18
    else "Teen"
    if age >= 13
    else "Child"
)
print(f"Age: {age}, Category: {category}")

# Number classification
num = 0
classification = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(f"Number: {num}, Classification: {classification}")

# =============================================================================
# 5. TERNARY OPERATORS WITH DIFFERENT DATA TYPES
# =============================================================================
print("\n5. TERNARY OPERATORS WITH DIFFERENT DATA TYPES")
print("-" * 30)

# With strings
name = "John"
display_name = name if name else "Anonymous"
print(f"Display name: {display_name}")

# With lists
items = [1, 2, 3]
message = f"Found {len(items)} items" if items else "No items found"
print(f"Message: {message}")

# With dictionaries
user = {"name": "Alice", "age": 25}
status = "Logged in" if user.get("name") else "Guest user"
print(f"Status: {status}")

# With numbers
price = 100
discount = 0.1 if price > 50 else 0.05
final_price = price * (1 - discount)
print(
    f"Original price: ${price}, Discount: {discount*100}%, Final price: ${final_price}"
)

# With boolean values
is_weekend = True
activity = "Relax" if is_weekend else "Work"
print(f"Day type: {'Weekend' if is_weekend else 'Weekday'}, Activity: {activity}")

# =============================================================================
# 6. PRACTICAL REAL-WORLD EXAMPLES
# =============================================================================
print("\n6. PRACTICAL REAL-WORLD EXAMPLES")
print("-" * 30)


# Example 1: User permission check
def get_user_permission(user_role):
    """Get user permission based on role."""
    return (
        "Admin" if user_role == "admin" else "User" if user_role == "user" else "Guest"
    )


roles = ["admin", "user", "guest", "moderator"]
for role in roles:
    permission = get_user_permission(role)
    print(f"Role: {role:10} -> Permission: {permission}")


# Example 2: Price calculation with discount
def calculate_price(original_price, is_member):
    """Calculate price with member discount."""
    discount_rate = 0.15 if is_member else 0.05
    return original_price * (1 - discount_rate)


prices = [100, 200, 50]
for price in prices:
    member_price = calculate_price(price, True)
    regular_price = calculate_price(price, False)
    print(
        f"Original: ${price:3} -> Member: ${member_price:5.2f}, Regular: ${regular_price:5.2f}"
    )


# Example 3: File size formatting
def format_file_size(size_bytes):
    """Format file size in human-readable format."""
    if size_bytes == 0:
        return "0 B"

    size_kb = size_bytes / 1024
    size_mb = size_bytes / (1024 * 1024)

    return (
        f"{size_mb:.1f} MB"
        if size_mb >= 1
        else f"{size_kb:.1f} KB"
        if size_kb >= 1
        else f"{size_bytes} B"
    )


file_sizes = [0, 500, 1500, 50000, 1500000]
for size in file_sizes:
    formatted = format_file_size(size)
    print(f"Size: {size:8} bytes -> {formatted}")


# Example 4: Password strength checker
def check_password_strength(password):
    """Check password strength."""
    if not password:
        return "No password"

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    return (
        "Very Strong"
        if score == 4 and length >= 8
        else "Strong"
        if score >= 3 and length >= 6
        else "Medium"
        if score >= 2
        else "Weak"
    )


passwords = ["", "123", "password", "Password123", "P@ssw0rd!", "MyStr0ng!P@ssw0rd"]
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"Password: {pwd:15} -> Strength: {strength}")

# =============================================================================
# 7. TERNARY OPERATORS IN FUNCTION CALLS
# =============================================================================
print("\n7. TERNARY OPERATORS IN FUNCTION CALLS")
print("-" * 30)


# Using ternary operators as function arguments
def greet_user(name, is_formal=False):
    """Greet user with formal or informal style."""
    greeting = "Good day" if is_formal else "Hi"
    return f"{greeting}, {name}!"


names = ["Alice", "Bob", "Charlie"]
for name in names:
    # Use ternary to determine formality
    is_formal = len(name) > 4
    message = greet_user(name, is_formal)
    print(f"Greeting: {message}")

# Ternary in list comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
categorized = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(f"Numbers: {numbers}")
print(f"Categorized: {categorized}")

# Ternary in dictionary comprehensions
scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 78}
grades = {
    name: "A" if score >= 90 else "B" if score >= 80 else "C"
    for name, score in scores.items()
}
print(f"Scores: {scores}")
print(f"Grades: {grades}")

# =============================================================================
# 8. WHEN TO USE TERNARY OPERATORS
# =============================================================================
print("\n8. WHEN TO USE TERNARY OPERATORS")
print("-" * 30)

print("✅ GOOD USE CASES:")
print("1. Simple conditional assignments")
print("2. One-line value selection")
print("3. Default value assignment")
print("4. Simple formatting decisions")
print("5. List/dict comprehensions")

# Good example 1: Simple assignment
user_input = "hello"
processed = user_input.upper() if user_input else "DEFAULT"
print(f"Good example 1: {processed}")


# Good example 2: Default values
def get_config_value(key, default=None):
    """Get config value with default."""
    config = {"theme": "dark", "language": "en"}
    return config.get(key) if key in config else default


theme = get_config_value("theme", "light")
print(f"Good example 2: Theme = {theme}")


# Good example 3: Simple formatting
def format_number(num):
    """Format number with appropriate precision."""
    return f"{num:.2f}" if isinstance(num, float) else str(num)


numbers = [1, 2.5, 3.14159, 10]
formatted = [format_number(num) for num in numbers]
print(f"Good example 3: {formatted}")

print("\n❌ AVOID THESE CASES:")
print("1. Complex nested conditions")
print("2. Multiple statements")
print("3. When readability suffers")
print("4. Complex logic that needs comments")

# Bad example: Too complex
# result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
# Better to use if-elif-else for complex logic

# =============================================================================
# 9. BEST PRACTICES AND TIPS
# =============================================================================
print("\n9. BEST PRACTICES AND TIPS")
print("-" * 30)

print("📝 BEST PRACTICES:")
print("1. Keep it simple and readable")
print("2. Use parentheses for complex expressions")
print("3. Don't nest too deeply (max 2-3 levels)")
print("4. Use meaningful variable names")
print("5. Consider readability over brevity")

# Tip 1: Use parentheses for clarity
x, y, z = 10, 20, 30
result = (x if x > y else y) if (x > y or y > z) else z
print(f"Tip 1 - With parentheses: {result}")


# Tip 2: Break complex expressions
def get_discount_rate(customer_type, purchase_amount):
    """Get discount rate with clear logic."""
    # Base discount
    base_discount = 0.1 if customer_type == "premium" else 0.05

    # Volume discount
    volume_discount = 0.05 if purchase_amount > 1000 else 0

    return base_discount + volume_discount


discount = get_discount_rate("premium", 1500)
print(f"Tip 2 - Clear logic: {discount*100}% discount")


# Tip 3: Use for simple validations
def validate_age(age):
    """Validate age with ternary."""
    return "Valid" if 0 <= age <= 120 else "Invalid"


ages = [25, -5, 150, 0, 120]
for age in ages:
    validation = validate_age(age)
    print(f"Tip 3 - Age {age:3}: {validation}")

# =============================================================================
# 10. COMMON MISTAKES TO AVOID
# =============================================================================
print("\n10. COMMON MISTAKES TO AVOID")
print("-" * 30)

print("⚠️  COMMON MISTAKES:")

# Mistake 1: Wrong order of conditions
# WRONG: result = "adult" else "minor" if age >= 18  # Syntax error
# CORRECT:
age = 20
result = "adult" if age >= 18 else "minor"
print(f"Mistake 1 - Correct syntax: {result}")

# Mistake 2: Using == True/False unnecessarily
value = 5
# WRONG: result = "positive" if value > 0 == True else "non-positive"
# CORRECT:
result = "positive" if value > 0 else "non-positive"
print(f"Mistake 2 - Direct comparison: {result}")

# Mistake 3: Too many nested conditions
score = 85
# AVOID: grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
# BETTER: Use if-elif-else for complex logic
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Mistake 3 - Clear logic: Grade {grade}")

# Mistake 4: Not considering operator precedence
a, b, c = 1, 2, 3
# WRONG: result = a if a > b else b if b > c else c  # Hard to read
# BETTER: Use parentheses
result = a if a > b else (b if b > c else c)
print(f"Mistake 4 - With parentheses: {result}")

print("\n" + "=" * 60)
print("SUMMARY OF TERNARY OPERATORS")
print("=" * 60)
print("SYNTAX: value_if_true if condition else value_if_false")
print()
print("✅ WHEN TO USE:")
print("  - Simple conditional assignments")
print("  - One-line value selection")
print("  - Default value assignment")
print("  - List/dict comprehensions")
print("  - Simple formatting decisions")
print()
print("❌ WHEN TO AVOID:")
print("  - Complex nested conditions")
print("  - Multiple statements")
print("  - When readability suffers")
print("  - Complex logic needing comments")
print()
print("📝 BEST PRACTICES:")
print("  - Keep it simple and readable")
print("  - Use parentheses for complex expressions")
print("  - Don't nest too deeply (max 2-3 levels)")
print("  - Use meaningful variable names")
print("  - Consider readability over brevity")
print()
print("🔧 COMMON PATTERNS:")
print("  - Default values: value or default")
print("  - Conditional assignment: x if condition else y")
print("  - Simple validation: 'valid' if condition else 'invalid'")
print("\nPractice with these examples to master ternary operators!")
