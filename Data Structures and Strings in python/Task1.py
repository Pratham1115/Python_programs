# Dictionary to store student names and their marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Eve": 95
}

# Ask user for a student's name
student_name = input("Enter a student's name: ")

# Retrieve and display marks or show appropriate message
if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")
else:
    print(f"Sorry, {student_name} is not found in the records.")