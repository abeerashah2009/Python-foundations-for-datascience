# Lab 2: Control Flow in Python

## Lab Overview

This lab introduces **control flow in Python**, which allows programs to make decisions based on conditions.

In this lab, we worked with:

* `if` statements
* `if-else` statements
* `if-elif-else` statements
* Comparison operators
* Logical operators
* Nested `if` statements
* Input validation
* Error handling
* Debugging control-flow errors
* A practical temperature categorization program

---

# Objectives

By completing this lab, students will be able to:

* Understand conditional statements in Python.
* Use `if`, `elif`, and `else`.
* Compare values using comparison operators.
* Use `and`, `or`, and `not`.
* Create nested conditional statements.
* Validate user input.
* Handle common programming errors.
* Debug incorrect Python code.
* Build a practical temperature categorization program.

---

# Prerequisites

Before starting this lab, basic knowledge of the following is recommended:

* Python variables
* Python data types
* `input()`
* `print()`
* Type conversion
* Basic Python syntax
* Running Python scripts from the terminal

---

# Lab Environment

The lab was performed in a Linux-based cloud environment with Python installed.

Check Python:

```bash
python3 --version
```

Check the current directory:

```bash
pwd
```

List files:

```bash
ls -la
```

---

# Task 1: Basic Conditional Statements

## 1.1 Simple `if` Statement

The `if` statement executes a block of code only when a condition is true.

### Example

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")
    print("You can vote in elections.")

print("Program finished.")
```

### Run

```bash
python3 simple_if.py
```

### Key Concept

```text
if condition:
    code
```

If the condition is `True`, the indented code runs.

### Example

```text
age = 20
20 >= 18 → True
```

Therefore, the `if` block executes.

---

# 1.2 `if-else` Statement

An `if-else` statement provides two possible paths.

```python
score = int(input("Enter your test score (0-100): "))

if score >= 60:
    print("Congratulations! You passed the test.")
else:
    print("Sorry, you did not pass the test.")
```

### Run

```bash
python3 if_else.py
```

### Logic

```text
Condition True  → if block
Condition False → else block
```

### Example

```text
Score = 75

75 >= 60 → True
Result → Passed
```

---

# 1.3 `if-elif-else`

When there are multiple possible conditions, we can use `elif`.

```python
score = int(input("Enter your test score (0-100): "))

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

print(f"Score: {score}")
print(f"Grade: {grade}")
```

### Run

```bash
python3 grade_system.py
```

### Example

```text
95 → A
85 → B
75 → C
65 → D
55 → F
```

### Important Point

Python checks conditions from **top to bottom**.

Once a condition is true, its block executes and the remaining `elif` conditions are skipped.

---

# Task 2: Logical Operators

Logical operators allow multiple conditions to be combined.

Python provides three important logical operators:

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | All conditions must be True         |
| `or`     | At least one condition must be True |
| `not`    | Reverses the result                 |

---

# 2.1 `and` Operator

The `and` operator requires **all conditions** to be true.

Example:

```python
username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

if username == "student" and password == "python123" and age >= 13:
    print("Access granted!")
else:
    print("Access denied!")
```

### Run

```bash
python3 logical_and.py
```

### Example

```text
username = student
password = python123
age = 16
```

All conditions are true:

```text
True and True and True
```

Result:

```text
Access granted!
```

---

# 2.2 `or` Operator

The `or` operator requires **at least one condition** to be true.

Example:

```python
day = input("What day is it? ").lower()

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
```

### Run

```bash
python3 logical_or.py
```

### Example

```text
day = saturday
```

Evaluation:

```text
True or False
```

Result:

```text
It's the weekend!
```

---

# 2.3 `not` Operator

The `not` operator reverses a Boolean condition.

Example:

```python
is_raining = input("Is it raining? (yes/no): ").lower()

if not is_raining == "yes":
    print("You can go outside.")
else:
    print("Take an umbrella.")
```

### Run

```bash
python3 logical_not.py
```

### Concept

```text
not True  → False
not False → True
```

---

# Task 3: Temperature Categorization

This task combines conditional statements and logical operators into a practical program.

---

# 3.1 Basic Temperature Categorization

The program classifies temperature as:

* HOT
* COLD
* MILD

Example:

```python
temperature = float(input("Enter temperature in Fahrenheit: "))

if temperature >= 80:
    category = "hot"
elif temperature <= 50:
    category = "cold"
else:
    category = "mild"

