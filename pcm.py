import pandas as pd
import matplotlib.pyplot as plt


students = pd.DataFrame({
    "Name": ["Vidya", "Sachin", "Priyanshu", "Vikash Singh"],
    "Physics": [45, 89, 56, 99],
    "Chemistry": [82, 39, 61, 95],
    "Maths": [85, 87, 50, 98],
})

subjects = ["Physics", "Chemistry", "Maths"]
students["Total"] = students[subjects].sum(axis=1)
students["Average"] = students[subjects].mean(axis=1)
students["Percentage"] = students["Total"] / (len(subjects) * 100) * 100

print(students[["Name", "Total", "Average", "Percentage"]])

plt.figure(figsize=(9, 5))
for _, student in students.iterrows():
    plt.plot(subjects, student[subjects], marker="o", label=student["Name"])
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Performance by Subject")
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(students["Name"], students["Percentage"], color="steelblue")
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.title("Student Percentage")
plt.ylim(0, 100)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("pcm_percentage.png")
plt.show()
