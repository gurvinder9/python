"""
15. Logical Operators in Python

Logical operators are used to combine or modify boolean expressions.
Python has three logical operators: and, or, not

LOGICAL OPERATORS:
1. and - Returns True if both operands are True
2. or - Returns True if at least one operand is True
3. not - Reverses the boolean value of the operand

These operators work with boolean values and follow short-circuit evaluation.
"""

print("=" * 60)
print("LOGICAL OPERATORS IN PYTHON")
print("=" * 60)

# =============================================================================
# 1. BASIC LOGICAL OPERATORS OVERVIEW
# =============================================================================
print("\n1. BASIC LOGICAL OPERATORS OVERVIEW")
print("-" * 30)

# Truth table for AND operator
print("AND OPERATOR TRUTH TABLE:")
print("True  and True  =", True and True)
print("True  and False =", True and False)
print("False and True  =", False and True)
print("False and False =", False and False)

print("\nOR OPERATOR TRUTH TABLE:")
print("True  or True  =", True or True)
print("True  or False =", True or False)
print("False or True  =", False or True)
print("False or False =", False or False)

print("\nNOT OPERATOR TRUTH TABLE:")
print("not True  =", not True)
print("not False =", not False)

# =============================================================================
# 2. AND OPERATOR DETAILED EXPLANATION
# =============================================================================
print("\n2. AND OPERATOR DETAILED EXPLANATION")
print("-" * 30)

print("AND OPERATOR:")
print("- Returns True ONLY if BOTH operands are True")
print("- Returns False if ANY operand is False")
print("- Short-circuits: stops evaluating if first operand is False")

# Basic AND examples
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Age: {age}, Has license: {has_license}")
print(f"Can drive: {can_drive}")

# AND with different combinations
print("\nAND OPERATOR EXAMPLES:")
test_cases = [
    (True, True, "Both True"),
    (True, False, "First True, Second False"),
    (False, True, "First False, Second True"),
    (False, False, "Both False"),
]

for a, b, description in test_cases:
    result = a and b
    print(f"{a:5} and {b:5} = {result:5} # {description}")

# AND with non-boolean values
print("\nAND WITH NON-BOOLEAN VALUES:")
print("AND returns the first falsy value or the last truthy value")
print(f"0 and 5 = {0 and 5}")
print(f"3 and 5 = {3 and 5}")
print(f"'' and 'hello' = {repr('' and 'hello')}")
print(f"'hello' and 'world' = {repr('hello' and 'world')}")
print(f"None and 'value' = {repr(None and 'value')}")

# =============================================================================
# 3. OR OPERATOR DETAILED EXPLANATION
# =============================================================================
print("\n3. OR OPERATOR DETAILED EXPLANATION")
print("-" * 30)

print("OR OPERATOR:")
print("- Returns True if AT LEAST ONE operand is True")
print("- Returns False ONLY if BOTH operands are False")
print("- Short-circuits: stops evaluating if first operand is True")

# Basic OR examples
weather = "sunny"
temperature = 25
good_weather = weather == "sunny" or temperature > 20
print(f"Weather: {weather}, Temperature: {temperature}")
print(f"Good weather: {good_weather}")

# OR with different combinations
print("\nOR OPERATOR EXAMPLES:")
test_cases = [
    (True, True, "Both True"),
    (True, False, "First True, Second False"),
    (False, True, "First False, Second True"),
    (False, False, "Both False"),
]

for a, b, description in test_cases:
    result = a or b
    print(f"{a:5} or {b:5} = {result:5} # {description}")

# OR with non-boolean values
print("\nOR WITH NON-BOOLEAN VALUES:")
print("OR returns the first truthy value or the last falsy value")
print(f"0 or 5 = {0 or 5}")
print(f"3 or 5 = {3 or 5}")
print(f"'' or 'hello' = {repr('' or 'hello')}")
print(f"'hello' or 'world' = {repr('hello' or 'world')}")
print(f"None or '' or 'default' = {repr(None or '' or 'default')}")

# =============================================================================
# 4. NOT OPERATOR DETAILED EXPLANATION
# =============================================================================
print("\n4. NOT OPERATOR DETAILED EXPLANATION")
print("-" * 30)

