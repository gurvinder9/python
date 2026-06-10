"""
The Walrus Operator (:=) in Python 3.8+
========================================

The walrus operator (:=) is officially called the "assignment expression operator".
It was introduced in Python 3.8 (PEP 572) and allows you to assign values to
variables as part of an expression.

Key Points:
- Syntax: variable := expression
- Assigns AND returns a value in one operation
- Useful for avoiding duplicate code
- Reduces the number of lines needed
- Named "walrus" because := looks like a walrus on its side
- Works in if statements, while loops, list comprehensions, and more

Why Use It?
- Assign and use a value in the same expression
- Avoid repeated function calls or calculations
- Make code more concise and readable
- Improve performance by avoiding redundant computations

Requirements:
- Python 3.8 or higher
- Not available in Python 3.7 or earlier

Note: Use it judiciously - it can make code harder to read if overused!
"""

import re
import time

# ============================================
# 1. BASIC WALRUS OPERATOR USAGE
# ============================================

print("=" * 50)
print("1. BASIC WALRUS OPERATOR USAGE")
print("=" * 50)

# Traditional approach (without walrus operator)
print("WITHOUT walrus operator:")
n = 10
if n > 5:
    print(f"n = {n}, which is greater than 5")

print()

# With walrus operator (assign and check in one line)
print("WITH walrus operator:")
if (n := 10) > 5:
    print(f"n = {n}, which is greater than 5")

print()

# Another example
print("Getting user input (simulated):")
# Without walrus
user_input = "hello"
if user_input:
    print(f"You entered: {user_input}")

# With walrus
if user_input := "world":
    print(f"You entered: {user_input}")

print()

# ============================================
# 2. WALRUS IN IF STATEMENTS
# ============================================

print("=" * 50)
print("2. WALRUS IN IF STATEMENTS")
print("=" * 50)


# Example 1: Avoiding repeated function calls
def get_data():
    """Simulate expensive function call"""
    print("  (Fetching data...)")
    return {"status": "success", "data": [1, 2, 3, 4, 5]}


# Without walrus (calls get_data twice)
print("WITHOUT walrus (inefficient):")
if get_data()["status"] == "success":
    result = get_data()  # Called again!
    print(f"Data: {result['data']}")

print()

# With walrus (calls get_data only once)
print("WITH walrus (efficient):")
if (result := get_data())["status"] == "success":
    print(f"Data: {result['data']}")

print()


# Example 2: Processing and checking results
def calculate_score(points):
    """Calculate score from points"""
    return points * 10


print("Checking score threshold:")
points = 8

# Without walrus
score = calculate_score(points)
if score >= 75:
    print(f"Pass! Score: {score}")
else:
    print(f"Fail. Score: {score}")

# With walrus
if (score := calculate_score(points)) >= 75:
    print(f"Pass! Score: {score}")
else:
    print(f"Fail. Score: {score}")

print()

# ============================================
# 3. WALRUS IN WHILE LOOPS
# ============================================

print("=" * 50)
print("3. WALRUS IN WHILE LOOPS")
print("=" * 50)

# Example 1: Reading data until a condition
print("Example 1: Reading numbers until zero")

# Without walrus
numbers = [5, 3, 8, 2, 0, 9, 1]
index = 0
num = numbers[index]
while num != 0:
    print(f"Processing: {num}")
    index += 1
    if index < len(numbers):
        num = numbers[index]
    else:
        break

print()

# With walrus (more concise)
numbers = [5, 3, 8, 2, 0, 9, 1]
index = 0
while (num := numbers[index] if index < len(numbers) else 0) != 0:
    print(f"Processing: {num}")
    index += 1

print()

# Example 2: Processing chunks of data
print("Example 2: Processing data in chunks")

data = "Hello World Python Programming"
words = data.split()
word_iter = iter(words)

# With walrus operator
chunk_size = 2
chunks_processed = 0
while (chunk := [next(word_iter, None) for _ in range(chunk_size)]) and any(chunk):
    valid_chunk = [w for w in chunk if w is not None]
    print(f"Chunk {chunks_processed + 1}: {valid_chunk}")
    chunks_processed += 1

print()

# Example 3: File reading pattern (simulated)
print("Example 3: File reading pattern")

# Simulated file lines
file_lines = ["line 1", "line 2", "line 3", ""]
line_index = 0


