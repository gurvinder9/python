"""
Functions in Python
===================

A function is a reusable block of code that performs a specific task.
Functions help organize code, make it more readable, and reduce repetition.

Key Concepts:
- Functions are defined using the 'def' keyword
- Functions can accept input (parameters) and return output
- Functions create their own scope
- Functions are first-class objects in Python
- Functions promote DRY (Don't Repeat Yourself) principle

Why Use Functions?
- Code reusability
- Better organization
- Easier testing and debugging
- Abstraction and modularity
- Easier maintenance

Syntax:
    def function_name(parameters):
        '''Docstring'''
        # function body
        return value
"""

# ============================================
# 1. BASIC FUNCTION DEFINITION
# ============================================

print("=" * 50)
print("1. BASIC FUNCTION DEFINITION")
print("=" * 50)


# Simple function with no parameters
def greet():
    """Print a greeting message"""
    print("Hello, World!")


# Calling the function
greet()

print()


# Function with parameters
def greet_person(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")

print()


# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers and print the result"""
    result = a + b
    print(f"{a} + {b} = {result}")


add_numbers(5, 3)
add_numbers(10, 20)

print()

# ============================================
# 2. RETURN STATEMENTS
# ============================================

print("=" * 50)
print("2. RETURN STATEMENTS")
print("=" * 50)


# Function that returns a value
def multiply(x, y):
    """Multiply two numbers and return the result"""
    return x * y


result = multiply(4, 5)
print(f"Result: {result}")

# Using return value in expressions
print(f"Double of 6 * 7: {multiply(6, 7) * 2}")

print()


# Function returning multiple values (as tuple)
def get_min_max(numbers):
    """Return minimum and maximum from a list"""
    return min(numbers), max(numbers)


nums = [3, 7, 2, 9, 1, 5]
minimum, maximum = get_min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")

print()


# Function with early return
def is_even(number):
    """Check if number is even"""
    if number % 2 == 0:
        return True
    return False


print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

print()


# Function with no explicit return (returns None)
def print_message(msg):
    """Print a message without returning anything"""
    print(f"Message: {msg}")


result = print_message("Hello")
print(f"Return value: {result}")  # None

print()

# ============================================
# 3. FUNCTION PARAMETERS
# ============================================

print("=" * 50)
print("3. FUNCTION PARAMETERS")
print("=" * 50)


# Positional parameters
def describe_person(name, age, city):
    """Describe a person with positional parameters"""
    print(f"{name} is {age} years old and lives in {city}")


describe_person("Alice", 25, "NYC")

print()


# Keyword arguments
def create_profile(name, age, city):
    """Create a profile using keyword arguments"""
    print(f"Name: {name}, Age: {age}, City: {city}")


# Can be called with keyword arguments in any order
create_profile(age=30, name="Bob", city="LA")
create_profile("Charlie", city="Chicago", age=35)

print()


# Default parameters
def greet_with_default(name="Guest", greeting="Hello"):
    """Greet with default parameters"""
    print(f"{greeting}, {name}!")


greet_with_default()  # Uses defaults
greet_with_default("Alice")  # Overrides name
greet_with_default("Bob", "Hi")  # Overrides both
greet_with_default(greeting="Hey")  # Override only greeting

print()


# Mix of positional and default parameters
def calculate_price(base_price, tax_rate=0.08, discount=0):
    """Calculate final price with tax and discount"""
    subtotal = base_price * (1 + tax_rate)
    final_price = subtotal * (1 - discount)
    return final_price


print(f"Price 1: ${calculate_price(100):.2f}")
print(f"Price 2: ${calculate_price(100, 0.10):.2f}")
print(f"Price 3: ${calculate_price(100, 0.10, 0.15):.2f}")

print()

# ============================================
# 4. *args - VARIABLE POSITIONAL ARGUMENTS
# ============================================

print("=" * 50)
print("4. *args - VARIABLE POSITIONAL ARGUMENTS")
print("=" * 50)


# Function accepting any number of arguments
def sum_all(*args):
    """Sum any number of arguments"""
    print(f"Arguments: {args}")
    print(f"Type: {type(args)}")  # tuple
    return sum(args)


print(f"Sum: {sum_all(1, 2, 3)}")
print(f"Sum: {sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")
print(f"Sum: {sum_all()}")  # Empty tuple

print()


# Combining regular parameters with *args
def greet_all(greeting, *names):
    """Greet multiple people"""
    for name in names:
        print(f"{greeting}, {name}!")


greet_all("Hello", "Alice", "Bob", "Charlie")

print()


# Real-world example: finding maximum
def find_maximum(*numbers):
    """Find maximum from any number of arguments"""
    if not numbers:
        return None
    return max(numbers)


print(f"Max: {find_maximum(3, 7, 2, 9, 1)}")
print(f"Max: {find_maximum(42)}")
print(f"Max: {find_maximum()}")

print()

# ============================================
# 5. **kwargs - VARIABLE KEYWORD ARGUMENTS
# ============================================

print("=" * 50)
print("5. **kwargs - VARIABLE KEYWORD ARGUMENTS")
print("=" * 50)


# Function accepting any number of keyword arguments
def print_info(**kwargs):
    """Print information from keyword arguments"""
    print(f"Arguments: {kwargs}")
    print(f"Type: {type(kwargs)}")  # dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25, city="NYC")
print()
print_info(product="Laptop", price=999, brand="Apple")

print()


# Combining *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts any arguments"""
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")


flexible_function(1, 2, 3, name="Alice", age=25)

print()


# Real-world example: creating user profiles
def create_user_profile(username, email, **additional_info):
    """Create user profile with required and optional fields"""
    profile = {"username": username, "email": email}
    profile.update(additional_info)
    return profile


user1 = create_user_profile("alice", "alice@email.com", age=25, city="NYC")
user2 = create_user_profile(
    "bob", "bob@email.com", country="USA", occupation="Developer"
)

print("User 1:", user1)
print("User 2:", user2)

print()

# ============================================
# 6. LAMBDA FUNCTIONS (Anonymous Functions)
# ============================================

print("=" * 50)
print("6. LAMBDA FUNCTIONS")
print("=" * 50)

# Basic lambda function
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"Sum: {add(3, 7)}")

