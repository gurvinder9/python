"""
12. Conditional Logic (Control Flow) in Python

Conditional logic allows your program to make decisions based on different conditions.
Python provides several types of conditional statements and operators.

TYPES OF CONDITIONAL LOGIC IN PYTHON:
1. if statements
2. elif (else if) statements
3. else statements
4. Nested conditional statements
5. Ternary operators (conditional expressions)
6. Logical operators (and, or, not)
7. Comparison operators (==, !=, <, >, <=, >=)
8. Membership operators (in, not in)
9. Identity operators (is, is not)
10. Short-circuit evaluation
"""

print("=" * 60)
print("CONDITIONAL LOGIC IN PYTHON")
print("=" * 60)

# =============================================================================
# 1. BASIC IF STATEMENTS
# =============================================================================
print("\n1. BASIC IF STATEMENTS")
print("-" * 30)

age = 18
if age >= 18:
    print("You are an adult!")

temperature = 25
if temperature > 30:
    print("It's hot outside!")

# Multiple conditions in one if statement
score = 85
if score >= 80 and score < 90:
    print("Good job! You got a B grade!")

# =============================================================================
# 2. IF-ELSE STATEMENTS
# =============================================================================
print("\n2. IF-ELSE STATEMENTS")
print("-" * 30)

age = 16
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# Another example
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# =============================================================================
# 3. IF-ELIF-ELSE STATEMENTS (Multiple Conditions)
# =============================================================================
print("\n3. IF-ELIF-ELSE STATEMENTS")
print("-" * 30)

score = 92
if score >= 90:
    grade = "A"
    print(f"Excellent! Grade: {grade}")
elif score >= 80:
    grade = "B"
    print(f"Good! Grade: {grade}")
elif score >= 70:
    grade = "C"
    print(f"Average. Grade: {grade}")
elif score >= 60:
    grade = "D"
    print(f"Below average. Grade: {grade}")
else:
    grade = "F"
    print(f"Failed. Grade: {grade}")

# Temperature example
temp = 15
if temp > 30:
    weather = "Hot"
elif temp > 20:
    weather = "Warm"
elif temp > 10:
    weather = "Cool"
else:
    weather = "Cold"
print(f"The weather is {weather}")

# =============================================================================
# 4. NESTED CONDITIONAL STATEMENTS
# =============================================================================
print("\n4. NESTED CONDITIONAL STATEMENTS")
print("-" * 30)

age = 20
has_license = True

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a driver's license")
else:
    print("You are a minor")
    if age >= 16:
        print("You can get a learner's permit")
    else:
        print("You're too young to drive")

# Another nested example
weather = "sunny"
temperature = 25

if weather == "sunny":
    if temperature > 30:
        print("It's a hot sunny day - wear sunscreen!")
    elif temperature > 20:
        print("It's a pleasant sunny day")
    else:
        print("It's sunny but cool")
else:
    print("It's not sunny today")

# =============================================================================
# 5. TERNARY OPERATORS (Conditional Expressions)
# =============================================================================
print("\n5. TERNARY OPERATORS")
print("-" * 30)

# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Multiple ternary operators
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade: {grade}")

# Practical example
temperature = 25
clothing = "shorts" if temperature > 25 else "pants"
print(f"Wear {clothing}")

# =============================================================================
# 6. LOGICAL OPERATORS
# =============================================================================
print("\n6. LOGICAL OPERATORS")
print("-" * 30)

# AND operator - both conditions must be True
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive!")

# OR operator - at least one condition must be True
weather = "rainy"
if weather == "sunny" or weather == "cloudy":
    print("Good weather for outdoor activities")

# NOT operator - reverses the boolean value
is_weekend = False
if not is_weekend:
    print("It's a weekday")

# Combining multiple logical operators
age = 20
has_license = True
is_weekend = True

if age >= 18 and has_license and not is_weekend:
    print("You can drive to work!")
elif age >= 18 and has_license and is_weekend:
    print("You can drive for fun!")

# =============================================================================
# 7. COMPARISON OPERATORS
# =============================================================================
print("\n7. COMPARISON OPERATORS")
print("-" * 30)

a = 10
b = 20

# Equal to
if a == 10:
    print("a equals 10")

# Not equal to
if a != b:
    print("a is not equal to b")

# Less than
if a < b:
    print("a is less than b")

# Greater than
if b > a:
    print("b is greater than a")

# Less than or equal to
if a <= 10:
    print("a is less than or equal to 10")

# Greater than or equal to
if b >= 20:
    print("b is greater than or equal to 20")