print("NOT OPERATOR:")
print("- Reverses the boolean value of the operand")
print("- Always returns a boolean value (True or False)")
print("- Has higher precedence than AND and OR")

# Basic NOT examples
is_weekend = False
is_weekday = not is_weekend
print(f"Is weekend: {is_weekend}")
print(f"Is weekday: {is_weekday}")

# NOT with different values
print("\nNOT OPERATOR EXAMPLES:")
test_values = [True, False, 1, 0, "hello", "", [1, 2], [], None]

for value in test_values:
    result = not value
    print(f"not {repr(value):10} = {result:5}")

# NOT with comparisons
print("\nNOT WITH COMPARISONS:")
age = 16
is_minor = not (age >= 18)
print(f"Age: {age}, Is minor: {is_minor}")

score = 85
failed = not (score >= 60)
print(f"Score: {score}, Failed: {failed}")

# =============================================================================
# 5. OPERATOR PRECEDENCE AND GROUPING
# =============================================================================
print("\n5. OPERATOR PRECEDENCE AND GROUPING")
print("-" * 30)

print("OPERATOR PRECEDENCE (from highest to lowest):")
print("1. not")
print("2. and")
print("3. or")

# Examples showing precedence
print("\nPRECEDENCE EXAMPLES:")

# Example 1: not has highest precedence
result1 = not True and False
result2 = (not True) and False
result3 = not (True and False)
print(f"not True and False = {result1}")
print(f"(not True) and False = {result2}")
print(f"not (True and False) = {result3}")

# Example 2: and has higher precedence than or
result1 = True or False and False
result2 = True or (False and False)
result3 = (True or False) and False
print(f"True or False and False = {result1}")
print(f"True or (False and False) = {result2}")
print(f"(True or False) and False = {result3}")

# Example 3: Complex expression
a, b, c = True, False, True
result1 = not a or b and c
result2 = (not a) or (b and c)
result3 = not (a or b) and c
print(f"not a or b and c = {result1}")
print(f"(not a) or (b and c) = {result2}")
print(f"not (a or b) and c = {result3}")

# =============================================================================
# 6. SHORT-CIRCUIT EVALUATION
# =============================================================================
print("\n6. SHORT-CIRCUIT EVALUATION")
print("-" * 30)

print("SHORT-CIRCUIT EVALUATION:")
print("- Python stops evaluating as soon as it knows the result")
print("- AND: stops if first operand is False")
print("- OR: stops if first operand is True")


# Function to demonstrate short-circuit
def expensive_operation():
    print("  -> Expensive operation executed!")
    return True


def cheap_operation():
    print("  -> Cheap operation executed!")
    return False


print("\nAND SHORT-CIRCUIT EXAMPLES:")
print("False and expensive_operation():")
result = False and expensive_operation()
print(f"Result: {result}")

print("\nTrue and expensive_operation():")
result = True and expensive_operation()
print(f"Result: {result}")

print("\nOR SHORT-CIRCUIT EXAMPLES:")
print("True or expensive_operation():")
result = True or expensive_operation()
print(f"Result: {result}")

print("\nFalse or expensive_operation():")
result = False or expensive_operation()
print(f"Result: {result}")


# Practical short-circuit example
def safe_divide(a, b):
    """Safely divide two numbers using short-circuit evaluation."""
    return b != 0 and a / b


print("\nPRACTICAL SHORT-CIRCUIT EXAMPLE:")
print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")

# =============================================================================
# 7. COMBINING LOGICAL OPERATORS
# =============================================================================
print("\n7. COMBINING LOGICAL OPERATORS")
print("-" * 30)


# Complex logical expressions
def check_user_permissions(user):
    """Check user permissions with complex logic."""
    has_admin = user.get("role") == "admin"
    has_moderator = user.get("role") == "moderator"
    is_verified = user.get("verified", False)
    has_permissions = user.get("permissions", [])

    # Complex logical expression
    can_moderate = (
        (has_admin or has_moderator) and is_verified and len(has_permissions) > 0
    )

    return can_moderate


# Test cases
users = [
    {"role": "admin", "verified": True, "permissions": ["read", "write"]},
    {"role": "moderator", "verified": True, "permissions": ["read"]},
    {"role": "user", "verified": True, "permissions": ["read"]},
    {"role": "admin", "verified": False, "permissions": ["read", "write"]},
    {"role": "moderator", "verified": True, "permissions": []},
]