# Lambda in sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]

# Sort by score (second element)
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Students sorted by score:")
for name, score in sorted_students:
    print(f"{name}: {score}")

print()

# Lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Lambda with map
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")

print()

# ============================================
# 7. SCOPE (Local vs Global)
# ============================================

print("=" * 50)
print("7. SCOPE (Local vs Global)")
print("=" * 50)

# Global variable
global_var = "I'm global"


def test_scope():
    """Test variable scope"""
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")


test_scope()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would raise NameError

print()

# Modifying global variable
counter = 0


def increment():
    """Increment global counter"""
    global counter
    counter += 1
    print(f"Counter: {counter}")


increment()
increment()
increment()

print()


# Nested scope
def outer():
    """Outer function"""
    outer_var = "outer"

    def inner():
        """Inner function"""
        inner_var = "inner"
        print(f"Inner can access: {outer_var} and {inner_var}")

    inner()
    print(f"Outer can access: {outer_var}")
    # print(inner_var)  # This would raise NameError


outer()

print()

# ============================================
# 8. DOCSTRINGS
# ============================================

print("=" * 50)
print("8. DOCSTRINGS")
print("=" * 50)


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle

    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width


# Accessing docstring
print("Function docstring:")
print(calculate_area.__doc__)

print()

# Using help()
print("Help information:")
help(calculate_area)

print()

# ============================================
# 9. TYPE HINTS (Function Annotations)
# ============================================

print("=" * 50)
print("9. TYPE HINTS")
print("=" * 50)


def add_numbers_typed(a: int, b: int) -> int:
    """Add two integers with type hints"""
    return a + b


print(f"Sum: {add_numbers_typed(5, 3)}")


def greet_typed(name: str, age: int) -> str:
    """Create greeting with type hints"""
    return f"{name} is {age} years old"


print(greet_typed("Alice", 25))


def process_list(items: list[int]) -> list[int]:
    """Process list of integers"""
    return [x * 2 for x in items]


print(f"Processed: {process_list([1, 2, 3, 4])}")

print()

# ============================================
# 10. RECURSION
# ============================================

print("=" * 50)
print("10. RECURSION")
print("=" * 50)


