import numpy
import pandas as pd
import matplotlib.pyplot as plt

students = pd.DataFrame({
    "Name": ["Vidya", "Sachin", "Priyanshu", "Vikash Singh"],
    "Physics": [45, 89, 56, 69],
    "Chemistry": [82, 45, 61, 95],
    "Maths": [85, 87, 90, 70],
})
# you have to plot a dashboard of 2*2
# create a graph to display the total marks of each student
total_marks = students[["Physics", "Chemistry", "Maths"]].sum(axis=1)
plt.subplot(2, 2, 1)
plt.bar(students["Name"], total_marks, color='skyblue')
plt.title("Total Marks of Each Student")
plt.xlabel("Students")
plt.ylabel("Total Marks")

# create a line graph showing the comparison of students marks get by students in each subject
plt.subplot(2, 2, 2)
for _, student in students.iterrows():
    plt.plot(["Physics", "Chemistry", "Maths"], student[["Physics",
             "Chemistry", "Maths"]], marker="o", label=student["Name"])
plt.ylabel("Scores")
plt.title("Student Performance")
plt.xlabel("Subjects")
# create a bar graph showing the maximum and minimum marks obtained by students in each subject
plt.subplot(2, 2, 3)
subjects = ["Physics", "Chemistry", "Maths"]
max_marks = students[subjects].max()
min_marks = students[subjects].min()
x = range(len(subjects))
plt.bar([i - 0.2 for i in x], max_marks,
        width=0.4, label="Maximum", color='red')
plt.bar([i + 0.2 for i in x], min_marks,
        width=0.4, label="Minimum", color='green')
plt.ylabel("Marks")
plt.title("Maximum and Minimum Marks")
plt.xticks(x, subjects)
# create a line graph showing caomparison of students marks va as average marks of each subject
average_marks = students[subjects].mean()
plt.subplot(2, 2, 4)
plt.plot(subjects, average_marks, marker="o", color="blue")
plt.ylabel("Average Marks")
plt.title("Average Marks per Subject")
plt.show()