def read_line():
    """Simulate reading a line from file"""
    global line_index
    if line_index < len(file_lines):
        line = file_lines[line_index]
        line_index += 1
        return line
    return ""


# With walrus - classic file reading pattern
while line := read_line():
    print(f"Read: '{line}'")

print()

# ============================================
# 4. WALRUS IN LIST COMPREHENSIONS
# ============================================

print("=" * 50)
print("4. WALRUS IN LIST COMPREHENSIONS")
print("=" * 50)

# Example 1: Avoid repeated calculations
print("Example 1: Calculating and filtering")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without walrus (calculates square twice)
result = [n**2 for n in numbers if n**2 > 25]
print(f"Squares > 25 (without walrus): {result}")

# With walrus (calculates square once)
result = [square for n in numbers if (square := n**2) > 25]
print(f"Squares > 25 (with walrus): {result}")

print()

# Example 2: Complex transformations
print("Example 2: Complex transformations")


def expensive_operation(x):
    """Simulate expensive computation"""
    return x**3 + 2 * x**2 + x


# Without walrus
result = [expensive_operation(n) for n in range(5) if expensive_operation(n) % 2 == 0]
print(f"Without walrus: {result}")

# With walrus (more efficient)
result = [value for n in range(5) if (value := expensive_operation(n)) % 2 == 0]
print(f"With walrus: {result}")

print()

# Example 3: Filtering with string processing
print("Example 3: String processing")

words = ["hello", "world", "python", "programming", "code"]

# Get words where uppercase version is different
result = [upper for word in words if (upper := word.upper()) != word]
print(f"Uppercase words: {result}")

print()

# ============================================
# 5. WALRUS WITH REGULAR EXPRESSIONS
# ============================================

print("=" * 50)
print("5. WALRUS WITH REGULAR EXPRESSIONS")
print("=" * 50)

# Example: Matching and using regex results
text = "Contact: John at john@email.com or call 555-1234"

print("Finding email:")
# Without walrus
match = re.search(r"(\w+@\w+\.\w+)", text)
if match:
    print(f"Email found: {match.group(1)}")

# With walrus
if match := re.search(r"(\w+@\w+\.\w+)", text):
    print(f"Email found: {match.group(1)}")

print()

print("Finding phone number:")
# With walrus - cleaner code
if match := re.search(r"(\d{3}-\d{4})", text):
    print(f"Phone found: {match.group(1)}")

print()

# Multiple pattern matching
patterns = [
    (r"\w+@\w+\.\w+", "Email"),
    (r"\d{3}-\d{4}", "Phone"),
    (r"\b[A-Z][a-z]+\b", "Name"),
]

print("Finding patterns:")
for pattern, label in patterns:
    if match := re.search(pattern, text):
        print(f"{label}: {match.group()}")

print()

# ============================================
# 6. WALRUS IN NESTED STRUCTURES
# ============================================

print("=" * 50)
print("6. WALRUS IN NESTED STRUCTURES")
print("=" * 50)

# Example 1: Nested dictionaries
print("Example 1: Accessing nested data")

data = {"user": {"profile": {"name": "Alice", "age": 25}}}

# With walrus - check and use in one step
if profile := data.get("user", {}).get("profile"):
    print(f"User: {profile.get('name')}, Age: {profile.get('age')}")

print()

# Example 2: Processing nested lists
print("Example 2: Processing nested lists")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Find first row with sum > 10
for row in matrix:
    if (row_sum := sum(row)) > 10:
        print(f"Found row with sum {row_sum}: {row}")
        break

print()

# ============================================
# 7. PRACTICAL USE CASES
# ============================================

print("=" * 50)
print("7. PRACTICAL USE CASES")
print("=" * 50)

# Use Case 1: Input validation
print("Use Case 1: Input validation")


def validate_username(username):
    """Validate username"""
    if len(username) < 3:
        return None
    return username.lower()


test_users = ["Alice", "Bo", "Charlie", "X"]

for user in test_users:
    if valid_name := validate_username(user):
        print(f"✓ Valid username: {valid_name}")
    else:
        print(f"✗ Invalid username: {user}")

print()

# Use Case 2: Caching expensive operations
print("Use Case 2: Caching results")