print(f"Temperature category: {category.upper()}")
```

### Run

```bash
python3 temperature_categorizer.py
```

### Example

```text
90 → HOT
45 → COLD
65 → MILD
```

---

# 3.2 Nested `if` Statements

A nested `if` means placing one conditional statement inside another.

Example:

```python
if temperature >= 80:
    print("HOT")

    if humidity > 70:
        print("High humidity")
```

The inner condition is checked only after the outer condition is true.

### Structure

```text
if condition:
    if another_condition:
        code
```

---

# Advanced Temperature Categorizer

The advanced program considers:

* Temperature
* Humidity
* Sunny/cloudy weather
* Comfort level
* Weather recommendations

Example:

```python
temperature = float(input("Enter temperature in Fahrenheit: "))
humidity = float(input("Enter humidity percentage: "))
is_sunny = input("Is it sunny? (yes/no): ").lower()

if temperature >= 80:

    if humidity > 70:
        comfort_level = "Very Uncomfortable"
    elif humidity > 50:
        comfort_level = "Uncomfortable"
    else:
        comfort_level = "Tolerable"

elif temperature <= 50:

    if temperature <= 32:
        comfort_level = "Cold"
    else:
        comfort_level = "Cool"

else:

    if temperature >= 70 and humidity < 60 and is_sunny == "yes":
        comfort_level = "Perfect"
    else:
        comfort_level = "Comfortable"

print(f"Comfort Level: {comfort_level}")
```

---

# 3.3 Input Validation

Input validation makes a program safer and more reliable.

For example, the user might enter:

```text
hello
```

when the program expects a number.

Using `try-except` allows the program to handle this error.

Example:

```python
while True:
    try:
        temperature = float(input("Enter temperature: "))
        break
    except ValueError:
        print("Please enter a valid number.")
```

### Why Input Validation Matters

Without validation:

```text
hello → ValueError
```

With validation:

```text
hello → Error message → Ask again
```

---

# Task 4: Debugging and Troubleshooting

Debugging means finding and fixing errors in a program.

Common control-flow errors include:

* Incorrect indentation
* Missing colon
* Incorrect comparison operator
* Incorrect logical conditions
* Unreachable conditions
* Incorrect data types

---

# Common Error 1: Incorrect Indentation

### Wrong

```python
if temperature > 80:
print("Hot weather")
```

### Correct

```python
if temperature > 80:
    print("Hot weather")
```

Python uses indentation to define code blocks.

The standard indentation is:

```text
4 spaces
```

---

# Common Error 2: `=` vs `==`

### Assignment

```python
temperature = 80
```

`=` assigns a value.

### Comparison

```python
temperature == 80
```

`==` checks whether two values are equal.

### Correct

```python
if temperature == 80:
    print("Temperature is 80")
```

---

# Common Error 3: Missing Colon

### Wrong

```python
if temperature > 80
```

### Correct

```python
if temperature > 80:
```

Python conditional statements require a colon at the end.

---

# Common Error 4: Incorrect Data Type

### Problem

```python
temperature = input("Enter temperature: ")

if temperature > 80:
```

`input()` returns a string.

### Correct

```python
temperature = float(input("Enter temperature: "))
```

Now the value can be compared numerically.

---

# Common Error 5: Unreachable Condition

Consider:

```python
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
elif temperature > 100:
    print("This will never execute")
```

The final condition is unreachable because values greater than 100 have already been handled by the first condition.

### Correct Ordering

```python
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
```

---

# Important Comparison Operators

Python provides several comparison operators.

| Operator | Meaning               | Example   |
| -------- | --------------------- | --------- |
| `==`     | Equal                 | `x == 10` |
| `!=`     | Not equal             | `x != 10` |
| `>`      | Greater than          | `x > 10`  |
| `<`      | Less than             | `x < 10`  |
| `>=`     | Greater than or equal | `x >= 10` |
| `<=`     | Less than or equal    | `x <= 10` |

These operators return:

```text
True
```

or

```text
False
```

---

# Boolean Logic Summary

## AND

```python
True and True
```

Result:

```text
True
```

All conditions must be true.

---

## OR

```python
True or False
```

Result:

```text
True
```

At least one condition must be true.

---

## NOT

```python
not True
```

Result:

```text
False
```

It reverses the Boolean value.

---

# Files Created in This Lab

The following Python programs were used during the lab:

```text
simple_if.py
if_else.py
grade_system.py
logical_and.py
logical_or.py
logical_not.py
temperature_categorizer.py
advanced_temperature.py
validated_temperature.py
debug_practice.py
```

Check the files:

```bash
ls -la
```

---

# Testing the Python Programs

Each Python script can be executed using:

```bash
python3 filename.py
```

Examples:

```bash
python3 simple_if.py
```

```bash
python3 grade_system.py
```

```bash
python3 logical_and.py
```

```bash
python3 temperature_categorizer.py
```

---

# Verification Commands

Check Python version:

```bash
python3 --version
```

Check current directory:

```bash
pwd
```

List Python files:

```bash
ls -la *.py
```

Check Python syntax without executing the program:

```bash
python3 -m py_compile simple_if.py
```

Check another file:

```bash
python3 -m py_compile temperature_categorizer.py
```

If there is no output, the syntax check passed.

---

# Key Notes

## `if`

Used when a condition needs to be checked.

```python
if age >= 18:
    print("Adult")
