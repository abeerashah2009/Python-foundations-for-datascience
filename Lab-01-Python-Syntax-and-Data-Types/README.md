# Lab 01: Python Syntax and Data Types

## 📌 Lab Overview

This lab introduces the fundamental building blocks of Python programming.

The focus is on:

* Python syntax
* Variables
* Variable naming rules
* Basic data types
* `int`
* `float`
* `str`
* `bool`
* The `type()` function
* The `input()` function
* Type conversion
* Arithmetic operations
* String operations
* Basic error handling
* Practical user-input programs

This lab is designed for beginners and provides the foundation required for future Python topics such as **lists, dictionaries, functions, file handling, automation, data analysis, and AI/ML workflows**.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

* Understand basic Python syntax.
* Create and execute Python scripts.
* Create and assign variables.
* Follow Python variable naming rules.
* Identify common Python data types.
* Use the `type()` function.
* Collect user input using `input()`.
* Understand that `input()` returns a string.
* Convert values between different data types.
* Perform arithmetic operations.
* Perform basic string operations.
* Work with Boolean values.
* Handle common type-conversion errors.
* Build a practical student grade calculator.
* Verify Python programs from the Linux terminal.

---

# 🛠️ Prerequisites

No previous programming experience is required.

Basic knowledge of:

* Linux terminal
* Creating files
* Editing text files
* Running commands

is helpful.

---

# 💻 Lab Environment

The lab is performed in a Linux-based cloud environment with Python available.

First, verify Python:

```bash
python3 --version
```

Example:

```text
Python 3.12.3
```

Also check the location of Python:

```bash
which python3
```

Example:

```text
/usr/bin/python3
```

---

# 📁 Lab Directory Setup

Create a dedicated directory for Lab 01:

```bash
mkdir -p ~/python_lab1
cd ~/python_lab1
```

Verify the current directory:

```bash
pwd
```

Verify the directory contents:

```bash
ls -la
```

---

# 🧠 Task 1: Python Variables and Basic Data Types

## 1.1 Create the First Python Script

Create the file:

```bash
nano variables_demo.py
```

Add:

```python
# Lab 1: Python Variables and Data Types Demo

print("=== Python Data Types Demonstration ===")
print()

# Integer
student_age = 20
print("Student Age:", student_age)
print("Type of student_age:", type(student_age))
print()

# Float
student_gpa = 3.75
print("Student GPA:", student_gpa)
print("Type of student_gpa:", type(student_gpa))
print()

# String
student_name = "Alice Johnson"
print("Student Name:", student_name)
print("Type of student_name:", type(student_name))
print()

# Boolean
is_enrolled = True
print("Is Enrolled:", is_enrolled)
print("Type of is_enrolled:", type(is_enrolled))
print()

print("=== End of Data Types Demo ===")
```

Save and exit:

```text
Ctrl + X
Y
Enter
```

Run:

```bash
python3 variables_demo.py
```

---

# 📊 Python's Four Basic Data Types

| Data Type | Python Type | Example          | Purpose         |
| --------- | ----------- | ---------------- | --------------- |
| Integer   | `int`       | `20`             | Whole numbers   |
| Float     | `float`     | `3.75`           | Decimal numbers |
| String    | `str`       | `"Alice"`        | Text            |
| Boolean   | `bool`      | `True` / `False` | Logical values  |

---

# 🔢 `int` — Integer

An integer is a whole number.

Example:

```python
age = 20
```

Check its type:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

Examples:

```python
students = 30
score = 95
year = 2026
```

---

# 🔢 `float` — Floating-Point Number

A float represents a number containing a decimal value.

Example:

```python
gpa = 3.75
```

Check:

```python
print(type(gpa))
```

Output:

```text
<class 'float'>
```

Examples:

```python
price = 19.99
temperature = 25.5
percentage = 87.5
```

---

# 📝 `str` — String

A string represents text.

Example:

```python
name = "Alice Johnson"
```

Check:

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

Strings are normally written inside:

```python
"double quotes"
```

or:

```python
'single quotes'
```

---

# ✅ `bool` — Boolean

A Boolean represents one of two logical values:

```python
True
False
```

Example:

```python
is_enrolled = True
```

Check:

```python
print(type(is_enrolled))
```

Output:

```text
<class 'bool'>
```

Boolean values are commonly used in:

* Conditions
* Authentication
* Validation
* Program decisions
* Automation

---

# 🧪 Task 1.2: Variable Naming Rules

Create:

```bash
nano variable_naming.py
```

Add:

```python
# Variable Naming Rules and Examples

print("=== Variable Naming Examples ===")
print()

# Valid variable names
first_name = "John"
last_name = "Smith"
age_in_years = 25
course_code_2024 = "CS101"
_private_variable = "hidden"

print("Valid variable examples:")
print("first_name:", first_name)
print("last_name:", last_name)
print("age_in_years:", age_in_years)
print("course_code_2024:", course_code_2024)
print("_private_variable:", _private_variable)
print()

# Multiple assignment
x, y, z = 10, 20.5, "Hello"

print("Multiple assignment:")
print("x =", x, "| Type:", type(x))
print("y =", y, "| Type:", type(y))
print("z =", z, "| Type:", type(z))
print()

# Same value assigned to multiple variables
a = b = c = 100

print("Same value assignment:")
print("a =", a, "| b =", b, "| c =", c)
```

Run:

```bash
python3 variable_naming.py
```

---

# 📌 Python Variable Naming Rules

Python variable names:

### ✅ Can contain:

* Letters
* Numbers
* Underscores

Examples:

```python
student_name
student1
course_2026
```

### ❌ Cannot start with a number

Invalid:

```python
1student = "Abeera"
```

Valid:

```python
student1 = "Abeera"
```

### ❌ Cannot contain spaces

Invalid:

```python
student name = "Abeera"
```

Valid:

```python
student_name = "Abeera"
```

### ❌ Cannot use Python keywords

For example:

```python
class
if
for
while
def
```

should not be used as normal variable names.

---

# ⌨️ Task 2: Working With `input()`

## 2.1 Basic User Input

Create:

```bash
nano user_input_demo.py
```

Add:

```python
# User Input Demonstration

print("=== User Input Collection ===")
print()

print("Let's collect some information about you!")

user_name = input("Please enter your name: ")

print("Hello,", user_name + "!")
print("Type of user_name:", type(user_name))
print()

user_age_str = input("Please enter your age: ")

print("You entered:", user_age_str)
print("Type of user_age_str:", type(user_age_str))
print()

favorite_number_str = input("Enter your favorite number: ")

print("Your favorite number is:", favorite_number_str)
print("Type:", type(favorite_number_str))
print()

print("Notice: input() returns a string.")
```

Run:

```bash
python3 user_input_demo.py
```

Test with:

```text
Name: Abeera
Age: 20
Favorite number: 7
```

---

# ⭐ Important Concept: `input()` Returns a String

Even if the user enters:

```text
20
```

Python initially stores it as:

```python
"20"
```

Therefore:

```python
age = input("Enter age: ")
```

results in:

```python
type(age)
```

being:

```text
<class 'str'>
```

If you need an integer, convert it:

```python
age = int(input("Enter age: "))
```

---

# 🧪 Task 2.2: Advanced Input Handling

Create:

```bash
nano advanced_input.py
```

Add:

```python
# Advanced Input Handling

print("=== Advanced Input Handling ===")
print()

print("Student Registration System")
print("-" * 30)

student_name = input("Student Name: ")
student_id = input("Student ID: ")
email = input("Email Address: ")

print()
print("Registration Summary:")
print("Name:", student_name)
print("ID:", student_id)
print("Email:", email)
print()

course_selection = input("Select your course (CS/IT/ENG): ")
semester = input("Enter semester (Fall/Spring/Summer): ")

print()
print("Course Information:")
print("Selected Course:", course_selection)
print("Semester:", semester)
print()

is_full_time = input("Are you a full-time student? (yes/no): ")

print("Full-time status:", is_full_time)
print("Type:", type(is_full_time))
```

Run:

```bash
python3 advanced_input.py
```

---

# 🔄 Task 3: Type Conversion

Type conversion means changing a value from one data type to another.

Common conversion functions:

| Function  | Converts To |
| --------- | ----------- |
| `int()`   | Integer     |
| `float()` | Float       |
| `str()`   | String      |
| `bool()`  | Boolean     |

---

# 🧪 Task 3.1: Basic Type Conversion

Create:

```bash
nano type_conversion.py
```

Add:

```python
# Type Conversion Demonstration

print("=== Type Conversion Examples ===")
print()

# String to Integer
age_str = "25"
age_int = int(age_str)

print("Original string:", age_str)
print("Type:", type(age_str))
print("Converted to int:", age_int)
print("Type:", type(age_int))
print()

# String to Float
price_str = "19.99"
price_float = float(price_str)

print("Original string:", price_str)
print("Type:", type(price_str))
print("Converted to float:", price_float)
print("Type:", type(price_float))
print()

# Integer to String
score = 95
score_str = str(score)

print("Original integer:", score)
print("Type:", type(score))
print("Converted to string:", score_str)
print("Type:", type(score_str))
print()

# Float to Integer
gpa = 3.87
gpa_int = int(gpa)

print("Original float:", gpa)
print("Converted to int:", gpa_int)
print("Note: The decimal portion is truncated.")
print()

# Boolean conversions
print("Boolean Conversion:")
print("int(True):", int(True))
print("int(False):", int(False))
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))
```

