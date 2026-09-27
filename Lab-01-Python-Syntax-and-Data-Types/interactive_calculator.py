# Lab 1: Interactive Calculator
# This script collects two numbers from the user,
# converts the input strings to floats, and performs
# basic arithmetic operations.

print("=== Simple Calculator ===")
print()

print("Let's perform some basic calculations!")

# Get user input
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert input strings to floating-point numbers
num1 = float(num1_str)
num2 = float(num2_str)

print()
print("Input Analysis:")
print("First input:", num1_str, "| Type:", type(num1_str))
print("After conversion:", num1, "| Type:", type(num1))
print("Second input:", num2_str, "| Type:", type(num2_str))
print("After conversion:", num2, "| Type:", type(num2))
print()

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Calculation Results:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print()

# Convert results to different types
print("Type Conversion of Results:")
print("Addition as integer:", int(addition))
print("Addition as string:", str(addition))