```

## `elif`

Used to check another condition when the previous condition was false.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

## `else`

Runs when none of the previous conditions are true.

```python
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

## `and`

All conditions must be true.

```python
age >= 18 and has_id == True
```

## `or`

At least one condition must be true.

```python
day == "Saturday" or day == "Sunday"
```

## `not`

Reverses a condition.

```python
not is_raining
```

---

# Real-World Applications

Control flow is used in many real-world applications.

Examples include:

### Authentication

```python
if username == correct_username:
    print("Login successful")
else:
    print("Login failed")
```

### Grade Systems

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

### System Monitoring

```python
if cpu_usage > 90:
    print("High CPU usage")
```

### DevOps Automation

```python
if deployment_success:
    print("Deployment completed")
else:
    print("Deployment failed")
```

### Cloud Monitoring

```python
if server_status == "down":
    print("Start recovery process")
```

---

# Lab Completion Checklist

* [x] Created basic `if` statement
* [x] Created `if-else` statement
* [x] Used `elif`
* [x] Used comparison operators
* [x] Used `and`
* [x] Used `or`
* [x] Used `not`
* [x] Created nested conditions
* [x] Created temperature categorization program
* [x] Added input validation
* [x] Practiced debugging
* [x] Fixed indentation errors
* [x] Fixed comparison errors
* [x] Tested Python programs

---

# Conclusion

Lab 2 introduced the fundamentals of **control flow in Python**.

The lab demonstrated how Python programs can make decisions using:

```text
if
elif
else
```

and how multiple conditions can be combined using:

```text
and
or
not
```

We also practiced nested conditions, input validation, debugging, and error correction.

The temperature categorization project provided a practical example of combining multiple programming concepts into a single application.

These concepts are important foundations for future Python topics such as:

* Loops
* Functions
* Lists
* Dictionaries
* File handling
* Automation
* System administration
* DevOps scripting

---

# Final Lab Summary

```text
Lab: 02
Topic: Control Flow in Python
Language: Python 3
Environment: Linux Cloud Lab
Level: Beginner

Main Concepts:
- if
- elif
- else
- and
- or
- not
- Comparison Operators
- Nested Conditions
- Input Validation
- Debugging
```

**Status: Lab 2 Complete**
# Lab 2: Control Flow in Python

## Lab Overview

This lab introduces **control flow in Python**, which allows programs to make decisions based on conditions.

In this lab, we worked with:

* `if` statements
* `if-else` statements
* `if-elif-else` statements
* Comparison operators
* Logical operators
* Nested `if` statements
* Input validation
* Error handling
* Debugging control-flow errors
* A practical temperature categorization program

---

# Objectives

By completing this lab, students will be able to:

* Understand conditional statements in Python.
* Use `if`, `elif`, and `else`.
* Compare values using comparison operators.
* Use `and`, `or`, and `not`.
* Create nested conditional statements.
* Validate user input.
* Handle common programming errors.
* Debug incorrect Python code.
* Build a practical temperature categorization program.

---

# Prerequisites

Before starting this lab, basic knowledge of the following is recommended:

* Python variables
* Python data types
* `input()`
* `print()`
* Type conversion
* Basic Python syntax
* Running Python scripts from the terminal

---

# Lab Environment

The lab was performed in a Linux-based cloud environment with Python installed.

Check Python:

```bash
python3 --version
```

Check the current directory:

```bash
pwd
```

List files:

```bash
ls -la
```

---

# Task 1: Basic Conditional Statements

## 1.1 Simple `if` Statement

The `if` statement executes a block of code only when a condition is true.

### Example

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")
    print("You can vote in elections.")

print("Program finished.")
```

### Run

```bash
python3 simple_if.py
```

### Key Concept

```text
if condition:
    code