Run:

```bash
python3 type_conversion.py
```

---

# ⚠️ Important: Integer Conversion Truncates

Consider:

```python
number = 3.87
result = int(number)
```

The result is:

```text
3
```

Python does not round it to `4`.

It removes the decimal portion.

---

# 🧮 Task 3.2: Interactive Calculator

Create:

```bash
nano interactive_calculator.py
```

Add:

```python
# Interactive Calculator

print("=== Simple Calculator ===")
print()

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

num1 = float(num1_str)
num2 = float(num2_str)

print()
print("Input Analysis:")
print("First input:", num1_str)
print("After conversion:", num1)
print("Type:", type(num1))
print()

print("Calculation Results:")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")

print()
print("Type Conversion of Results:")
print("Addition as integer:", int(addition))
print("Addition as string:", str(addition))
```

Run:

```bash
python3 interactive_calculator.py
```

Example:

```text
First number: 15.5
Second number: 4.2
```

---

# ➕ Task 4: Arithmetic Operations

Create:

```bash
nano operations_demo.py
```

Add:

```python
# Basic Operations with Different Data Types

print("=== Arithmetic Operations ===")
print()

a = 10
b = 3

print("Integer Operations:")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print()

x = 15.5
y = 2.5

print("Float Operations:")
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print()

print("Mixed Operations:")
result1 = a + x
result2 = b * y

print(f"{a} + {x} = {result1}")
print(f"Type: {type(result1)}")

print(f"{b} * {y} = {result2}")
print(f"Type: {type(result2)}")
print()

first_name = "John"
last_name = "Doe"

print("String Operations:")
print("Concatenation:", first_name + " " + last_name)
print("Repetition:", first_name * 3)
print("Length:", len(first_name))
```

Run:

```bash
python3 operations_demo.py
```

---

# 📊 Python Arithmetic Operators

| Operator | Meaning           | Example   |
| -------- | ----------------- | --------- |
| `+`      | Addition          | `10 + 3`  |
| `-`      | Subtraction       | `10 - 3`  |
| `*`      | Multiplication    | `10 * 3`  |
| `/`      | Division          | `10 / 3`  |
| `//`     | Floor division    | `10 // 3` |
| `%`      | Modulus/remainder | `10 % 3`  |
| `**`     | Exponentiation    | `10 ** 3` |

---

# 📝 String Operations

Python also allows basic operations on strings.

### Concatenation

```python
first = "Hello"
last = "World"

result = first + " " + last
```

Result:

```text
Hello World
```

### Repetition

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

### Length

```python
name = "Abeera"
print(len(name))
```

---

# 🎓 Task 4.2: Practical Student Grade Calculator

Create:

```bash
nano grade_calculator.py
```

Add:

```python
# Student Grade Calculator

print("=== Student Grade Calculator ===")
print()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
course_name = input("Enter course name: ")

print()
print("Enter assessment scores:")

quiz1 = float(input("Quiz 1 score: "))
quiz2 = float(input("Quiz 2 score: "))
midterm = float(input("Midterm score: "))
final = float(input("Final exam score: "))
project = float(input("Project score: "))

quiz_average = (quiz1 + quiz2) / 2

weighted_score = (
    (quiz_average * 0.20)
    + (midterm * 0.25)
    + (final * 0.35)
    + (project * 0.20)
)

if weighted_score >= 90:
    letter_grade = "A"
elif weighted_score >= 80:
    letter_grade = "B"
elif weighted_score >= 70:
    letter_grade = "C"
elif weighted_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

is_passing = weighted_score >= 60

print()
print("=== Final Grade Report ===")
print("Student:", student_name)
print("ID:", student_id)
print("Course:", course_name)
print()

print("Quiz Average:", f"{quiz_average:.2f}")
print("Midterm:", midterm)
print("Final:", final)
print("Project:", project)
print()

print("Weighted Final Score:", f"{weighted_score:.2f}")
print("Letter Grade:", letter_grade)
print("Passing Status:", is_passing)
print("Status Type:", type(is_passing))

print()
print("=== Type Conversion Examples ===")
print("Final score as integer:", int(weighted_score))
print("Final score as string:", str(weighted_score))
print("Passing status as integer:", int(is_passing))
```

Run:

```bash
python3 grade_calculator.py
```

Example test data:

```text
Student name: Sarah Johnson
Student ID: 12345
Course: Introduction to Python
Quiz 1: 85
Quiz 2: 92
Midterm: 78
Final: 88
Project: 95
```

---

# 🧪 Task 5: Error Handling

User input can contain invalid values.

For example:

```python
age = int("hello")
```

causes:

```text
ValueError
```

To handle this safely, Python provides `try` and `except`.

---

# 🛡️ Task 5.1: Safe Type Conversion

Create:

```bash
nano error_examples.py
```

Add:

```python
# Common Type Conversion Errors and Solutions

print("=== Error Handling Examples ===")
print()

user_input = input("Enter a whole number: ")

try:
    number = int(user_input)

    print("Conversion successful!")
    print("Number:", number)
    print("Type:", type(number))

except ValueError:
    print("Error: Invalid integer.")
    print("Please enter a whole number.")

print()

user_input2 = input("Enter a decimal number: ")

try:
    decimal_number = float(user_input2)

    print("Conversion successful!")
    print("Number:", decimal_number)
    print("Type:", type(decimal_number))

except ValueError:
    print("Error: Invalid decimal number.")
    print("Please enter a valid number.")
```

Run:

```bash
python3 error_examples.py
```

Test with:

```text
42
```

Then test again with:

```text
hello
```

Observe the difference.

---

# 🔍 Boolean Conversion

Test:

```python
print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))
```

Expected:

```text
True
False
True
False
```

### Important clarification

For strings:

```python
bool("False")
```

returns:

```text
True
```

because `"False"` is a **non-empty string**.

It does not automatically interpret the text `"False"` as the Boolean value `False`.

---

# 🔧 Troubleshooting

## Issue 1: Python Is Not Found

Run:

```bash
python3 --version
```

Also try:

```bash
python --version
```

Find Python:

```bash
which python3
```

---

## Issue 2: `IndentationError`

Python uses indentation to define code blocks.

Incorrect:

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

Use **4 spaces** for normal indentation.

---

# ❌ Issue 3: `ValueError`

Example:

```python
age = int("hello")
```

Error:

```text
ValueError
```

Solution:

```python
try:
    age = int(user_input)
except ValueError:
    print("Please enter a valid number.")
```

---

# ❌ Issue 4: `ZeroDivisionError`

This will fail:

```python
result = 10 / 0
```

Use validation before performing division.

For example:

```python
if num2 != 0:
    result = num1 / num2
else:
    print("Cannot divide by zero.")
```

---

# ❌ Issue 5: File Not Found

Check your current directory:

```bash
pwd
```

List files:

```bash
ls -la
```

Return to the lab directory:

```bash
cd ~/python_lab1
```

---

# 🧪 Lab Verification

Run:

```bash
cd ~/python_lab1
```

List all scripts:

```bash
ls -lh
```

Expected files include:

```text
variables_demo.py
variable_naming.py
user_input_demo.py
advanced_input.py
type_conversion.py
interactive_calculator.py
operations_demo.py
grade_calculator.py
error_examples.py
```

---

# 🔎 Syntax Verification

Python provides a useful way to check whether a script has syntax errors without running it:

```bash
python3 -m py_compile variables_demo.py
```

Repeat for the other scripts:

```bash
python3 -m py_compile variable_naming.py
python3 -m py_compile user_input_demo.py
python3 -m py_compile advanced_input.py
python3 -m py_compile type_conversion.py
python3 -m py_compile interactive_calculator.py
python3 -m py_compile operations_demo.py
python3 -m py_compile grade_calculator.py
python3 -m py_compile error_examples.py
```

If there is no output, the syntax check passed.

---

# 📂 Suggested Evidence Structure

For a professional GitHub portfolio, keep evidence organized:

```text
Lab-01-Python-Syntax-and-Data-Types/
├── README.md
├── variables_demo.py
├── variable_naming.py
├── user_input_demo.py
├── advanced_input.py
├── type_conversion.py
├── interactive_calculator.py
├── operations_demo.py
├── grade_calculator.py
├── error_examples.py
└── evidence/
    ├── python-version.txt
    ├── variables-output.txt
    ├── input-output.txt
    ├── conversion-output.txt
    ├── calculator-output.txt
    ├── grade-calculator-output.txt
    └── syntax-check.txt
```

---

# 📝 Generate Evidence

Record the Python version:

```bash
python3 --version > evidence/python-version.txt
```

Record variable demonstration:

```bash
python3 variables_demo.py > evidence/variables-output.txt
```

Record type conversion:

```bash
python3 type_conversion.py > evidence/conversion-output.txt
```

Record operations:

```bash
python3 operations_demo.py > evidence/calculator-output.txt
```

Check all Python files:

```bash
python3 -m py_compile *.py
```

Save the verification result:

```bash
python3 -m py_compile *.py 2> evidence/syntax-check.txt
```

> ⚠️ Review evidence before committing it. Do not store passwords, private information, API keys, tokens, or other secrets in your Git repository.

---

# 📊 Core Concepts Summary

| Concept   | Example           | Purpose            |
| --------- | ----------------- | ------------------ |
| Variable  | `name = "Abeera"` | Store data         |
| Integer   | `age = 20`        | Whole number       |
| Float     | `gpa = 3.75`      | Decimal number     |
| String    | `name = "Abeera"` | Text               |
| Boolean   | `active = True`   | True/False         |
| `type()`  | `type(age)`       | Identify type      |
| `input()` | `input("Name: ")` | Get user input     |
| `int()`   | `int("20")`       | Convert to integer |
| `float()` | `float("3.14")`   | Convert to float   |
| `str()`   | `str(20)`         | Convert to string  |
| `bool()`  | `bool(1)`         | Convert to Boolean |
| `+`       | `10 + 5`          | Addition           |
| `-`       | `10 - 5`          | Subtraction        |
| `*`       | `10 * 5`          | Multiplication     |
| `/`       | `10 / 5`          | Division           |
| `//`      | `10 // 3`         | Floor division     |
| `%`       | `10 % 3`          | Remainder          |
| `**`      | `2 ** 3`          | Power              |

---

# 🧠 Interview / Viva Questions

## 1. What is Python?

Python is a high-level, general-purpose programming language known for its simple syntax and wide range of applications.

## 2. What is a variable?

A variable is a name used to reference/store a value.

Example:

```python
age = 20
```

## 3. What are the four basic data types covered in this lab?

```text
int
float
str
bool
```

## 4. What does `type()` do?

It identifies the data type of a value or variable.

Example:

```python
type(20)
```

returns:

```text
<class 'int'>
```

## 5. What does `input()` return?

`input()` returns a string.

Even numeric-looking input initially comes in as a string.

## 6. How do you convert a string to an integer?

```python
int("25")
```

## 7. How do you convert a string to a float?

```python
float("3.14")
```

## 8. What happens when a float is converted to an integer?

The decimal portion is truncated.

Example:

```python
int(3.99)
```

returns:

```text
3
```

## 9. What is a Boolean?

A Boolean represents one of two values:

```python
True
False
```

## 10. Why is type conversion important?

It allows programs to use data in the correct form, especially when processing user input.

---

# 💼 Practical Application

The concepts from this lab are directly useful in automation and DevOps.

For example, a Python automation script may collect:

```python
server_name = input("Server name: ")
port = int(input("Port: "))
enabled = True
```

Here:

```text
server_name → str
port        → int
enabled     → bool
```

These basic concepts later become important when working with:

* Linux automation
* AWS
* APIs
* Configuration files
* JSON
* Infrastructure automation
* Data analysis
* Monitoring scripts
* DevOps tools
* AI/ML applications

---

# 🧩 Concept Flow

```text
User Input
    │
    ▼
input()
    │
    ▼
String Data
    │
    ▼
Type Conversion
    │
    ├── int()
    ├── float()
    ├── str()
    └── bool()
    │
    ▼
Processing
    │
    ├── Arithmetic
    ├── String Operations
    └── Conditions
    │
    ▼
Output
```

---

# ✅ Lab Completion Checklist

* [ ] Verified Python installation.
* [ ] Created the Lab 01 directory.
* [ ] Created `variables_demo.py`.
* [ ] Practiced `int`.
* [ ] Practiced `float`.
* [ ] Practiced `str`.
* [ ] Practiced `bool`.
* [ ] Used `type()`.
* [ ] Practiced variable naming.
* [ ] Practiced multiple assignment.
* [ ] Used `input()`.
* [ ] Confirmed that `input()` returns strings.
* [ ] Practiced `int()` conversion.
* [ ] Practiced `float()` conversion.
* [ ] Practiced `str()` conversion.
* [ ] Practiced `bool()` conversion.
* [ ] Built an interactive calculator.
* [ ] Practiced arithmetic operators.
* [ ] Practiced string operations.
* [ ] Built a student grade calculator.
* [ ] Practiced `try/except`.
* [ ] Tested invalid input.
* [ ] Checked Python syntax.
* [ ] Created evidence files.
* [ ] Reviewed evidence for sensitive information.

---

# 🏁 Conclusion

Lab 01 established the foundation for Python programming by introducing **syntax, variables, data types, user input, type conversion, arithmetic operations, strings, Boolean values, and basic error handling**.

The most important concepts learned were:

```python
# Variables
name = "Abeera"

# Integer
age = 20

# Float
gpa = 3.75

# Boolean
is_active = True

# Check type
type(age)

# User input
name = input("Enter your name: ")

# Type conversion
age = int(input("Enter your age: "))
```

These concepts are fundamental to almost every Python program.

The lab also demonstrated how simple Python concepts can be combined to create a practical application such as a **student grade calculator**.

---

# 🚀 Next Steps

After completing this lab, the recommended progression is:

```text
Lab 01
Python Syntax & Data Types
        ↓
Variables & Input
        ↓
Type Conversion
        ↓
Lists & Tuples
        ↓
Dictionaries & Sets
        ↓
Conditional Statements
        ↓
Loops
        ↓
Functions
        ↓
File Handling
        ↓
Modules & Packages
        ↓
Data Science / Automation
```

---

## 📂 Final Lab Structure

```text
Lab-01-Python-Syntax-and-Data-Types/
│
├── README.md
│
├── variables_demo.py
├── variable_naming.py
├── user_input_demo.py
├── advanced_input.py
├── type_conversion.py
├── interactive_calculator.py
├── operations_demo.py
├── grade_calculator.py
├── error_examples.py
│
└── evidence/
    ├── python-version.txt
    ├── variables-output.txt
    ├── input-output.txt
    ├── conversion-output.txt
    ├── calculator-output.txt
    ├── grade-calculator-output.txt
    └── syntax-check.txt
```

---

**Lab:** 01 — Python Syntax and Data Types

**Status:** ✅ Completed

**Difficulty:** Beginner

**Primary Skills:** `Python 3` · Variables · `int` · `float` · `str` · `bool` · `type()` · `input()` · Type Conversion · Arithmetic · Strings · Error Handling
# Lab 01: Python Syntax and Data Types

## 📌 Lab Overview

This lab introduces the fundamental building blocks of Python programming.

The focus is on:

* Python syntax
* Variables
* Variable naming rules
* Basic data types
* `int`
* `float`
* `str`
* `bool`
* The `type()` function
* The `input()` function
* Type conversion
* Arithmetic operations
* String operations
* Basic error handling
* Practical user-input programs

This lab is designed for beginners and provides the foundation required for future Python topics such as **lists, dictionaries, functions, file handling, automation, data analysis, and AI/ML workflows**.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

* Understand basic Python syntax.
* Create and execute Python scripts.
* Create and assign variables.
* Follow Python variable naming rules.
* Identify common Python data types.
* Use the `type()` function.
* Collect user input using `input()`.
* Understand that `input()` returns a string.
* Convert values between different data types.
* Perform arithmetic operations.
* Perform basic string operations.
* Work with Boolean values.
* Handle common type-conversion errors.
* Build a practical student grade calculator.
* Verify Python programs from the Linux terminal.

---

# 🛠️ Prerequisites

No previous programming experience is required.

Basic knowledge of:

* Linux terminal
* Creating files
* Editing text files
* Running commands

is helpful.

---

# 💻 Lab Environment

The lab is performed in a Linux-based cloud environment with Python available.

First, verify Python:

```bash
python3 --version
```

Example:

```text
Python 3.12.3
```

Also check the location of Python:

```bash
which python3
```

Example:

```text
/usr/bin/python3
```

---

# 📁 Lab Directory Setup

Create a dedicated directory for Lab 01:

```bash
mkdir -p ~/python_lab1
cd ~/python_lab1
```

Verify the current directory:

```bash
pwd
```

Verify the directory contents:

```bash
ls -la
```

---

# 🧠 Task 1: Python Variables and Basic Data Types

## 1.1 Create the First Python Script

Create the file:

```bash
nano variables_demo.py
```

Add:

```python
# Lab 1: Python Variables and Data Types Demo

print("=== Python Data Types Demonstration ===")
print()

# Integer
student_age = 20
print("Student Age:", student_age)
print("Type of student_age:", type(student_age))
print()

# Float
student_gpa = 3.75
print("Student GPA:", student_gpa)
print("Type of student_gpa:", type(student_gpa))
print()

# String
student_name = "Alice Johnson"
print("Student Name:", student_name)
print("Type of student_name:", type(student_name))
print()

# Boolean
is_enrolled = True
print("Is Enrolled:", is_enrolled)
print("Type of is_enrolled:", type(is_enrolled))
print()

print("=== End of Data Types Demo ===")
```

Save and exit:

```text
Ctrl + X
Y
Enter
```

Run:

```bash
python3 variables_demo.py
```

---

# 📊 Python's Four Basic Data Types

| Data Type | Python Type | Example          | Purpose         |
| --------- | ----------- | ---------------- | --------------- |
| Integer   | `int`       | `20`             | Whole numbers   |
| Float     | `float`     | `3.75`           | Decimal numbers |
| String    | `str`       | `"Alice"`        | Text            |
| Boolean   | `bool`      | `True` / `False` | Logical values  |

