# Lab 1: Arithmetic Operations Demonstration
# This script demonstrates Python arithmetic operators:
# addition, subtraction, multiplication, division,
# floor division, modulus, and exponentiation.

print("=== Arithmetic Operations Demonstration ===")
print()

# Input values
number_a = 17
number_b = 5

print("Number A:", number_a)
print("Number B:", number_b)
print()

# Basic arithmetic operations
addition = number_a + number_b
subtraction = number_a - number_b
multiplication = number_a * number_b
division = number_a / number_b
floor_division = number_a // number_b
remainder = number_a % number_b
exponentiation = number_a ** number_b

print("Arithmetic Results:")
print("Addition (+):", addition)
print("Subtraction (-):", subtraction)
print("Multiplication (*):", multiplication)
print("Division (/):", division)
print("Floor Division (//):", floor_division)
print("Modulus (%):", remainder)
print("Exponentiation (**):", exponentiation)
print()

# Demonstrate operator precedence
result = number_a + number_b * 2

print("Operator Precedence:")
print("17 + 5 * 2 =", result)
print("Multiplication is performed before addition.")
print()

print("=== End of Arithmetic Operations Demo ===")
