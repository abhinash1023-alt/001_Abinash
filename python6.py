# Program: Student Grades using User Input

# Step 1: Create an empty dictionary to store student names and marks
students_marks = {}

# Step 2: Ask how many students you want to enter
n = int(input("Enter number of students: "))

# Step 3: Take input for each student
for i in range(n):
    name = input(f"\nEnter student {i+1} name: ")
    marks = int(input(f"Enter marks of {name}: "))
    students_marks[name] = marks

# Step 4: Calculate grade based on marks
print("\n--- Student Grades ---")
for student, marks in students_marks.items():
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B+'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    else:
        grade = 'F'

    print(f"{student} scored {marks} and got grade {grade}.")
