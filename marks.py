# Student Marks Matrix Analysis

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    row = []
    print("Enter marks for Student", i + 1)
    for j in range(subjects):
        row.append(float(input("Subject " + str(j + 1) + ": ")))
    marks.append(row)

# Row-wise statistics
averages = []

print("\nStudent Averages:")
for i in range(students):
    avg = sum(marks[i]) / subjects
    averages.append(avg)
    print("Student", i + 1, "Average:", round(avg, 2))

# Top performer
top = averages.index(max(averages))
print("\nTop Performer: Student", top + 1)
print("Highest Average:", round(averages[top], 2))

# Column-wise statistics
print("\nSubject Averages:")
for j in range(subjects):
    total = sum(marks[i][j] for i in range(students))
    avg = total / students
    print("Subject", j + 1, "Average:", round(avg, 2))

    if avg < 40:
        print("Warning: Low performance in Subject", j + 1)
