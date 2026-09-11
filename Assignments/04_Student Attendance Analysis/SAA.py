import numpy as np
import pandas as pd

# ============================================================
# PROJECT 4: STUDENT ATTENDANCE ANALYSIS
# ============================================================

# Given Dataset
attendance = np.array([
    [90, 85, 95, 88],
    [75, 80, 70, 78],
    [95, 92, 98, 96],
    [65, 70, 72, 68],
    [85, 88, 90, 87]
])

# Student names and subjects
students = [
    "Student 1",
    "Student 2",
    "Student 3",
    "Student 4",
    "Student 5"
]

subjects = ["Python", "Java", "SQL", "ML"]


# ============================================================
# 1. AVERAGE ATTENDANCE OF EACH STUDENT
# ============================================================

student_average = np.mean(attendance, axis=1)

print("\n1. Average Attendance of Each Student:")
for i in range(len(students)):
    print(f"{students[i]}: {student_average[i]:.2f}%")


# ============================================================
# 2. AVERAGE ATTENDANCE OF EACH SUBJECT
# ============================================================

subject_average = np.mean(attendance, axis=0)

print("\n2. Average Attendance of Each Subject:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {subject_average[i]:.2f}%")


# ============================================================
# 3. HIGHEST ATTENDANCE IN EACH SUBJECT
# ============================================================

highest_attendance = np.max(attendance, axis=0)

print("\n3. Highest Attendance in Each Subject:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {highest_attendance[i]}%")


# ============================================================
# 4. LOWEST ATTENDANCE IN EACH SUBJECT
# ============================================================

lowest_attendance = np.min(attendance, axis=0)

print("\n4. Lowest Attendance in Each Subject:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {lowest_attendance[i]}%")


# ============================================================
# 5. STUDENTS HAVING AVERAGE ATTENDANCE ABOVE 80%
# ============================================================

print("\n5. Students Having Average Attendance Above 80%:")

for i in range(len(student_average)):
    if student_average[i] > 80:
        print(f"{students[i]}: {student_average[i]:.2f}%")


# ============================================================
# 6. STUDENT WITH HIGHEST AVERAGE ATTENDANCE
# ============================================================

highest_student_index = np.argmax(student_average)

print("\n6. Student With Highest Average Attendance:")
print(
    f"{students[highest_student_index]}: "
    f"{student_average[highest_student_index]:.2f}%"
)


# ============================================================
# 7. STANDARD DEVIATION OF ATTENDANCE
# ============================================================

standard_deviation = np.std(attendance)

print("\n7. Standard Deviation of Attendance:")
print(f"{standard_deviation:.2f}")


# ============================================================
# 8. CLASSIFY STUDENTS USING np.where()
#    Attendance >= 75% = Eligible
#    Attendance < 75%  = Not Eligible
# ============================================================

status = np.where(
    student_average >= 75,
    "Eligible",
    "Not Eligible"
)

print("\n8. Student Eligibility Status:")

for i in range(len(students)):
    print(f"{students[i]}: {status[i]}")


# ============================================================
# 9. CONVERT DATA INTO PANDAS DATAFRAME
# ============================================================

df = pd.DataFrame(
    attendance,
    columns=subjects,
    index=students
)


# ============================================================
# 10. ADD AVERAGE AND STATUS COLUMNS
# ============================================================

df["Average"] = df.mean(axis=1)

df["Status"] = np.where(
    df["Average"] >= 75,
    "Eligible",
    "Not Eligible"
)


# ============================================================
# FINAL DATAFRAME
# ============================================================

print("\n10. Final Student Attendance DataFrame:")
print(df)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("             STUDENT ATTENDANCE ANALYSIS")
print("=" * 60)

print(f"Total Students : {len(students)}")
print(f"Total Subjects : {len(subjects)}")

print(
    f"Highest Average: "
    f"{students[highest_student_index]} "
    f"({student_average[highest_student_index]:.2f}%)"
)

print(f"Overall Standard Deviation: {standard_deviation:.2f}")

print("\nEligible Students:")
for i in range(len(students)):
    if status[i] == "Eligible":
        print(f"  {students[i]}")

print("\nNot Eligible Students:")
for i in range(len(students)):
    if status[i] == "Not Eligible":
        print(f"  {students[i]}")

print("=" * 60)