```

If the condition is `True`, the indented code runs.

### Example

```text
age = 20
20 >= 18 → True
```

Therefore, the `if` block executes.

---

# 1.2 `if-else` Statement

An `if-else` statement provides two possible paths.

```python
score = int(input("Enter your test score (0-100): "))

if score >= 60:
    print("Congratulations! You passed the test.")
else:
    print("Sorry, you did not pass the test.")
```

### Run

```bash
python3 if_else.py
```

### Logic

```text
Condition True  → if block
Condition False → else block
```

### Example

```text
Score = 75

75 >= 60 → True
Result → Passed
```

---

# 1.3 `if-elif-else`

When there are multiple possible conditions, we can use `elif`.

```python
score = int(input("Enter your test score (0-100): "))

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

print(f"Score: {score}")
print(f"Grade: {grade}")
```

### Run

```bash
python3 grade_system.py
```

### Example

```text
95 → A
85 → B
75 → C
65 → D
55 → F
```

### Important Point

Python checks conditions from **top to bottom**.

Once a condition is true, its block executes and the remaining `elif` conditions are skipped.

---

# Task 2: Logical Operators

Logical operators allow multiple conditions to be combined.

Python provides three important logical operators:

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | All conditions must be True         |
| `or`     | At least one condition must be True |
| `not`    | Reverses the result                 |

---

# 2.1 `and` Operator

The `and` operator requires **all conditions** to be true.

Example:

```python
username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

if username == "student" and password == "python123" and age >= 13:
    print("Access granted!")
else:
    print("Access denied!")
```

### Run

```bash
python3 logical_and.py
```

### Example

```text
username = student
password = python123
age = 16
```

All conditions are true:

```text
True and True and True
```

Result:

```text
Access granted!
```

---

# 2.2 `or` Operator

The `or` operator requires **at least one condition** to be true.

Example:

```python
day = input("What day is it? ").lower()

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
```

### Run

```bash
python3 logical_or.py
```

### Example

```text
day = saturday
```

Evaluation:

```text
True or False
```

Result:

```text
It's the weekend!
```

---

# 2.3 `not` Operator

The `not` operator reverses a Boolean condition.

Example:

```python
is_raining = input("Is it raining? (yes/no): ").lower()

if not is_raining == "yes":
    print("You can go outside.")
else:
    print("Take an umbrella.")
```

### Run

```bash
python3 logical_not.py
```

### Concept

```text
not True  → False
not False → True
```

---

# Task 3: Temperature Categorization

This task combines conditional statements and logical operators into a practical program.

---

# 3.1 Basic Temperature Categorization

The program classifies temperature as:

* HOT
* COLD
* MILD

Example:

```python
temperature = float(input("Enter temperature in Fahrenheit: "))

if temperature >= 80:
    category = "hot"
elif temperature <= 50:
    category = "cold"
else:
    category = "mild"

print(f"Temperature category: {category.upper()}")
```

### Run

```bash
python3 temperature_categorizer.py
```

### Example

```text
90 → HOT
45 → COLD
65 → MILD
```

---

# 3.2 Nested `if` Statements

A nested `if` means placing one conditional statement inside another.

Example:

```python
if temperature >= 80:
    print("HOT")

    if humidity > 70:
        print("High humidity")
```

The inner condition is checked only after the outer condition is true.

### Structure

```text
if condition:
    if another_condition:
        code
```

---

# Advanced Temperature Categorizer

The advanced program considers:

* Temperature
* Humidity
* Sunny/cloudy weather
* Comfort level
* Weather recommendations

Example:

```python
temperature = float(input("Enter temperature in Fahrenheit: "))
humidity = float(input("Enter humidity percentage: "))
is_sunny = input("Is it sunny? (yes/no): ").lower()

if temperature >= 80:

    if humidity > 70:
        comfort_level = "Very Uncomfortable"
    elif humidity > 50:
        comfort_level = "Uncomfortable"
    else:
        comfort_level = "Tolerable"

elif temperature <= 50:

    if temperature <= 32:
        comfort_level = "Cold"
    else:
        comfort_level = "Cool"

else:

    if temperature >= 70 and humidity < 60 and is_sunny == "yes":
        comfort_level = "Perfect"
    else:
        comfort_level = "Comfortable"

print(f"Comfort Level: {comfort_level}")
```

---

# 3.3 Input Validation

Input validation makes a program safer and more reliable.

For example, the user might enter:

```text
hello
```

when the program expects a number.

Using `try-except` allows the program to handle this error.

Example:

```python
while True:
    try:
        temperature = float(input("Enter temperature: "))
        break
    except ValueError:
        print("Please enter a valid number.")
