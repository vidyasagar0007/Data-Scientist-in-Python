import numpy as np
import pandas as pd

# Given dataset
marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

subjects = ["Python", "SQL", "Machine Learning"]

# 1. Total marks obtained by each student
total = np.sum(marks, axis=1)
print("1. Total marks:", total)

# 2. Average marks of each student
average = np.mean(marks, axis=1)
print("2. Average marks:", average)

# 3. Average marks in each subject
subject_average = np.mean(marks, axis=0)
print("3. Subject average:", subject_average)

# 4. Highest score in each subject
highest = np.max(marks, axis=0)
print("4. Highest score:", highest)

# 5. Lowest score in each subject
lowest = np.min(marks, axis=0)
print("5. Lowest score:", lowest)

# 6. Students whose average marks are above 80
above_80 = np.where(average > 80)[0]
print("6. Students with average above 80:", above_80)

# 7. Pass or Fail status using np.where()
# Assuming average >= 40 means Pass
status = np.where(average >= 40, "Pass", "Fail")
print("7. Pass/Fail status:", status)

# 8. Index of highest-performing student
highest_student_index = np.argmax(average)
print("8. Highest-performing student index:", highest_student_index)

# 9. Standard deviation for each subject
std = np.std(marks, axis=0)
print("9. Standard deviation:", std)

# 10. Convert final results into Pandas DataFrame
df = pd.DataFrame(marks, columns=subjects)

df["Total"] = total
df["Average"] = average
df["Status"] = status

print("\n10. Final DataFrame:")
print(df)