print("USER PERMISSION CHECKS:")
for i, user in enumerate(users, 1):
    can_moderate = check_user_permissions(user)
    print(
        f"User {i}: {user['role']:10} | Verified: {user['verified']:5} | Permissions: {len(user['permissions']):2} | Can moderate: {can_moderate}"
    )

# =============================================================================
# 8. PRACTICAL REAL-WORLD EXAMPLES
# =============================================================================
print("\n8. PRACTICAL REAL-WORLD EXAMPLES")
print("-" * 30)


# Example 1: User authentication
def authenticate_user(username, password, remember_me=False):
    """Authenticate user with multiple conditions."""
    valid_username = username and len(username) >= 3
    valid_password = password and len(password) >= 6
    has_special_char = password and any(c in "!@#$%^&*()" for c in password)

    # Complex authentication logic
    is_authenticated = (
        valid_username and valid_password and (has_special_char or remember_me)
    )

    return is_authenticated


print("USER AUTHENTICATION EXAMPLES:")
test_users = [
    ("alice", "password123!", True),
    ("bob", "weak", False),
    ("charlie", "strongpass", True),
    ("", "password123!", False),
]

for username, password, remember in test_users:
    auth_result = authenticate_user(username, password, remember)
    print(
        f"Username: {username:10} | Password: {password:15} | Remember: {remember:5} | Authenticated: {auth_result}"
    )


# Example 2: Data validation
def validate_data(data):
    """Validate data with multiple conditions."""
    has_name = data.get("name") and len(data["name"]) > 0
    has_email = data.get("email") and "@" in data["email"]
    has_age = data.get("age") and 0 <= data["age"] <= 120
    has_phone = data.get("phone") and len(data["phone"]) >= 10

    # All required fields must be present
    is_valid = has_name and has_email and has_age and has_phone

    return is_valid


print("\nDATA VALIDATION EXAMPLES:")
test_data = [
    {"name": "Alice", "email": "alice@example.com", "age": 25, "phone": "1234567890"},
    {"name": "", "email": "bob@example.com", "age": 30, "phone": "0987654321"},
    {"name": "Charlie", "email": "invalid-email", "age": 35, "phone": "5555555555"},
    {"name": "Diana", "email": "diana@example.com", "age": 150, "phone": "1111111111"},
    {"name": "Eve", "email": "eve@example.com", "age": 28, "phone": "123"},
]

for i, data in enumerate(test_data, 1):
    is_valid = validate_data(data)
    print(f"Data {i}: Valid = {is_valid:5} | {data}")


# Example 3: Game logic
def check_game_win(player, computer):
    """Check if player wins in rock-paper-scissors."""
    # Win conditions
    rock_beats_scissors = player == "rock" and computer == "scissors"
    paper_beats_rock = player == "paper" and computer == "rock"
    scissors_beats_paper = player == "scissors" and computer == "paper"

    # Player wins if any condition is true
    player_wins = rock_beats_scissors or paper_beats_rock or scissors_beats_paper

    return player_wins


print("\nGAME LOGIC EXAMPLES:")
game_moves = [
    ("rock", "scissors"),
    ("paper", "rock"),
    ("scissors", "paper"),
    ("rock", "paper"),
    ("paper", "scissors"),
    ("scissors", "rock"),
]

for player, computer in game_moves:
    player_wins = check_game_win(player, computer)
    print(f"Player: {player:8} | Computer: {computer:8} | Player wins: {player_wins}")

# =============================================================================
# 9. COMMON PATTERNS AND IDIOMS
# =============================================================================
print("\n9. COMMON PATTERNS AND IDIOMS")
print("-" * 30)


# Pattern 1: Default values with OR
def get_config_value(key, default=None):
    """Get config value with default using OR operator."""
    config = {"theme": "dark", "language": "en", "debug": False}
    return config.get(key) or default


print("DEFAULT VALUES PATTERN:")
theme = get_config_value("theme", "light")
missing_key = get_config_value("missing_key", "default_value")
print(f"Theme: {theme}")
print(f"Missing key: {missing_key}")


# Pattern 2: Conditional execution with AND
def log_message(message, level="INFO"):
    """Log message only if message exists."""
    if message and level:
        print(f"[{level}] {message}")