```

### Why Input Validation Matters

Without validation:

```text
hello → ValueError
```

With validation:

```text
hello → Error message → Ask again
```

---

# Task 4: Debugging and Troubleshooting

Debugging means finding and fixing errors in a program.

Common control-flow errors include:

* Incorrect indentation
* Missing colon
* Incorrect comparison operator
* Incorrect logical conditions
* Unreachable conditions
* Incorrect data types

---

# Common Error 1: Incorrect Indentation

### Wrong

```python
if temperature > 80:
print("Hot weather")
```

### Correct

```python
if temperature > 80:
    print("Hot weather")
```

Python uses indentation to define code blocks.

The standard indentation is:

```text
4 spaces
```

---

# Common Error 2: `=` vs `==`

### Assignment

```python
temperature = 80
```

`=` assigns a value.

### Comparison

```python
temperature == 80
```

`==` checks whether two values are equal.

### Correct

```python
if temperature == 80:
    print("Temperature is 80")
```

---

# Common Error 3: Missing Colon

### Wrong

```python
if temperature > 80
```

### Correct

```python
if temperature > 80:
```

Python conditional statements require a colon at the end.

---

# Common Error 4: Incorrect Data Type

### Problem

```python
temperature = input("Enter temperature: ")

if temperature > 80:
```

`input()` returns a string.

### Correct

```python
temperature = float(input("Enter temperature: "))
```

Now the value can be compared numerically.

---

# Common Error 5: Unreachable Condition

Consider:

```python
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
elif temperature > 100:
    print("This will never execute")
```

The final condition is unreachable because values greater than 100 have already been handled by the first condition.

### Correct Ordering

```python
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
```

---

# Important Comparison Operators

Python provides several comparison operators.

| Operator | Meaning               | Example   |
| -------- | --------------------- | --------- |
| `==`     | Equal                 | `x == 10` |
| `!=`     | Not equal             | `x != 10` |
| `>`      | Greater than          | `x > 10`  |
| `<`      | Less than             | `x < 10`  |
| `>=`     | Greater than or equal | `x >= 10` |
| `<=`     | Less than or equal    | `x <= 10` |

These operators return:

```text
True
```

or

```text
False
```

---

# Boolean Logic Summary

## AND

```python
True and True
```

Result:

```text
True
```

All conditions must be true.

---

## OR

```python
True or False
```

Result:

```text
True
```

At least one condition must be true.

---

## NOT

```python
not True
```

Result:

```text
False
```

It reverses the Boolean value.

---

# Files Created in This Lab

The following Python programs were used during the lab:

```text
simple_if.py
if_else.py
grade_system.py
logical_and.py
logical_or.py
logical_not.py
temperature_categorizer.py
advanced_temperature.py
validated_temperature.py
debug_practice.py
```

Check the files:

```bash
ls -la
```

---

# Testing the Python Programs

Each Python script can be executed using:

```bash
python3 filename.py
```

Examples:

```bash
python3 simple_if.py
```

```bash
python3 grade_system.py
```

```bash
python3 logical_and.py
```

```bash
python3 temperature_categorizer.py
```

---

# Verification Commands

Check Python version:

```bash
python3 --version
```

Check current directory:

```bash
pwd
```

List Python files:

```bash
ls -la *.py
```

Check Python syntax without executing the program:

```bash
python3 -m py_compile simple_if.py
```

Check another file:

```bash
python3 -m py_compile temperature_categorizer.py
```

If there is no output, the syntax check passed.

---

# Key Notes

## `if`

Used when a condition needs to be checked.

```python
if age >= 18:
    print("Adult")
```

## `elif`

Used to check another condition when the previous condition was false.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

## `else`

Runs when none of the previous conditions are true.

```python
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

## `and`

All conditions must be true.

```python
age >= 18 and has_id == True
```

## `or`

At least one condition must be true.

```python
day == "Saturday" or day == "Sunday"
```

## `not`

Reverses a condition.

```python
not is_raining
```

---

# Real-World Applications

Control flow is used in many real-world applications.

Examples include:

### Authentication

```python
if username == correct_username:
    print("Login successful")
else:
    print("Login failed")
```

### Grade Systems

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

### System Monitoring

```python
if cpu_usage > 90:
    print("High CPU usage")
```

### DevOps Automation

