# Lab 1: User Input Demonstration
# This script demonstrates how input() collects
# information from the user.
#
# Important:
# input() always returns the entered value as a string.

print("=== User Input Collection ===")
print()

# Collecting string input
print("Let's collect some information about you!")

user_name = input("Please enter your name: ")

print("Hello,", user_name + "!")
print("Type of user_name:", type(user_name))
print()

# Collecting numeric input
# The value is still a string because input() returns strings.
user_age_str = input("Please enter your age: ")

print("You entered:", user_age_str)
print("Type of user_age_str:", type(user_age_str))
print()

# Another example of input returning a string
favorite_number_str = input("Enter your favorite number: ")

print("Your favorite number is:", favorite_number_str)
print("Type:", type(favorite_number_str))
print()

print("Notice: All input() results are strings!")
