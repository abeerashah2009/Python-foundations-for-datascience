# Lab 1: Advanced Input Handling
# This script demonstrates collecting multiple
# pieces of information from a user.

print("=== Advanced Input Handling ===")
print()

# Student registration information
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

# Course information
course_selection = input("Select your course (CS/IT/ENG): ")
semester = input("Enter semester (Fall/Spring/Summer): ")

print()
print("Course Information:")
print("Selected Course:", course_selection)
print("Semester:", semester)
print()

# Boolean-like input
# Note: input() returns a string, not a Boolean.
is_full_time = input("Are you a full-time student? (yes/no): ")

print("Full-time status:", is_full_time)
print("Type:", type(is_full_time))