# Factorial using recursion
def factorial(n):
    """Calculate factorial recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")

print()


# Fibonacci using recursion
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")
print("\n")


# Countdown using recursion
def countdown(n):
    """Countdown from n to 1"""
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)


countdown(5)

print()

# ============================================
# 11. HIGHER-ORDER FUNCTIONS
# ============================================

print("=" * 50)
print("11. HIGHER-ORDER FUNCTIONS")
print("=" * 50)


# Function that takes another function as parameter
def apply_operation(numbers, operation):
    """Apply operation to each number"""
    return [operation(num) for num in numbers]


def double(x):
    return x * 2


def square(x):
    return x**2


nums = [1, 2, 3, 4, 5]
print(f"Original: {nums}")
print(f"Doubled: {apply_operation(nums, double)}")
print(f"Squared: {apply_operation(nums, square)}")

print()


# Function that returns another function
def multiplier(factor):
    """Return a function that multiplies by factor"""

    def multiply(x):
        return x * factor

    return multiply


times_2 = multiplier(2)
times_3 = multiplier(3)
times_10 = multiplier(10)

print(f"5 × 2 = {times_2(5)}")
print(f"5 × 3 = {times_3(5)}")
print(f"5 × 10 = {times_10(5)}")

print()

# ============================================
# 12. NESTED FUNCTIONS
# ============================================

print("=" * 50)
print("12. NESTED FUNCTIONS")
print("=" * 50)


def outer_function(text):
    """Outer function containing nested functions"""

    def inner_function():
        """Inner function that uses outer variable"""
        print(f"Inner: {text}")

    inner_function()
    print(f"Outer: {text}")


outer_function("Hello")

print()


# Closure example
def make_counter():
    """Create a counter using closure"""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter1 = make_counter()
counter2 = make_counter()

print(f"Counter 1: {counter1()}")  # 1
print(f"Counter 1: {counter1()}")  # 2
print(f"Counter 2: {counter2()}")  # 1
print(f"Counter 1: {counter1()}")  # 3

print()

# ============================================
# 13. DECORATORS (Basic Introduction)
# ============================================

print("=" * 50)
print("13. DECORATORS (Basic Introduction)")
print("=" * 50)


# Simple decorator
def my_decorator(func):
    """Simple decorator that adds behavior"""

    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@my_decorator
def say_hello():
    """Function to be decorated"""
    print("Hello!")


say_hello()

print()


# Decorator with arguments
def repeat(times):
    """Decorator that repeats function call"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet_decorated(name):
    """Function that will be repeated"""
    print(f"Hello, {name}!")


greet_decorated("Alice")

print()

# ============================================
# 14. PRACTICAL EXAMPLES
# ============================================

print("=" * 50)
print("14. PRACTICAL EXAMPLES")
print("=" * 50)


# Example 1: Input validation
def validate_age(age):
    """Validate age input"""
    if not isinstance(age, int):
        return False, "Age must be an integer"
    if age < 0:
        return False, "Age cannot be negative"
    if age > 150:
        return False, "Age seems unrealistic"
    return True, "Valid age"


test_ages = [25, -5, 200, "abc"]
for age in test_ages:
    valid, message = validate_age(age)
    print(f"Age {age}: {message}")

print()


# Example 2: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9


print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

print()


# Example 3: Calculate statistics
def calculate_stats(numbers):
    """Calculate basic statistics"""
    if not numbers:
        return None

    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    sorted_nums = sorted(numbers)

    # Median
    mid = count // 2
    if count % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]

    return {
        "count": count,
        "sum": total,
        "mean": mean,
        "median": median,
        "min": min(numbers),
        "max": max(numbers),
    }


data = [23, 45, 67, 12, 89, 34, 56, 78]
stats = calculate_stats(data)
print("Statistics:")
for key, value in stats.items():
    print(f"{key.capitalize()}: {value}")

print()


# Example 4: Password validator
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password too short (min 8 characters)"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if not has_upper:
        return False, "Password needs uppercase letter"
    if not has_lower:
        return False, "Password needs lowercase letter"
    if not has_digit:
        return False, "Password needs digit"
    if not has_special:
        return False, "Password needs special character"

    return True, "Strong password"