```python
if deployment_success:
    print("Deployment completed")
else:
    print("Deployment failed")
```

### Cloud Monitoring

```python
if server_status == "down":
    print("Start recovery process")
```

---

# Lab Completion Checklist

* [x] Created basic `if` statement
* [x] Created `if-else` statement
* [x] Used `elif`
* [x] Used comparison operators
* [x] Used `and`
* [x] Used `or`
* [x] Used `not`
* [x] Created nested conditions
* [x] Created temperature categorization program
* [x] Added input validation
* [x] Practiced debugging
* [x] Fixed indentation errors
* [x] Fixed comparison errors
* [x] Tested Python programs

---

# Conclusion

Lab 2 introduced the fundamentals of **control flow in Python**.

The lab demonstrated how Python programs can make decisions using:

```text
if
elif
else
```

and how multiple conditions can be combined using:

```text
and
or
not
```

We also practiced nested conditions, input validation, debugging, and error correction.

The temperature categorization project provided a practical example of combining multiple programming concepts into a single application.

These concepts are important foundations for future Python topics such as:

* Loops
* Functions
* Lists
* Dictionaries
* File handling
* Automation
* System administration
* DevOps scripting

---

# Final Lab Summary

```text
Lab: 02
Topic: Control Flow in Python
Language: Python 3
Environment: Linux Cloud Lab
Level: Beginner

Main Concepts:
- if
- elif
- else
- and
- or
- not
- Comparison Operators
- Nested Conditions
- Input Validation
- Debugging
```

**Status: Lab 2 Complete**
# Lab 2: Control Flow in Python

## Lab Overview

This lab introduces **control flow in Python**, which allows programs to make decisions based on conditions.

In this lab, we worked with:

* `if` statements
* `if-else` statements
* `if-elif-else` statements
* Comparison operators
* Logical operators
* Nested `if` statements
* Input validation
* Error handling
* Debugging control-flow errors
* A practical temperature categorization program

---

# Objectives

By completing this lab, students will be able to:

* Understand conditional statements in Python.
* Use `if`, `elif`, and `else`.
* Compare values using comparison operators.
* Use `and`, `or`, and `not`.
* Create nested conditional statements.
* Validate user input.
* Handle common programming errors.
* Debug incorrect Python code.
* Build a practical temperature categorization program.

---

# Prerequisites

Before starting this lab, basic knowledge of the following is recommended:

* Python variables
* Python data types
* `input()`
* `print()`
* Type conversion
* Basic Python syntax
* Running Python scripts from the terminal

---

# Lab Environment

The lab was performed in a Linux-based cloud environment with Python installed.

Check Python:

```bash
python3 --version
```

Check the current directory:

```bash
pwd
```

List files:

```bash
ls -la
```

---

# Task 1: Basic Conditional Statements

## 1.1 Simple `if` Statement

The `if` statement executes a block of code only when a condition is true.

### Example

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")
    print("You can vote in elections.")

print("Program finished.")
```

### Run

```bash
python3 simple_if.py
```

### Key Concept

```text
if condition:
    code
```

If the condition is `True`, the indented code runs.

### Example

```text
age = 20
20 >= 18 → True
```

Therefore, the `if` block executes.

---

# 1.2 `if-else` Statement

An `if-else` statement provides two possible paths.

```python
score = int(input("Enter your test score (0-100): "))

if score >= 60:
    print("Congratulations! You passed the test.")
else:
    print("Sorry, you did not pass the test.")
```

### Run

```bash
python3 if_else.py
```

### Logic

```text
Condition True  → if block
Condition False → else block
```

### Example

```text
Score = 75

75 >= 60 → True
Result → Passed
```

---

# 1.3 `if-elif-else`

When there are multiple possible conditions, we can use `elif`.

```python
score = int(input("Enter your test score (0-100): "))

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

print(f"Score: {score}")
print(f"Grade: {grade}")
```

### Run

```bash
python3 grade_system.py
```

### Example

```text
95 → A
85 → B
75 → C
65 → D
55 → F
```

### Important Point

Python checks conditions from **top to bottom**.

Once a condition is true, its block executes and the remaining `elif` conditions are skipped.

---

# Task 2: Logical Operators

Logical operators allow multiple conditions to be combined.

Python provides three important logical operators:

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | All conditions must be True         |
| `or`     | At least one condition must be True |
| `not`    | Reverses the result                 |

---

# 2.1 `and` Operator

The `and` operator requires **all conditions** to be true.

Example:

```python
username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