# String comparisons
name1 = "Alice"
name2 = "Bob"
if name1 < name2:  # Alphabetical comparison
    print(f"{name1} comes before {name2} alphabetically")

# =============================================================================
# 8. MEMBERSHIP OPERATORS
# =============================================================================
print("\n8. MEMBERSHIP OPERATORS")
print("-" * 30)

# IN operator - checks if value is in a sequence
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is in the fruit list")

# NOT IN operator - checks if value is NOT in a sequence
if "grape" not in fruits:
    print("Grape is not in the fruit list")

# With strings
text = "Hello World"
if "World" in text:
    print("'World' is in the text")

# With dictionaries
person = {"name": "John", "age": 30, "city": "New York"}
if "age" in person:
    print("Age key exists in person dictionary")

# With ranges
if 5 in range(1, 10):
    print("5 is in the range from 1 to 9")

# =============================================================================
# 9. IDENTITY OPERATORS
# =============================================================================
print("\n9. IDENTITY OPERATORS")
print("-" * 30)

# IS operator - checks if two variables refer to the same object
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # Same reference

if list1 is list3:
    print("list1 and list3 refer to the same object")

if list1 is not list2:
    print("list1 and list2 are different objects (even though they have same content)")

# IS NOT operator
if list1 is not list2:
    print("list1 and list2 are not the same object")

# Common use case with None
value = None
if value is None:
    print("Value is None")

# =============================================================================
# 10. SHORT-CIRCUIT EVALUATION
# =============================================================================
print("\n10. SHORT-CIRCUIT EVALUATION")
print("-" * 30)


# Python stops evaluating as soon as it knows the result
def check_condition():
    print("This function was called!")
    return True


# With AND - if first condition is False, second won't be evaluated
if False and check_condition():
    print("This won't print")

# With OR - if first condition is True, second won't be evaluated
if True or check_condition():
    print("This will print, but check_condition won't be called")


# Practical example
def divide(a, b):
    return a / b


# Safe division using short-circuit evaluation
a, b = 10, 0
if b != 0 and divide(a, b) > 5:
    print("Division result is greater than 5")

# =============================================================================
# 11. COMPLEX CONDITIONAL EXAMPLES
# =============================================================================
print("\n11. COMPLEX CONDITIONAL EXAMPLES")
print("-" * 30)


# Student grading system
def calculate_grade(score, attendance):
    """Calculate grade based on score and attendance."""
    if attendance < 80:
        return "F (Poor attendance)"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Test the function
student_score = 85
student_attendance = 90
grade = calculate_grade(student_score, student_attendance)
print(f"Student grade: {grade}")


# Weather recommendation system
def weather_recommendation(temperature, weather, wind_speed):
    """Provide weather-based recommendations."""
    if weather == "sunny":
        if temperature > 30:
            return "It's hot! Stay hydrated and wear sunscreen."
        elif temperature > 20:
            return "Perfect weather! Great for outdoor activities."
        else:
            return "Sunny but cool. Bring a light jacket."
    elif weather == "rainy":
        if wind_speed > 20:
            return "Stormy weather! Stay indoors."
        else:
            return "Rainy day. Don't forget your umbrella!"
    elif weather == "cloudy":
        return "Cloudy day. Good for a walk or indoor activities."
    else:
        return "Check the weather forecast for more details."


# Test weather recommendations
recommendation = weather_recommendation(25, "sunny", 10)
print(f"Weather recommendation: {recommendation}")

# =============================================================================
# 12. COMMON PATTERNS AND BEST PRACTICES
# =============================================================================
print("\n12. COMMON PATTERNS AND BEST PRACTICES")
print("-" * 30)


# Pattern 1: Early return (guard clauses)
def process_user(user):
    """Process user with early returns."""
    if user is None:
        return "No user provided"

    if not user.get("name"):
        return "User name is required"

    if user.get("age", 0) < 18:
        return "User must be 18 or older"

    return f"Processing user: {user['name']}"


# Pattern 2: Using elif instead of multiple if statements
def get_day_type(day):
    """Get type of day."""
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        return "Weekday"
    elif day in ["Saturday", "Sunday"]:
        return "Weekend"
    else:
        return "Invalid day"


# Pattern 3: Chaining comparisons
def check_range(number):
    """Check if number is in range using chained comparisons."""
    if 0 <= number <= 100:
        return "Number is between 0 and 100"
    else:
        return "Number is outside the range"


# Test the patterns
user = {"name": "Alice", "age": 25}
result = process_user(user)
print(f"User processing: {result}")

day_type = get_day_type("Saturday")
print(f"Day type: {day_type}")

range_check = check_range(50)
print(f"Range check: {range_check}")