passwords = ["weak", "StrongPass123!", "NoSpecial123", "short1!"]
for pwd in passwords:
    valid, msg = validate_password(pwd)
    print(f"'{pwd}': {msg}")

print()

# ============================================
# 15. BEST PRACTICES
# ============================================

print("=" * 50)
print("15. BEST PRACTICES")
print("=" * 50)

print(
    """
Best Practices for Writing Functions:

1. Single Responsibility Principle
   - Each function should do ONE thing well
   - If a function does too much, split it

2. Naming Conventions
   - Use descriptive, lowercase names with underscores
   - Verbs for functions that perform actions
   - Use clear parameter names

3. Documentation
   - Always include docstrings
   - Explain parameters and return values
   - Include examples if complex

4. Function Length
   - Keep functions short (typically < 20-30 lines)
   - If too long, break into smaller functions

5. Parameters
   - Limit number of parameters (max 3-5)
   - Use *args and **kwargs when appropriate
   - Put required parameters first, optional last

6. Return Values
   - Be consistent with return types
   - Return early for special cases
   - Return None explicitly if no value

7. Side Effects
   - Minimize side effects (modifying global state)
   - Prefer pure functions when possible
   - Make side effects explicit in function name

8. Error Handling
   - Validate inputs
   - Use exceptions for error conditions
   - Provide meaningful error messages

9. Testing
   - Write testable functions
   - Keep functions pure when possible
   - Use type hints for clarity

10. DRY Principle
    - Don't Repeat Yourself
    - Extract common code into functions
    - Reuse instead of duplicating code
"""
)

# ============================================
# 16. COMMON PATTERNS
# ============================================

print("=" * 50)
print("16. COMMON PATTERNS")
print("=" * 50)


# Pattern 1: Guard clauses (early returns)
def process_data(data):
    """Process data with guard clauses"""
    # Early returns for special cases
    if data is None:
        return None

    if not data:
        return []

    if not isinstance(data, list):
        return None

    # Main logic
    return [x * 2 for x in data]


print(f"Process None: {process_data(None)}")
print(f"Process empty: {process_data([])}")
print(f"Process data: {process_data([1, 2, 3])}")

print()


# Pattern 2: Factory functions
def create_person(name, age):
    """Factory function to create person dictionary"""
    return {"name": name, "age": age, "type": "person"}


person1 = create_person("Alice", 25)
person2 = create_person("Bob", 30)
print(f"Person 1: {person1}")
print(f"Person 2: {person2}")

print()


# Pattern 3: Pipeline pattern
def remove_spaces(text):
    """Remove spaces from text"""
    return text.replace(" ", "")


def to_uppercase(text):
    """Convert text to uppercase"""
    return text.upper()


def add_prefix(text, prefix=">>>"):
    """Add prefix to text"""
    return f"{prefix} {text}"


# Chaining functions
text = "hello world"
result = add_prefix(to_uppercase(remove_spaces(text)))
print(f"Pipeline result: {result}")

print()

"""
SUMMARY
=======

What are Functions?
- Reusable blocks of code that perform specific tasks
- Defined using 'def' keyword
- Can accept parameters and return values
- First-class objects in Python

Key Components:
1. Function name (lowercase with underscores)
2. Parameters (input)
3. Function body (code to execute)
4. Return statement (output)
5. Docstring (documentation)

Types of Parameters:
- Positional parameters
- Keyword parameters
- Default parameters
- *args (variable positional)
- **kwargs (variable keyword)

Advanced Concepts:
- Lambda functions (anonymous)
- Recursion (function calling itself)
- Higher-order functions (functions as parameters/returns)
- Nested functions and closures
- Decorators (modify function behavior)

When to Use Functions:
- Code is repeated multiple times
- Complex logic needs organization
- Need to abstract functionality
- Want to improve code readability
- Need to test specific functionality

Benefits:
- Code reusability
- Better organization
- Easier debugging
- Improved maintainability
- Abstraction and modularity
- Testability

Best Practices:
- Single responsibility
- Clear naming
- Good documentation
- Proper parameter handling
- Consistent return values
- Minimal side effects
- Input validation
- Keep functions short
"""

print("=" * 50)
print("END OF FUNCTIONS EXPLANATION")
print("=" * 50)