---

# 🔢 `int` — Integer

An integer is a whole number.

Example:

```python
age = 20
```

Check its type:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

Examples:

```python
students = 30
score = 95
year = 2026
```

---

# 🔢 `float` — Floating-Point Number

A float represents a number containing a decimal value.

Example:

```python
gpa = 3.75
```

Check:

```python
print(type(gpa))
```

Output:

```text
<class 'float'>
```

Examples:

```python
price = 19.99
temperature = 25.5
percentage = 87.5
```

---

# 📝 `str` — String

A string represents text.

Example:

```python
name = "Alice Johnson"
```

Check:

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

Strings are normally written inside:

```python
"double quotes"
```

or:

```python
'single quotes'
```

---

# ✅ `bool` — Boolean

A Boolean represents one of two logical values:

```python
True
False
```

Example:

```python
is_enrolled = True
```

Check:

```python
print(type(is_enrolled))
```

Output:

```text
<class 'bool'>
```

Boolean values are commonly used in:

* Conditions
* Authentication
* Validation
* Program decisions
* Automation

---

# 🧪 Task 1.2: Variable Naming Rules

Create:

```bash
nano variable_naming.py
```

Add:

```python
# Variable Naming Rules and Examples

print("=== Variable Naming Examples ===")
print()

# Valid variable names
first_name = "John"
last_name = "Smith"
age_in_years = 25
course_code_2024 = "CS101"
_private_variable = "hidden"

print("Valid variable examples:")
print("first_name:", first_name)
print("last_name:", last_name)
print("age_in_years:", age_in_years)
print("course_code_2024:", course_code_2024)
print("_private_variable:", _private_variable)
print()

# Multiple assignment
x, y, z = 10, 20.5, "Hello"

print("Multiple assignment:")
print("x =", x, "| Type:", type(x))
print("y =", y, "| Type:", type(y))
print("z =", z, "| Type:", type(z))
print()

# Same value assigned to multiple variables
a = b = c = 100

print("Same value assignment:")
print("a =", a, "| b =", b, "| c =", c)
```

Run:

```bash
python3 variable_naming.py
```

---

# 📌 Python Variable Naming Rules

Python variable names:

### ✅ Can contain:

* Letters
* Numbers
* Underscores

Examples:

```python
student_name
student1
course_2026
```

### ❌ Cannot start with a number

Invalid:

```python
1student = "Abeera"
```

Valid:

```python
student1 = "Abeera"
```

### ❌ Cannot contain spaces

Invalid:

```python
student name = "Abeera"
```

Valid:

```python
student_name = "Abeera"
```

### ❌ Cannot use Python keywords

For example:

```python
class
if
for
while
def
```

should not be used as normal variable names.

---

# ⌨️ Task 2: Working With `input()`

## 2.1 Basic User Input

Create:

```bash
nano user_input_demo.py
```

Add:

```python
# User Input Demonstration

print("=== User Input Collection ===")
print()

print("Let's collect some information about you!")

user_name = input("Please enter your name: ")

print("Hello,", user_name + "!")
print("Type of user_name:", type(user_name))
print()

user_age_str = input("Please enter your age: ")

print("You entered:", user_age_str)
print("Type of user_age_str:", type(user_age_str))
print()

favorite_number_str = input("Enter your favorite number: ")

print("Your favorite number is:", favorite_number_str)
print("Type:", type(favorite_number_str))
print()

print("Notice: input() returns a string.")
```

Run:

```bash
python3 user_input_demo.py
```

Test with:

```text
Name: Abeera
Age: 20
Favorite number: 7
```

---

# ⭐ Important Concept: `input()` Returns a String

Even if the user enters:

```text
20
```

Python initially stores it as:

```python
"20"
```

Therefore:

```python
age = input("Enter age: ")
```

results in:

```python
type(age)
```

being:

```text
<class 'str'>
```

If you need an integer, convert it:

```python
age = int(input("Enter age: "))
```

---

# 🧪 Task 2.2: Advanced Input Handling

Create:

```bash
nano advanced_input.py
```

Add:

```python
# Advanced Input Handling

print("=== Advanced Input Handling ===")
print()

print("Student Registration System")
print("-" * 30)

student_name = input("Student Name: ")
student_id = input("Student ID: ")
email = input("Email Address: ")

print()
print("Registration Summary:")
print("Name:", student_name)
print("ID:", student_id)
print("Email:", email)
print()

course_selection = input("Select your course (CS/IT/ENG): ")
semester = input("Enter semester (Fall/Spring/Summer): ")

print()
print("Course Information:")
print("Selected Course:", course_selection)
print("Semester:", semester)
print()

is_full_time = input("Are you a full-time student? (yes/no): ")

print("Full-time status:", is_full_time)
print("Type:", type(is_full_time))
```

Run:

```bash
python3 advanced_input.py
```

---

# 🔄 Task 3: Type Conversion

Type conversion means changing a value from one data type to another.

Common conversion functions:

| Function  | Converts To |
| --------- | ----------- |
| `int()`   | Integer     |
| `float()` | Float       |
| `str()`   | String      |
| `bool()`  | Boolean     |

---

# 🧪 Task 3.1: Basic Type Conversion

Create:

```bash
nano type_conversion.py
```

Add:

```python
# Type Conversion Demonstration

print("=== Type Conversion Examples ===")
print()

# String to Integer
age_str = "25"
age_int = int(age_str)

print("Original string:", age_str)
print("Type:", type(age_str))
print("Converted to int:", age_int)
print("Type:", type(age_int))
print()

# String to Float
price_str = "19.99"
price_float = float(price_str)

print("Original string:", price_str)
print("Type:", type(price_str))
print("Converted to float:", price_float)
print("Type:", type(price_float))
print()

# Integer to String
score = 95
score_str = str(score)

print("Original integer:", score)
print("Type:", type(score))
print("Converted to string:", score_str)
print("Type:", type(score_str))
print()

# Float to Integer
gpa = 3.87
gpa_int = int(gpa)

print("Original float:", gpa)
print("Converted to int:", gpa_int)
print("Note: The decimal portion is truncated.")
print()

# Boolean conversions
print("Boolean Conversion:")
print("int(True):", int(True))
print("int(False):", int(False))
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))
```

Run:

```bash
python3 type_conversion.py
```

---

# ⚠️ Important: Integer Conversion Truncates

Consider:

```python
number = 3.87
result = int(number)
```

The result is:

```text
3
```

Python does not round it to `4`.

It removes the decimal portion.

---

# 🧮 Task 3.2: Interactive Calculator

Create:

```bash
nano interactive_calculator.py
```

Add:

```python
# Interactive Calculator

print("=== Simple Calculator ===")
print()

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

num1 = float(num1_str)
num2 = float(num2_str)

print()
print("Input Analysis:")
print("First input:", num1_str)
print("After conversion:", num1)
print("Type:", type(num1))
print()

print("Calculation Results:")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")

print()
print("Type Conversion of Results:")
print("Addition as integer:", int(addition))
print("Addition as string:", str(addition))
```

Run:

```bash
python3 interactive_calculator.py
```

Example:

```text
First number: 15.5
Second number: 4.2
```

---

# ➕ Task 4: Arithmetic Operations

Create:

```bash
nano operations_demo.py
```

Add:

```python
# Basic Operations with Different Data Types

print("=== Arithmetic Operations ===")
print()

a = 10
b = 3

print("Integer Operations:")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print()

x = 15.5
y = 2.5

print("Float Operations:")
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print()

print("Mixed Operations:")
result1 = a + x
result2 = b * y

print(f"{a} + {x} = {result1}")
print(f"Type: {type(result1)}")

print(f"{b} * {y} = {result2}")
print(f"Type: {type(result2)}")
print()

first_name = "John"
last_name = "Doe"

print("String Operations:")
print("Concatenation:", first_name + " " + last_name)
print("Repetition:", first_name * 3)
print("Length:", len(first_name))
```

Run:

```bash
python3 operations_demo.py
```

---

# 📊 Python Arithmetic Operators

| Operator | Meaning           | Example   |
| -------- | ----------------- | --------- |
| `+`      | Addition          | `10 + 3`  |
| `-`      | Subtraction       | `10 - 3`  |
| `*`      | Multiplication    | `10 * 3`  |
| `/`      | Division          | `10 / 3`  |
| `//`     | Floor division    | `10 // 3` |
| `%`      | Modulus/remainder | `10 % 3`  |
| `**`     | Exponentiation    | `10 ** 3` |

---

# 📝 String Operations

Python also allows basic operations on strings.

### Concatenation

```python
first = "Hello"
last = "World"

result = first + " " + last
```

Result:

```text
Hello World
```

### Repetition

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

### Length

```python
name = "Abeera"
print(len(name))
```

---

# 🎓 Task 4.2: Practical Student Grade Calculator

Create:

```bash
nano grade_calculator.py
```

Add:

```python
# Student Grade Calculator

print("=== Student Grade Calculator ===")
print()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
course_name = input("Enter course name: ")

print()
print("Enter assessment scores:")

quiz1 = float(input("Quiz 1 score: "))
quiz2 = float(input("Quiz 2 score: "))
midterm = float(input("Midterm score: "))
final = float(input("Final exam score: "))
project = float(input("Project score: "))

quiz_average = (quiz1 + quiz2) / 2

weighted_score = (
    (quiz_average * 0.20)
    + (midterm * 0.25)
    + (final * 0.35)
    + (project * 0.20)
)

if weighted_score >= 90:
    letter_grade = "A"
elif weighted_score >= 80:
    letter_grade = "B"
elif weighted_score >= 70:
    letter_grade = "C"
elif weighted_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

is_passing = weighted_score >= 60

print()
print("=== Final Grade Report ===")
print("Student:", student_name)
print("ID:", student_id)
print("Course:", course_name)
print()

print("Quiz Average:", f"{quiz_average:.2f}")
print("Midterm:", midterm)
print("Final:", final)
print("Project:", project)
print()

print("Weighted Final Score:", f"{weighted_score:.2f}")
print("Letter Grade:", letter_grade)
print("Passing Status:", is_passing)
print("Status Type:", type(is_passing))

print()
print("=== Type Conversion Examples ===")
print("Final score as integer:", int(weighted_score))
print("Final score as string:", str(weighted_score))
print("Passing status as integer:", int(is_passing))
```

Run:

```bash
python3 grade_calculator.py
```

Example test data:

```text
Student name: Sarah Johnson
Student ID: 12345
Course: Introduction to Python
Quiz 1: 85
Quiz 2: 92
Midterm: 78
Final: 88
Project: 95
```

---

# 🧪 Task 5: Error Handling

User input can contain invalid values.

For example:

```python
age = int("hello")
```

causes:

```text
ValueError
```

To handle this safely, Python provides `try` and `except`.

---

# 🛡️ Task 5.1: Safe Type Conversion

Create:

```bash
nano error_examples.py
```

Add:

```python
# Common Type Conversion Errors and Solutions

print("=== Error Handling Examples ===")
print()

user_input = input("Enter a whole number: ")

try:
    number = int(user_input)

    print("Conversion successful!")
    print("Number:", number)
    print("Type:", type(number))

except ValueError:
    print("Error: Invalid integer.")
    print("Please enter a whole number.")

print()

user_input2 = input("Enter a decimal number: ")

try:
    decimal_number = float(user_input2)

    print("Conversion successful!")
    print("Number:", decimal_number)
    print("Type:", type(decimal_number))

except ValueError:
    print("Error: Invalid decimal number.")
    print("Please enter a valid number.")
```

Run:

```bash
python3 error_examples.py
```

Test with:

```text
42
```

Then test again with:

```text
hello
```

Observe the difference.

---

# 🔍 Boolean Conversion

Test:

```python
print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))
```

Expected:

```text
True
False
True
False
```

### Important clarification

For strings:

```python
bool("False")
```

returns:

```text
True
```

because `"False"` is a **non-empty string**.

It does not automatically interpret the text `"False"` as the Boolean value `False`.

---

# 🔧 Troubleshooting

## Issue 1: Python Is Not Found

Run:

```bash
python3 --version
```

Also try:

```bash
python --version
```

Find Python:

```bash
which python3
```

---

## Issue 2: `IndentationError`

Python uses indentation to define code blocks.

Incorrect:

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

Use **4 spaces** for normal indentation.

---

# ❌ Issue 3: `ValueError`

Example:

```python
age = int("hello")
```

Error:

```text
ValueError
```

Solution:

```python
try:
    age = int(user_input)
except ValueError:
    print("Please enter a valid number.")
```

---

# ❌ Issue 4: `ZeroDivisionError`

This will fail:

```python
result = 10 / 0
```

Use validation before performing division.

For example:

```python
if num2 != 0:
    result = num1 / num2
else:
    print("Cannot divide by zero.")
```

---

# ❌ Issue 5: File Not Found

Check your current directory:

```bash
pwd
```

List files:

```bash
ls -la
```

Return to the lab directory:

```bash
cd ~/python_lab1
```

---

# 🧪 Lab Verification

Run:

```bash
cd ~/python_lab1
```

List all scripts:

```bash
ls -lh
```

Expected files include:

```text
variables_demo.py
variable_naming.py
user_input_demo.py
advanced_input.py
type_conversion.py
interactive_calculator.py
operations_demo.py
grade_calculator.py
error_examples.py
```

---

# 🔎 Syntax Verification

Python provides a useful way to check whether a script has syntax errors without running it:

```bash
python3 -m py_compile variables_demo.py
```

Repeat for the other scripts:

```bash
python3 -m py_compile variable_naming.py
python3 -m py_compile user_input_demo.py
python3 -m py_compile advanced_input.py
python3 -m py_compile type_conversion.py
python3 -m py_compile interactive_calculator.py
python3 -m py_compile operations_demo.py
python3 -m py_compile grade_calculator.py
python3 -m py_compile error_examples.py
```

If there is no output, the syntax check passed.

---

# 📂 Suggested Evidence Structure

For a professional GitHub portfolio, keep evidence organized:

```text
Lab-01-Python-Syntax-and-Data-Types/
├── README.md
├── variables_demo.py
├── variable_naming.py
├── user_input_demo.py
├── advanced_input.py
├── type_conversion.py
├── interactive_calculator.py
├── operations_demo.py
├── grade_calculator.py
├── error_examples.py
└── evidence/
    ├── python-version.txt
    ├── variables-output.txt
    ├── input-output.txt
    ├── conversion-output.txt
    ├── calculator-output.txt
    ├── grade-calculator-output.txt
    └── syntax-check.txt
```

---

# 📝 Generate Evidence

Record the Python version:

```bash
python3 --version > evidence/python-version.txt
```

Record variable demonstration:

```bash
python3 variables_demo.py > evidence/variables-output.txt
```

Record type conversion:

```bash
python3 type_conversion.py > evidence/conversion-output.txt
```

Record operations:

```bash
python3 operations_demo.py > evidence/calculator-output.txt
```

Check all Python files:

```bash
python3 -m py_compile *.py
```

Save the verification result:

```bash
python3 -m py_compile *.py 2> evidence/syntax-check.txt
```

> ⚠️ Review evidence before committing it. Do not store passwords, private information, API keys, tokens, or other secrets in your Git repository.

---

# 📊 Core Concepts Summary

| Concept   | Example           | Purpose            |
| --------- | ----------------- | ------------------ |
| Variable  | `name = "Abeera"` | Store data         |
| Integer   | `age = 20`        | Whole number       |
| Float     | `gpa = 3.75`      | Decimal number     |
| String    | `name = "Abeera"` | Text               |
| Boolean   | `active = True`   | True/False         |
| `type()`  | `type(age)`       | Identify type      |
| `input()` | `input("Name: ")` | Get user input     |
| `int()`   | `int("20")`       | Convert to integer |
| `float()` | `float("3.14")`   | Convert to float   |
| `str()`   | `str(20)`         | Convert to string  |
| `bool()`  | `bool(1)`         | Convert to Boolean |
| `+`       | `10 + 5`          | Addition           |
| `-`       | `10 - 5`          | Subtraction        |
| `*`       | `10 * 5`          | Multiplication     |
| `/`       | `10 / 5`          | Division           |
| `//`      | `10 // 3`         | Floor division     |
| `%`       | `10 % 3`          | Remainder          |
| `**`      | `2 ** 3`          | Power              |

---

# 🧠 Interview / Viva Questions

## 1. What is Python?

Python is a high-level, general-purpose programming language known for its simple syntax and wide range of applications.

## 2. What is a variable?

A variable is a name used to reference/store a value.

Example:

```python
age = 20
```

## 3. What are the four basic data types covered in this lab?

```text
int
float
str
bool
```

## 4. What does `type()` do?

It identifies the data type of a value or variable.

Example:

```python
type(20)
```

returns:

```text
<class 'int'>
```

## 5. What does `input()` return?

`input()` returns a string.

Even numeric-looking input initially comes in as a string.

## 6. How do you convert a string to an integer?

```python
int("25")
```

## 7. How do you convert a string to a float?

```python
float("3.14")
```

## 8. What happens when a float is converted to an integer?

The decimal portion is truncated.

Example:

```python
int(3.99)
```

returns:

```text
3
```

## 9. What is a Boolean?

A Boolean represents one of two values:

```python
True
False
```

## 10. Why is type conversion important?

It allows programs to use data in the correct form, especially when processing user input.

---

# 💼 Practical Application

The concepts from this lab are directly useful in automation and DevOps.

For example, a Python automation script may collect:

```python
server_name = input("Server name: ")
port = int(input("Port: "))
enabled = True
```

Here:

```text
server_name → str
port        → int
enabled     → bool
```

These basic concepts later become important when working with:

* Linux automation
* AWS
* APIs
* Configuration files
* JSON
* Infrastructure automation
* Data analysis
* Monitoring scripts
* DevOps tools
* AI/ML applications

---

# 🧩 Concept Flow

```text
User Input
    │
    ▼
input()
    │
    ▼
String Data
    │
    ▼
Type Conversion
    │
    ├── int()
    ├── float()
    ├── str()
    └── bool()
    │
    ▼
Processing
    │
    ├── Arithmetic
    ├── String Operations
    └── Conditions
    │
    ▼
Output
```

