# Lab 1: Grade Calculator
# This script calculates a student's weighted final score
# using quiz, midterm, final exam, and project scores.

print("=== Student Grade Calculator ===")
print()

# Student information
student_name = input("Student name: ")
student_id = input("Student ID: ")
course_name = input("Course name: ")

print()
print("Enter assessment scores from 0 to 100.")
print()

# Assessment scores
quiz_1 = float(input("Quiz 1: "))
quiz_2 = float(input("Quiz 2: "))
midterm = float(input("Midterm: "))
final_exam = float(input("Final: "))
project = float(input("Project: "))

# Weights
quiz_1_weight = 0.10
quiz_2_weight = 0.10
midterm_weight = 0.20
final_weight = 0.40
project_weight = 0.20

# Calculate weighted score
weighted_score = (
    quiz_1 * quiz_1_weight
    + quiz_2 * quiz_2_weight
    + midterm * midterm_weight
    + final_exam * final_weight
    + project * project_weight
)

# Determine letter grade
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

# Determine passing status
passing_status = weighted_score >= 60

print()
print("=== Grade Report ===")
print("Student Name:", student_name)
print("Student ID:", student_id)
print("Course:", course_name)
print()

print("Quiz 1:", quiz_1)
print("Quiz 2:", quiz_2)
print("Midterm:", midterm)
print("Final:", final_exam)
print("Project:", project)
print()

print(f"Weighted Final Score: {weighted_score:.2f}")
print("Letter Grade:", letter_grade)
print("Passing Status:", passing_status)
print()

print("=== End of Grade Report ===")