def compute_fibonacci(n, cache={}):
    """Compute Fibonacci with caching"""
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = compute_fibonacci(n - 1, cache) + compute_fibonacci(n - 2, cache)
    return cache[n]


# Using walrus to compute and check
n = 10
if (result := compute_fibonacci(n)) > 100:
    print(f"Fibonacci({n}) = {result} (greater than 100)")
else:
    print(f"Fibonacci({n}) = {result} (less than or equal to 100)")

print()

# Use Case 3: API response handling (simulated)
print("Use Case 3: API response handling")


def fetch_user_data(user_id):
    """Simulate API call"""
    database = {
        1: {"name": "Alice", "status": "active"},
        2: {"name": "Bob", "status": "inactive"},
    }
    return database.get(user_id)


user_id = 1
# With walrus - fetch and check in one step
if (user_data := fetch_user_data(user_id)) and user_data.get("status") == "active":
    print(f"Active user found: {user_data['name']}")
else:
    print(f"User {user_id} not found or inactive")

print()

# Use Case 4: Finding first match
print("Use Case 4: Finding first matching element")


def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [15, 16, 17, 18, 19, 20]

# Find first prime using walrus
first_prime = next((num for num in numbers if is_prime(num)), None)
print(f"First prime: {first_prime}")

# Or with walrus in different context
for num in numbers:
    if is_prime(num):
        first_prime = num
        break

print(f"First prime (loop): {first_prime}")

print()

# ============================================
# 8. DICTIONARY COMPREHENSIONS WITH WALRUS
# ============================================

print("=" * 50)
print("8. DICTIONARY COMPREHENSIONS WITH WALRUS")
print("=" * 50)

# Example: Transform and filter
print("Example: Processing scores")

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 92, 78, 95, 88]


# Create dict with grade calculation
def calculate_grade(score):
    """Calculate letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    return "F"


# With walrus in dict comprehension
result = {
    name: grade
    for name, score in zip(students, scores)
    if (grade := calculate_grade(score)) in ["A", "B"]
}

print("Students with A or B grades:")
for name, grade in result.items():
    print(f"  {name}: {grade}")

print()

# ============================================
# 9. WALRUS OPERATOR GOTCHAS AND LIMITATIONS
# ============================================

print("=" * 50)
print("9. GOTCHAS AND LIMITATIONS")
print("=" * 50)

print("Gotcha 1: Parentheses are often required")
# This works
if (x := 10) > 5:
    print(f"✓ Correct: x = {x}")

# This would cause SyntaxError without parentheses in some contexts
# x := 10  # SyntaxError!

print()

print("Gotcha 2: Walrus vs regular assignment")
# Regular assignment doesn't return a value for use in expressions
# y = 10 > 5  # This assigns False to y, not 10
y = 10
result = y > 5
print(f"Regular assignment: y = {y}, result = {result}")

# Walrus assigns AND uses the value
result = (z := 10) > 5
print(f"Walrus: z = {z}, result = {result}")

print()

print("Gotcha 3: Scope in comprehensions")
# The variable persists after the comprehension
numbers = [1, 2, 3, 4, 5]
result = [square for n in numbers if (square := n**2) > 10]
print(f"Result: {result}")
print(f"Variable 'square' still exists: {square}")  # Last assigned value

print()

print("Gotcha 4: Can't use in f-strings (in older Python versions)")
# This works in Python 3.8+
value = 42
text = f"The value is {value}"
print(text)

# But walrus in f-string requires Python 3.8+
text = f"The value is {(new_val := 100)}"
print(text)
print(f"new_val = {new_val}")

print()

# ============================================
# 10. WHEN TO USE vs WHEN NOT TO USE
# ============================================

print("=" * 50)
print("10. WHEN TO USE vs WHEN NOT TO USE")
print("=" * 50)

print(
    """
WHEN TO USE WALRUS OPERATOR:

✓ In if statements to avoid duplicate calls
  if (result := expensive_function()) is not None:
      use(result)

✓ In while loops for cleaner iteration
  while (line := file.readline()):
      process(line)

✓ In comprehensions to avoid recalculation
  [y for x in data if (y := transform(x)) > threshold]

✓ With regex to capture and check matches
  if (match := pattern.search(text)):
      use(match.group())

✓ To reduce repeated function calls
  if (data := fetch_data()) and data.get('status') == 'ok':
      process(data)