if username == "student" and password == "python123" and age >= 13:
    print("Access granted!")
else:
    print("Access denied!")
```

### Run

```bash
python3 logical_and.py
```

### Example

```text
username = student
password = python123
age = 16
```

All conditions are true:

```text
True and True and True
```

Result:

```text
Access granted!
```

---

# 2.2 `or` Operator

The `or` operator requires **at least one condition** to be true.

Example:

```python
day = input("What day is it? ").lower()

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
```

### Run

```bash
python3 logical_or.py
```

### Example

```text
day = saturday
```

Evaluation:

```text
True or False
```

Result:

```text
It's the weekend!
```

---

# 2.3 `not` Operator

The `not` operator reverses a Boolean condition.

Example:

```python
is_raining = input("Is it raining? (yes/no): ").lower()

if not is_raining == "yes":
    print("You can go outside.")
else:
    print("Take an umbrella.")
```

### Run

```bash
python3 logical_not.py
```

### Concept

```text
not True  → False
not False → True
```

---

# Task 3: Temperature Categorization

This task combines conditional statements and logical operators into a practical program.

---

# 3.1 Basic Temperature Categorization

The program classifies temperature as:

* HOT
* COLD
* MILD

Example:

```python
temperature = float(input("Enter temperature in Fahrenheit: "))

if temperature >= 80:
    category = "hot"
elif temperature <= 50:
    category = "cold"
else:
    category = "mild"

print(f"Temperature category: {category.upper()}")
```

### Run

```bash
python3 temperature_categorizer.py
```

### Example

```text
90 → HOT
45 → COLD
65 → MILD
```

---

# 3.2 Nested `if` Statements

A nested `if` means placing one conditional statement inside another.

Example:

```python
if temperature >= 80:
    print("HOT")

    if humidity > 70:
        print("High humidity")
```

The inner condition is checked only after the outer condition is true.

### Structure

```text
if condition:
    if another_condition:
        code
```

---

# Advanced Temperature Categorizer

The advanced program considers:

* Temperature
* Humidity
* Sunny/cloudy weather
* Comfort level
* Weather recommendations

Example:

```python
temperature = float(input("Enter temperature in Fahrenheit: "))
humidity = float(input("Enter humidity percentage: "))
is_sunny = input("Is it sunny? (yes/no): ").lower()

if temperature >= 80:

    if humidity > 70:
        comfort_level = "Very Uncomfortable"
    elif humidity > 50:
        comfort_level = "Uncomfortable"
    else:
        comfort_level = "Tolerable"

elif temperature <= 50:

    if temperature <= 32:
        comfort_level = "Cold"
    else:
        comfort_level = "Cool"

else:

    if temperature >= 70 and humidity < 60 and is_sunny == "yes":
        comfort_level = "Perfect"
    else:
        comfort_level = "Comfortable"

print(f"Comfort Level: {comfort_level}")
```

---

# 3.3 Input Validation

Input validation makes a program safer and more reliable.

For example, the user might enter:

```text
hello
```

when the program expects a number.

Using `try-except` allows the program to handle this error.

Example:

```python
while True:
    try:
        temperature = float(input("Enter temperature: "))
        break
    except ValueError:
        print("Please enter a valid number.")
```

### Why Input Validation Matters

Without validation:

```text
hello → ValueError
```

With validation:

```text
hello → Error message → Ask again
```

---

# Task 4: Debugging and Troubleshooting

Debugging means finding and fixing errors in a program.

Common control-flow errors include:

* Incorrect indentation
* Missing colon
* Incorrect comparison operator
* Incorrect logical conditions
* Unreachable conditions
* Incorrect data types

---

# Common Error 1: Incorrect Indentation

### Wrong

```python
if temperature > 80:
print("Hot weather")
```

### Correct

```python
if temperature > 80:
    print("Hot weather")
```

Python uses indentation to define code blocks.

The standard indentation is:

```text
4 spaces
```

---

# Common Error 2: `=` vs `==`

### Assignment

```python
temperature = 80
```

`=` assigns a value.

### Comparison

```python
temperature == 80
```

`==` checks whether two values are equal.

### Correct

```python
if temperature == 80:
    print("Temperature is 80")
```

---

# Common Error 3: Missing Colon

### Wrong

```python
if temperature > 80
```

### Correct

```python
if temperature > 80:
```

Python conditional statements require a colon at the end.

---

# Common Error 4: Incorrect Data Type

### Problem

```python
temperature = input("Enter temperature: ")

