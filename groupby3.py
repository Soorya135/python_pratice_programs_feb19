from itertools import groupby

# Sample list of tuples (student, grade)
students_grades = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'B'), ('Eva', 'A')]

# Sort the list based on the grade (key function)
sorted_students_grades = sorted(students_grades, key=lambda x: x[1])

# Use itertools.groupby to group students based on their grades
grouped_students = {key: list(group) for key, group in groupby(sorted_students_grades, key=lambda x: x[1])}

# Display the grouped students
for key, group in grouped_students.items():
    print(f"Students with grade {key}: {group}")