WHEN NOT TO USE:

✗ When it makes code harder to read
  Bad: if (x := (y := (z := compute()))) > 0:

✗ When a simple assignment is clearer
  Bad: if (x := 5):
  Good: x = 5
        if x:

✗ When you don't need the variable later
  Bad: if (result := x > 5):
  Good: if x > 5:

✗ In complex nested expressions
  Gets confusing quickly!

✗ Just to save a line of code
  Readability matters more than brevity


BEST PRACTICES:

1. Use it to eliminate redundancy
2. Keep expressions simple
3. Use meaningful variable names
4. Don't overuse it
5. Prioritize readability
6. Add comments for complex usage
"""
)

# ============================================
# 11. PERFORMANCE COMPARISON
# ============================================

print("=" * 50)
print("11. PERFORMANCE COMPARISON")
print("=" * 50)


def slow_function(x):
    """Simulate slow function"""
    time.sleep(0.001)  # 1ms delay
    return x**2


# Without walrus (calls function twice)
print("Without walrus operator:")
start = time.time()
count = 0
for i in range(100):
    if slow_function(i) > 50:
        result = slow_function(i)  # Called again!
        count += 1
time_without = time.time() - start
print(f"Time: {time_without:.3f}s, Count: {count}")

# With walrus (calls function once)
print("\nWith walrus operator:")
start = time.time()
count = 0
for i in range(100):
    if (result := slow_function(i)) > 50:
        count += 1
time_with = time.time() - start
print(f"Time: {time_with:.3f}s, Count: {count}")

print(f"\nSpeedup: {time_without/time_with:.2f}x faster")

print()

# ============================================
# 12. REAL-WORLD EXAMPLES
# ============================================

print("=" * 50)
print("12. REAL-WORLD EXAMPLES")
print("=" * 50)

# Example 1: Log file parsing
print("Example 1: Log file parsing")

log_lines = [
    "2024-01-01 INFO: System started",
    "2024-01-01 ERROR: Connection failed",
    "2024-01-01 WARNING: Low memory",
    "2024-01-01 ERROR: Database error",
]

error_pattern = re.compile(r"ERROR: (.+)")

print("Errors found:")
for line in log_lines:
    if match := error_pattern.search(line):
        print(f"  - {match.group(1)}")

print()

# Example 2: Data validation pipeline
print("Example 2: Data validation pipeline")


def validate_email(email):
    """Validate email format"""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return email.lower()
    return None


emails = ["alice@example.com", "invalid-email", "bob@test.com", "bad@"]

valid_emails = [
    clean_email for email in emails if (clean_email := validate_email(email))
]

print(f"Valid emails: {valid_emails}")

print()

# Example 3: Configuration loading
print("Example 3: Configuration with fallbacks")


def get_config(key, config_dict):
    """Get config value"""
    return config_dict.get(key)


config = {"host": "localhost", "port": 8080, "timeout": 30}

# Using walrus with fallback
if (host := get_config("host", config)) and (port := get_config("port", config)):
    print(f"Connecting to {host}:{port}")

# With fallback value
database = get_config("database", config) or "default_db"
print(f"Using database: {database}")

print()

"""
SUMMARY
=======

The Walrus Operator (:=)

What is it?
- Assignment expression operator
- Introduced in Python 3.8 (PEP 572)
- Assigns AND returns a value
- Named "walrus" because := looks like a walrus

Syntax:
    variable := expression

Key Benefits:
1. Avoid duplicate function calls
2. Reduce code repetition
3. Improve performance
4. Make code more concise
5. Better resource utilization

Common Use Cases:
- If statements (assign and check)
- While loops (read and check)
- List comprehensions (calculate once)
- Regular expressions (match and use)
- Input validation
- API response handling

Requirements:
- Python 3.8 or higher
- Parentheses often required
- Use judiciously for readability

Best Practices:
✓ Use to eliminate redundancy
✓ Keep expressions simple
✓ Use meaningful variable names
✓ Prioritize readability
✗ Don't overuse
✗ Avoid complex nesting
✗ Don't sacrifice clarity

Remember:
"Just because you can use the walrus operator doesn't mean you should.
Use it when it improves code clarity and efficiency, not just to save lines."
"""

print("=" * 50)
print("END OF WALRUS OPERATOR EXPLANATION")
print("=" * 50)
