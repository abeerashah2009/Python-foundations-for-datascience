# Lab 1: Error Handling Examples
# This script demonstrates successful numeric conversion
# and handling invalid input with ValueError.

print("=== Error Handling Demonstration ===")
print()

# Example 1: Successful integer conversion
print("Example 1: Successful Integer Conversion")

integer_input = input("Enter an integer: ")

try:
    integer_value = int(integer_input)
    print("Conversion successful!")
    print("Value:", integer_value)
    print("Type:", type(integer_value))
except ValueError:
    print("Error: The entered value is not a valid integer.")

print()

# Example 2: Successful float conversion
print("Example 2: Float Conversion")

float_input = input("Enter a decimal number: ")

try:
    float_value = float(float_input)
    print("Conversion successful!")
    print("Value:", float_value)
    print("Type:", type(float_value))
except ValueError:
    print("Error: The entered value is not a valid number.")

print()

# Example 3: General error-handling explanation
print("Example 3: ValueError Handling")
print("ValueError occurs when a value has the correct general")
print("type but cannot be converted into the requested format.")

print()
print("=== End of Error Handling Demo ===")