if temperature > 80:
```

`input()` returns a string.

### Correct

```python
temperature = float(input("Enter temperature: "))
```

Now the value can be compared numerically.

---

# Common Error 5: Unreachable Condition

Consider:

```python
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
elif temperature > 100:
    print("This will never execute")
```

The final condition is unreachable because values greater than 100 have already been handled by the first condition.

### Correct Ordering

```python
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
```

---

# Important Comparison Operators

Python provides several comparison operators.

| Operator | Meaning               | Example   |
| -------- | --------------------- | --------- |
| `==`     | Equal                 | `x == 10` |
| `!=`     | Not equal             | `x != 10` |
| `>`      | Greater than          | `x > 10`  |
| `<`      | Less than             | `x < 10`  |
| `>=`     | Greater than or equal | `x >= 10` |
| `<=`     | Less than or equal    | `x <= 10` |

These operators return:

```text
True
```

or

```text
False
```

---

# Boolean Logic Summary

## AND

```python
True and True
```

Result:

```text
True
```

All conditions must be true.

---

## OR

```python
True or False
```

Result:

```text
True
```

At least one condition must be true.

---

## NOT

```python
not True
```

Result:

```text
False
```

It reverses the Boolean value.

---

# Files Created in This Lab

The following Python programs were used during the lab:

```text
simple_if.py
if_else.py
grade_system.py
logical_and.py
logical_or.py
logical_not.py
temperature_categorizer.py
advanced_temperature.py
validated_temperature.py
debug_practice.py
```

Check the files:

```bash
ls -la
```

---

# Testing the Python Programs

Each Python script can be executed using:

```bash
python3 filename.py
```

Examples:

```bash
python3 simple_if.py
```

```bash
python3 grade_system.py
```

```bash
python3 logical_and.py
```

```bash
python3 temperature_categorizer.py
```

---

# Verification Commands

Check Python version:

```bash
python3 --version
```

Check current directory:

```bash
pwd
```

List Python files:

```bash
ls -la *.py
```

Check Python syntax without executing the program:

```bash
python3 -m py_compile simple_if.py
```

Check another file:

```bash
python3 -m py_compile temperature_categorizer.py
```

If there is no output, the syntax check passed.

---

# Key Notes

## `if`

Used when a condition needs to be checked.

```python
if age >= 18:
    print("Adult")
```

## `elif`

Used to check another condition when the previous condition was false.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

## `else`

Runs when none of the previous conditions are true.

```python
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

## `and`

All conditions must be true.

```python
age >= 18 and has_id == True
```

## `or`

At least one condition must be true.

```python
day == "Saturday" or day == "Sunday"
```

## `not`

Reverses a condition.

```python
not is_raining
```

---

# Real-World Applications

Control flow is used in many real-world applications.

Examples include:

### Authentication

```python
if username == correct_username:
    print("Login successful")
else:
    print("Login failed")
```

### Grade Systems

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

### System Monitoring

```python
if cpu_usage > 90:
    print("High CPU usage")
```

### DevOps Automation

```python
if deployment_success:
    print("Deployment completed")
else:
    print("Deployment failed")
```

### Cloud Monitoring

```python
if server_status == "down":
    print("Start recovery process")
```

---

# Lab Completion Checklist

* [x] Created basic `if` statement
* [x] Created `if-else` statement
* [x] Used `elif`
* [x] Used comparison operators
* [x] Used `and`
* [x] Used `or`
* [x] Used `not`
* [x] Created nested conditions
* [x] Created temperature categorization program
* [x] Added input validation
* [x] Practiced debugging
* [x] Fixed indentation errors
* [x] Fixed comparison errors
* [x] Tested Python programs

---

# Conclusion

Lab 2 introduced the fundamentals of **control flow in Python**.

The lab demonstrated how Python programs can make decisions using:

```text
if
elif
else
```

and how multiple conditions can be combined using:

```text
and
or
not
```

We also practiced nested conditions, input validation, debugging, and error correction.

The temperature categorization project provided a practical example of combining multiple programming concepts into a single application.

These concepts are important foundations for future Python topics such as:

* Loops
* Functions
* Lists
* Dictionaries
* File handling
* Automation
* System administration
* DevOps scripting

---

# Final Lab Summary

```text
Lab: 02
Topic: Control Flow in Python
Language: Python 3
Environment: Linux Cloud Lab
Level: Beginner

Main Concepts:
- if
- elif
- else
- and
- or
- not
- Comparison Operators
- Nested Conditions
- Input Validation
- Debugging
```

**Status: Lab 2 Complete**