---

# ✅ Lab Completion Checklist

* [ ] Verified Python installation.
* [ ] Created the Lab 01 directory.
* [ ] Created `variables_demo.py`.
* [ ] Practiced `int`.
* [ ] Practiced `float`.
* [ ] Practiced `str`.
* [ ] Practiced `bool`.
* [ ] Used `type()`.
* [ ] Practiced variable naming.
* [ ] Practiced multiple assignment.
* [ ] Used `input()`.
* [ ] Confirmed that `input()` returns strings.
* [ ] Practiced `int()` conversion.
* [ ] Practiced `float()` conversion.
* [ ] Practiced `str()` conversion.
* [ ] Practiced `bool()` conversion.
* [ ] Built an interactive calculator.
* [ ] Practiced arithmetic operators.
* [ ] Practiced string operations.
* [ ] Built a student grade calculator.
* [ ] Practiced `try/except`.
* [ ] Tested invalid input.
* [ ] Checked Python syntax.
* [ ] Created evidence files.
* [ ] Reviewed evidence for sensitive information.

---

# 🏁 Conclusion

Lab 01 established the foundation for Python programming by introducing **syntax, variables, data types, user input, type conversion, arithmetic operations, strings, Boolean values, and basic error handling**.

The most important concepts learned were:

```python
# Variables
name = "Abeera"

# Integer
age = 20

# Float
gpa = 3.75

# Boolean
is_active = True

# Check type
type(age)

# User input
name = input("Enter your name: ")

# Type conversion
age = int(input("Enter your age: "))
```

These concepts are fundamental to almost every Python program.

The lab also demonstrated how simple Python concepts can be combined to create a practical application such as a **student grade calculator**.

---

# 🚀 Next Steps

After completing this lab, the recommended progression is:

```text
Lab 01
Python Syntax & Data Types
        ↓
Variables & Input
        ↓
Type Conversion
        ↓
Lists & Tuples
        ↓
Dictionaries & Sets
        ↓
Conditional Statements
        ↓
Loops
        ↓
Functions
        ↓
File Handling
        ↓
Modules & Packages
        ↓
Data Science / Automation
```

---

## 📂 Final Lab Structure

```text
Lab-01-Python-Syntax-and-Data-Types/
│
├── README.md
│
├── variables_demo.py
├── variable_naming.py
├── user_input_demo.py
├── advanced_input.py
├── type_conversion.py
├── interactive_calculator.py
├── operations_demo.py
├── grade_calculator.py
├── error_examples.py
│
└── evidence/
    ├── python-version.txt
    ├── variables-output.txt
    ├── input-output.txt
    ├── conversion-output.txt
    ├── calculator-output.txt
    ├── grade-calculator-output.txt
    └── syntax-check.txt
```

---

**Lab:** 01 — Python Syntax and Data Types

**Status:** ✅ Completed

**Difficulty:** Beginner

**Primary Skills:** `Python 3` · Variables · `int` · `float` · `str` · `bool` · `type()` · `input()` · Type Conversion · Arithmetic · Strings · Error Handling
# Lab 01: Python Syntax and Data Types

## 📌 Lab Overview

This lab introduces the fundamental building blocks of Python programming.

The focus is on:

* Python syntax
* Variables
* Variable naming rules
* Basic data types
* `int`
* `float`
* `str`
* `bool`
* The `type()` function
* The `input()` function
* Type conversion
* Arithmetic operations
* String operations
* Basic error handling
* Practical user-input programs

This lab is designed for beginners and provides the foundation required for future Python topics such as **lists, dictionaries, functions, file handling, automation, data analysis, and AI/ML workflows**.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

* Understand basic Python syntax.
* Create and execute Python scripts.
* Create and assign variables.
* Follow Python variable naming rules.
* Identify common Python data types.
* Use the `type()` function.
* Collect user input using `input()`.
* Understand that `input()` returns a string.
* Convert values between different data types.
* Perform arithmetic operations.
* Perform basic string operations.
* Work with Boolean values.
* Handle common type-conversion errors.
* Build a practical student grade calculator.
* Verify Python programs from the Linux terminal.

---

# 🛠️ Prerequisites

No previous programming experience is required.

Basic knowledge of:

* Linux terminal
* Creating files
* Editing text files
* Running commands

is helpful.

---

# 💻 Lab Environment

The lab is performed in a Linux-based cloud environment with Python available.

First, verify Python:

```bash
python3 --version
```

Example:

```text
Python 3.12.3
```

Also check the location of Python:

```bash
which python3
```

Example:

```text
/usr/bin/python3
```

---

# 📁 Lab Directory Setup

Create a dedicated directory for Lab 01:

```bash
mkdir -p ~/python_lab1
cd ~/python_lab1
```

Verify the current directory:

```bash
pwd
```

Verify the directory contents:

```bash
ls -la
```

---

# 🧠 Task 1: Python Variables and Basic Data Types

## 1.1 Create the First Python Script

Create the file:

```bash
nano variables_demo.py
```

Add:

```python
# Lab 1: Python Variables and Data Types Demo

print("=== Python Data Types Demonstration ===")
print()

# Integer
student_age = 20
print("Student Age:", student_age)
print("Type of student_age:", type(student_age))
print()

# Float
student_gpa = 3.75
print("Student GPA:", student_gpa)
print("Type of student_gpa:", type(student_gpa))
print()

# String
student_name = "Alice Johnson"
print("Student Name:", student_name)
print("Type of student_name:", type(student_name))
print()

# Boolean
is_enrolled = True
print("Is Enrolled:", is_enrolled)
print("Type of is_enrolled:", type(is_enrolled))
print()

print("=== End of Data Types Demo ===")
```

Save and exit:

```text
Ctrl + X
Y
Enter
```

Run:

```bash
python3 variables_demo.py
```

---

# 📊 Python's Four Basic Data Types

| Data Type | Python Type | Example          | Purpose         |
| --------- | ----------- | ---------------- | --------------- |
| Integer   | `int`       | `20`             | Whole numbers   |
| Float     | `float`     | `3.75`           | Decimal numbers |
| String    | `str`       | `"Alice"`        | Text            |
| Boolean   | `bool`      | `True` / `False` | Logical values  |

---

# 🔢 `int` — Integer

An integer is a whole number.

Example:

```python
age = 20
```

Check its type:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

Examples:

```python
students = 30
score = 95
year = 2026
```

---

# 🔢 `float` — Floating-Point Number

A float represents a number containing a decimal value.

Example:

```python
gpa = 3.75
```

Check:

```python
print(type(gpa))
```

Output:

```text
<class 'float'>
```

Examples:

```python
price = 19.99
temperature = 25.5
percentage = 87.5
```

---

# 📝 `str` — String

A string represents text.

Example:

```python
name = "Alice Johnson"
```

Check:

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

Strings are normally written inside:

```python
"double quotes"
```

or:

```python
'single quotes'
```

---

# ✅ `bool` — Boolean

A Boolean represents one of two logical values:

```python
True
False
```

Example:

```python
is_enrolled = True
```

Check:

```python
print(type(is_enrolled))
```

Output:

```text
<class 'bool'>
```

Boolean values are commonly used in:

* Conditions
* Authentication
* Validation
* Program decisions
* Automation

---

# 🧪 Task 1.2: Variable Naming Rules

Create:

```bash
nano variable_naming.py
```

Add:

```python
# Variable Naming Rules and Examples

print("=== Variable Naming Examples ===")
print()

# Valid variable names
first_name = "John"
last_name = "Smith"
age_in_years = 25
course_code_2024 = "CS101"
_private_variable = "hidden"

print("Valid variable examples:")
print("first_name:", first_name)
print("last_name:", last_name)
print("age_in_years:", age_in_years)
print("course_code_2024:", course_code_2024)
print("_private_variable:", _private_variable)
print()

# Multiple assignment
x, y, z = 10, 20.5, "Hello"

print("Multiple assignment:")
print("x =", x, "| Type:", type(x))
print("y =", y, "| Type:", type(y))
print("z =", z, "| Type:", type(z))
print()

# Same value assigned to multiple variables
a = b = c = 100

print("Same value assignment:")
print("a =", a, "| b =", b, "| c =", c)
```

Run:

```bash
python3 variable_naming.py
```

---

# 📌 Python Variable Naming Rules

Python variable names:

### ✅ Can contain:

* Letters
* Numbers
* Underscores

Examples:

```python
student_name
student1
course_2026
```

### ❌ Cannot start with a number

Invalid:

```python
1student = "Abeera"
```

Valid:

```python
student1 = "Abeera"
```

### ❌ Cannot contain spaces

Invalid:

```python
student name = "Abeera"
```

Valid:

```python
student_name = "Abeera"
```

### ❌ Cannot use Python keywords

For example:

```python
class
if
for
while
def
```

should not be used as normal variable names.

---

# ⌨️ Task 2: Working With `input()`

## 2.1 Basic User Input

Create:

```bash
nano user_input_demo.py
```

Add:

```python
# User Input Demonstration

print("=== User Input Collection ===")
print()

print("Let's collect some information about you!")

user_name = input("Please enter your name: ")

print("Hello,", user_name + "!")
print("Type of user_name:", type(user_name))
print()

user_age_str = input("Please enter your age: ")

print("You entered:", user_age_str)
print("Type of user_age_str:", type(user_age_str))
print()

favorite_number_str = input("Enter your favorite number: ")

print("Your favorite number is:", favorite_number_str)
print("Type:", type(favorite_number_str))
print()

print("Notice: input() returns a string.")
```

Run:

```bash
python3 user_input_demo.py
```

Test with:

```text
Name: Abeera
Age: 20
Favorite number: 7
```

---

# ⭐ Important Concept: `input()` Returns a String

Even if the user enters:

```text
20
```

Python initially stores it as:

```python
"20"
```

Therefore:

```python
age = input("Enter age: ")
```

results in:

```python
type(age)
```

being:

```text
<class 'str'>
```

If you need an integer, convert it:

```python
age = int(input("Enter age: "))
```

---

# 🧪 Task 2.2: Advanced Input Handling

Create:

```bash
nano advanced_input.py
```

Add:

```python
# Advanced Input Handling

print("=== Advanced Input Handling ===")
print()

print("Student Registration System")
print("-" * 30)

student_name = input("Student Name: ")
student_id = input("Student ID: ")
email = input("Email Address: ")

print()
print("Registration Summary:")
print("Name:", student_name)
print("ID:", student_id)
print("Email:", email)
print()

course_selection = input("Select your course (CS/IT/ENG): ")
semester = input("Enter semester (Fall/Spring/Summer): ")

print()
print("Course Information:")
print("Selected Course:", course_selection)
print("Semester:", semester)
print()

is_full_time = input("Are you a full-time student? (yes/no): ")

print("Full-time status:", is_full_time)
print("Type:", type(is_full_time))
```

Run:

```bash
python3 advanced_input.py
```

---

# 🔄 Task 3: Type Conversion

Type conversion means changing a value from one data type to another.

Common conversion functions:

| Function  | Converts To |
| --------- | ----------- |
| `int()`   | Integer     |
| `float()` | Float       |
| `str()`   | String      |
| `bool()`  | Boolean     |

---

# 🧪 Task 3.1: Basic Type Conversion

Create:

```bash
nano type_conversion.py
```

Add:

```python
# Type Conversion Demonstration

print("=== Type Conversion Examples ===")
print()

# String to Integer
age_str = "25"
age_int = int(age_str)

print("Original string:", age_str)
print("Type:", type(age_str))
print("Converted to int:", age_int)
print("Type:", type(age_int))
print()

# String to Float
price_str = "19.99"
price_float = float(price_str)

print("Original string:", price_str)
print("Type:", type(price_str))
print("Converted to float:", price_float)
print("Type:", type(price_float))
print()

# Integer to String
score = 95
score_str = str(score)

print("Original integer:", score)
print("Type:", type(score))
print("Converted to string:", score_str)
print("Type:", type(score_str))
print()

# Float to Integer
gpa = 3.87
gpa_int = int(gpa)

print("Original float:", gpa)
print("Converted to int:", gpa_int)
print("Note: The decimal portion is truncated.")
print()

# Boolean conversions
print("Boolean Conversion:")
print("int(True):", int(True))
print("int(False):", int(False))
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))
```

Run:

```bash
python3 type_conversion.py
```

---

# ⚠️ Important: Integer Conversion Truncates

Consider:

```python
number = 3.87
result = int(number)
```

The result is:

```text
3
```

Python does not round it to `4`.

It removes the decimal portion.

---

# 🧮 Task 3.2: Interactive Calculator

Create:

```bash
nano interactive_calculator.py
```

Add:

```python
# Interactive Calculator

print("=== Simple Calculator ===")
print()

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

num1 = float(num1_str)
num2 = float(num2_str)

print()
print("Input Analysis:")
print("First input:", num1_str)
print("After conversion:", num1)
print("Type:", type(num1))
print()

print("Calculation Results:")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")

print()
print("Type Conversion of Results:")
print("Addition as integer:", int(addition))
print("Addition as string:", str(addition))
```

Run:

```bash
python3 interactive_calculator.py
```

Example:

```text
First number: 15.5
Second number: 4.2
```

---

# ➕ Task 4: Arithmetic Operations

Create:

```bash
nano operations_demo.py
```

Add:

```python
# Basic Operations with Different Data Types

print("=== Arithmetic Operations ===")
print()

a = 10
b = 3

print("Integer Operations:")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print()

x = 15.5
y = 2.5

print("Float Operations:")
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print()

print("Mixed Operations:")
result1 = a + x
result2 = b * y

print(f"{a} + {x} = {result1}")
print(f"Type: {type(result1)}")

print(f"{b} * {y} = {result2}")
print(f"Type: {type(result2)}")
print()

first_name = "John"
last_name = "Doe"

print("String Operations:")
print("Concatenation:", first_name + " " + last_name)
print("Repetition:", first_name * 3)
print("Length:", len(first_name))
```

Run:

```bash
python3 operations_demo.py
```

---

# 📊 Python Arithmetic Operators

| Operator | Meaning           | Example   |
| -------- | ----------------- | --------- |
| `+`      | Addition          | `10 + 3`  |
| `-`      | Subtraction       | `10 - 3`  |
| `*`      | Multiplication    | `10 * 3`  |
| `/`      | Division          | `10 / 3`  |
| `//`     | Floor division    | `10 // 3` |
| `%`      | Modulus/remainder | `10 % 3`  |
| `**`     | Exponentiation    | `10 ** 3` |

---

# 📝 String Operations

Python also allows basic operations on strings.

### Concatenation

```python
first = "Hello"
last = "World"

result = first + " " + last
```

Result:

```text
Hello World
```

### Repetition

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

### Length

```python
name = "Abeera"
print(len(name))
```

---

# 🎓 Task 4.2: Practical Student Grade Calculator

Create:

```bash
nano grade_calculator.py
```

Add:

```python
# Student Grade Calculator

print("=== Student Grade Calculator ===")
print()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
course_name = input("Enter course name: ")

print()
print("Enter assessment scores:")

quiz1 = float(input("Quiz 1 score: "))
quiz2 = float(input("Quiz 2 score: "))
midterm = float(input("Midterm score: "))
final = float(input("Final exam score: "))
project = float(input("Project score: "))

quiz_average = (quiz1 + quiz2) / 2

weighted_score = (
    (quiz_average * 0.20)
    + (midterm * 0.25)
    + (final * 0.35)
    + (project * 0.20)
)

if weighted_score >= 90:
    letter_grade = "A"
elif weighted_score >= 80:
    letter_grade = "B"
elif weighted_score >= 70:
    letter_grade = "C"
elif weighted_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

is_passing = weighted_score >= 60

print()
print("=== Final Grade Report ===")
print("Student:", student_name)
print("ID:", student_id)
print("Course:", course_name)
print()

print("Quiz Average:", f"{quiz_average:.2f}")
print("Midterm:", midterm)
print("Final:", final)
print("Project:", project)
print()

print("Weighted Final Score:", f"{weighted_score:.2f}")
print("Letter Grade:", letter_grade)
print("Passing Status:", is_passing)
print("Status Type:", type(is_passing))

print()
print("=== Type Conversion Examples ===")
print("Final score as integer:", int(weighted_score))
print("Final score as string:", str(weighted_score))
print("Passing status as integer:", int(is_passing))
```

Run:

```bash
python3 grade_calculator.py
```

Example test data:

```text
Student name: Sarah Johnson
Student ID: 12345
Course: Introduction to Python
Quiz 1: 85
Quiz 2: 92
Midterm: 78
Final: 88
Project: 95
```

---

# 🧪 Task 5: Error Handling

User input can contain invalid values.

For example:

```python
age = int("hello")
```

causes:

```text
ValueError
```

To handle this safely, Python provides `try` and `except`.

---

# 🛡️ Task 5.1: Safe Type Conversion

Create:

```bash
nano error_examples.py
```

Add:

```python
# Common Type Conversion Errors and Solutions

print("=== Error Handling Examples ===")
print()

user_input = input("Enter a whole number: ")

try:
    number = int(user_input)

    print("Conversion successful!")
    print("Number:", number)
    print("Type:", type(number))

except ValueError:
    print("Error: Invalid integer.")
    print("Please enter a whole number.")

print()

user_input2 = input("Enter a decimal number: ")

try:
    decimal_number = float(user_input2)

    print("Conversion successful!")
    print("Number:", decimal_number)
    print("Type:", type(decimal_number))

except ValueError:
    print("Error: Invalid decimal number.")
    print("Please enter a valid number.")
```

Run:

```bash
python3 error_examples.py
```

Test with:

```text
42
```

Then test again with:

```text
hello
```

Observe the difference.

---

# 🔍 Boolean Conversion

Test:

```python
print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))
```

Expected:

```text
True
False
True
False
```

### Important clarification

For strings:

```python
bool("False")
```

returns:

```text
True
```

because `"False"` is a **non-empty string**.

It does not automatically interpret the text `"False"` as the Boolean value `False`.

---

# 🔧 Troubleshooting

## Issue 1: Python Is Not Found

Run:

```bash
python3 --version
```

Also try:

```bash
python --version
```

Find Python:

```bash
which python3
```

---

## Issue 2: `IndentationError`

Python uses indentation to define code blocks.

Incorrect:

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

Use **4 spaces** for normal indentation.

---

# ❌ Issue 3: `ValueError`

Example:

```python
age = int("hello")
```

Error:

```text
ValueError
```

Solution:

```python
try:
    age = int(user_input)
except ValueError:
    print("Please enter a valid number.")
```

---

# ❌ Issue 4: `ZeroDivisionError`

This will fail:

```python
result = 10 / 0
```

Use validation before performing division.

For example:

```python
if num2 != 0:
    result = num1 / num2
else:
    print("Cannot divide by zero.")
```

---

# ❌ Issue 5: File Not Found

Check your current directory:

```bash
pwd
```

List files:

```bash
ls -la
```

Return to the lab directory:

```bash
cd ~/python_lab1
```

---

# 🧪 Lab Verification

Run:

```bash
cd ~/python_lab1
```

List all scripts:

```bash
ls -lh
```

Expected files include:

```text
variables_demo.py
variable_naming.py
user_input_demo.py
advanced_input.py
type_conversion.py
interactive_calculator.py
operations_demo.py
grade_calculator.py
error_examples.py
```

---

# 🔎 Syntax Verification

Python provides a useful way to check whether a script has syntax errors without running it:

```bash
python3 -m py_compile variables_demo.py
```

Repeat for the other scripts:

```bash
python3 -m py_compile variable_naming.py
python3 -m py_compile user_input_demo.py
python3 -m py_compile advanced_input.py
python3 -m py_compile type_conversion.py
python3 -m py_compile interactive_calculator.py
python3 -m py_compile operations_demo.py
python3 -m py_compile grade_calculator.py
python3 -m py_compile error_examples.py
```

If there is no output, the syntax check passed.

---

# 📂 Suggested Evidence Structure

For a professional GitHub portfolio, keep evidence organized:

```text
Lab-01-Python-Syntax-and-Data-Types/
├── README.md
├── variables_demo.py
├── variable_naming.py
├── user_input_demo.py
├── advanced_input.py
├── type_conversion.py
├── interactive_calculator.py
├── operations_demo.py
├── grade_calculator.py
├── error_examples.py
└── evidence/
    ├── python-version.txt
    ├── variables-output.txt
    ├── input-output.txt
    ├── conversion-output.txt
    ├── calculator-output.txt
    ├── grade-calculator-output.txt
    └── syntax-check.txt
```

---

# 📝 Generate Evidence

Record the Python version:

```bash
python3 --version > evidence/python-version.txt
```

Record variable demonstration:

```bash
python3 variables_demo.py > evidence/variables-output.txt
```

Record type conversion:

```bash
python3 type_conversion.py > evidence/conversion-output.txt
```

Record operations:

```bash
python3 operations_demo.py > evidence/calculator-output.txt
```

Check all Python files:

```bash
python3 -m py_compile *.py
```

Save the verification result:

```bash
python3 -m py_compile *.py 2> evidence/syntax-check.txt
```

> ⚠️ Review evidence before committing it. Do not store passwords, private information, API keys, tokens, or other secrets in your Git repository.

---

# 📊 Core Concepts Summary

| Concept   | Example           | Purpose            |
| --------- | ----------------- | ------------------ |
| Variable  | `name = "Abeera"` | Store data         |
| Integer   | `age = 20`        | Whole number       |
| Float     | `gpa = 3.75`      | Decimal number     |
| String    | `name = "Abeera"` | Text               |
| Boolean   | `active = True`   | True/False         |
| `type()`  | `type(age)`       | Identify type      |
| `input()` | `input("Name: ")` | Get user input     |
| `int()`   | `int("20")`       | Convert to integer |
| `float()` | `float("3.14")`   | Convert to float   |
| `str()`   | `str(20)`         | Convert to string  |
| `bool()`  | `bool(1)`         | Convert to Boolean |
| `+`       | `10 + 5`          | Addition           |
| `-`       | `10 - 5`          | Subtraction        |
| `*`       | `10 * 5`          | Multiplication     |
| `/`       | `10 / 5`          | Division           |
| `//`      | `10 // 3`         | Floor division     |
| `%`       | `10 % 3`          | Remainder          |
| `**`      | `2 ** 3`          | Power              |

---

# 🧠 Interview / Viva Questions

## 1. What is Python?

Python is a high-level, general-purpose programming language known for its simple syntax and wide range of applications.

## 2. What is a variable?

A variable is a name used to reference/store a value.

Example:

```python
age = 20
```

## 3. What are the four basic data types covered in this lab?

```text
int
float
str
bool
```

## 4. What does `type()` do?

It identifies the data type of a value or variable.

Example:

```python
type(20)
```

returns:

```text
<class 'int'>
```

## 5. What does `input()` return?

`input()` returns a string.

Even numeric-looking input initially comes in as a string.

## 6. How do you convert a string to an integer?

```python
int("25")
```

## 7. How do you convert a string to a float?

```python
float("3.14")
```

## 8. What happens when a float is converted to an integer?

The decimal portion is truncated.

Example:

```python
int(3.99)
```

returns:

```text
3
```

## 9. What is a Boolean?

A Boolean represents one of two values:

```python
True
False
```

## 10. Why is type conversion important?

It allows programs to use data in the correct form, especially when processing user input.

---

# 💼 Practical Application

The concepts from this lab are directly useful in automation and DevOps.

For example, a Python automation script may collect:

```python
server_name = input("Server name: ")
port = int(input("Port: "))
enabled = True
```

Here:

```text
server_name → str
port        → int
enabled     → bool
```

These basic concepts later become important when working with:

* Linux automation
* AWS
* APIs
* Configuration files
* JSON
* Infrastructure automation
* Data analysis
* Monitoring scripts
* DevOps tools
* AI/ML applications

---

# 🧩 Concept Flow

```text
User Input
    │
    ▼
input()
    │
    ▼
String Data
    │
    ▼
Type Conversion
    │
    ├── int()
    ├── float()
    ├── str()
    └── bool()
    │
    ▼
Processing
    │
    ├── Arithmetic
    ├── String Operations
    └── Conditions
    │
    ▼
Output
```

---

# ✅ Lab Completion Checklist

* [ ] Verified Python installation.
* [ ] Created the Lab 01 directory.
* [ ] Created `variables_demo.py`.
* [ ] Practiced `int`.
* [ ] Practiced `float`.
* [ ] Practiced `str`.
* [ ] Practiced `bool`.
* [ ] Used `type()`.
* [ ] Practiced variable naming.
* [ ] Practiced multiple assignment.
* [ ] Used `input()`.
* [ ] Confirmed that `input()` returns strings.
* [ ] Practiced `int()` conversion.
* [ ] Practiced `float()` conversion.
* [ ] Practiced `str()` conversion.
* [ ] Practiced `bool()` conversion.
* [ ] Built an interactive calculator.
* [ ] Practiced arithmetic operators.
* [ ] Practiced string operations.
* [ ] Built a student grade calculator.
* [ ] Practiced `try/except`.
* [ ] Tested invalid input.
* [ ] Checked Python syntax.
* [ ] Created evidence files.
* [ ] Reviewed evidence for sensitive information.

---

# 🏁 Conclusion

Lab 01 established the foundation for Python programming by introducing **syntax, variables, data types, user input, type conversion, arithmetic operations, strings, Boolean values, and basic error handling**.

The most important concepts learned were:

```python
# Variables
name = "Abeera"

# Integer
age = 20

# Float
gpa = 3.75

# Boolean
is_active = True

# Check type
type(age)

# User input
name = input("Enter your name: ")

# Type conversion
age = int(input("Enter your age: "))
```

These concepts are fundamental to almost every Python program.

The lab also demonstrated how simple Python concepts can be combined to create a practical application such as a **student grade calculator**.

---

# 🚀 Next Steps

After completing this lab, the recommended progression is:

```text
Lab 01
Python Syntax & Data Types
        ↓
Variables & Input
        ↓
Type Conversion
        ↓
Lists & Tuples
        ↓
Dictionaries & Sets
        ↓
Conditional Statements
        ↓
Loops
        ↓
Functions
        ↓
File Handling
        ↓
Modules & Packages
        ↓
Data Science / Automation
```

---

## 📂 Final Lab Structure

```text
Lab-01-Python-Syntax-and-Data-Types/
│
├── README.md
│
├── variables_demo.py
├── variable_naming.py
├── user_input_demo.py
├── advanced_input.py
├── type_conversion.py
├── interactive_calculator.py
├── operations_demo.py
├── grade_calculator.py
├── error_examples.py
│
└── evidence/
    ├── python-version.txt
    ├── variables-output.txt
    ├── input-output.txt
    ├── conversion-output.txt
    ├── calculator-output.txt
    ├── grade-calculator-output.txt
    └── syntax-check.txt
```

---

**Lab:** 01 — Python Syntax and Data Types

**Status:** ✅ Completed

**Difficulty:** Beginner

**Primary Skills:** `Python 3` · Variables · `int` · `float` · `str` · `bool` · `type()` · `input()` · Type Conversion · Arithmetic · Strings · Error Handling