print("\nCONDITIONAL EXECUTION PATTERN:")
log_message("This will be logged")
log_message("")  # This won't be logged
log_message("Another message", "ERROR")


# Pattern 3: Validation with multiple conditions
def is_valid_email(email):
    """Validate email with multiple conditions."""
    return email and "@" in email and "." in email and len(email) > 5


print("\nVALIDATION PATTERN:")
emails = ["user@example.com", "invalid", "", "user@domain", "a@b.c"]
for email in emails:
    is_valid = is_valid_email(email)
    print(f"Email: {email:15} | Valid: {is_valid}")


# Pattern 4: Feature flags
def check_feature_access(user, feature):
    """Check if user has access to feature."""
    is_premium = user.get("premium", False)
    is_admin = user.get("role") == "admin"
    feature_enabled = feature.get("enabled", False)

    # Access if premium OR admin AND feature is enabled
    has_access = (is_premium or is_admin) and feature_enabled

    return has_access


print("\nFEATURE ACCESS PATTERN:")
users = [
    {"premium": True, "role": "user"},
    {"premium": False, "role": "admin"},
    {"premium": False, "role": "user"},
]
features = [
    {"name": "advanced_search", "enabled": True},
    {"name": "beta_features", "enabled": False},
]

for user in users:
    for feature in features:
        has_access = check_feature_access(user, feature)
        print(
            f"User: {user['role']:5} | Feature: {feature['name']:15} | Access: {has_access}"
        )

# =============================================================================
# 10. COMMON MISTAKES AND BEST PRACTICES
# =============================================================================
print("\n10. COMMON MISTAKES AND BEST PRACTICES")
print("-" * 30)

print("❌ COMMON MISTAKES:")

# Mistake 1: Using == True/False unnecessarily
value = 5
# WRONG: if value == True:
# CORRECT: if value:
print(f"Mistake 1 - Direct boolean check: {bool(value)}")

# Mistake 2: Confusing AND/OR logic
age = 20
has_license = True
# WRONG: can_drive = age >= 18 or has_license  # This would be True even for minors with license
# CORRECT: can_drive = age >= 18 and has_license
can_drive = age >= 18 and has_license
print(f"Mistake 2 - Correct AND logic: {can_drive}")

# Mistake 3: Not using parentheses for clarity
a, b, c = True, False, True
# CONFUSING: result = not a or b and c
# CLEAR: result = (not a) or (b and c)
result = (not a) or (b and c)
print(f"Mistake 3 - Clear parentheses: {result}")

print("\n✅ BEST PRACTICES:")


# Practice 1: Use parentheses for complex expressions
def check_complex_condition(x, y, z):
    """Use parentheses for clarity."""
    return (x > 0 and y > 0) or (z < 0 and x != y)


# Practice 2: Use meaningful variable names
def validate_user_input(username, password):
    """Use descriptive variable names."""
    is_username_valid = username and len(username) >= 3
    is_password_valid = password and len(password) >= 6
    is_input_valid = is_username_valid and is_password_valid

    return is_input_valid


# Practice 3: Break complex expressions into smaller parts
def process_order(order):
    """Break complex logic into smaller parts."""
    has_items = order.get("items") and len(order["items"]) > 0
    has_valid_address = order.get("address") and order["address"].get("street")
    has_payment = order.get("payment_method") and order["payment_method"] != "none"

    can_process = has_items and has_valid_address and has_payment

    return can_process


print("\n" + "=" * 60)
print("SUMMARY OF LOGICAL OPERATORS")
print("=" * 60)
print("OPERATORS:")
print("  - and: Returns True if BOTH operands are True")
print("  - or: Returns True if AT LEAST ONE operand is True")
print("  - not: Reverses the boolean value")
print()
print("PRECEDENCE (highest to lowest):")
print("  1. not")
print("  2. and")
print("  3. or")
print()
print("SHORT-CIRCUIT EVALUATION:")
print("  - AND: Stops if first operand is False")
print("  - OR: Stops if first operand is True")
print()
print("BEST PRACTICES:")
print("  - Use parentheses for complex expressions")
print("  - Use meaningful variable names")
print("  - Break complex logic into smaller parts")
print("  - Avoid unnecessary == True/False comparisons")
print("\nPractice with these examples to master logical operators!")
