import matplotlib.pyplot as plt
x = ["Vidya", 'Sachin', 'Priyanshu', 'Shivam', 'Divya']
y = [400, 500, 700, 600, 800]
# plt.title("Student Scores")
plt.subplot(2, 2, 1)
plt.bar(x, y, color="blue", width=0.8)
plt.subplot(2, 2, 2)
plt.bar(x, y, color="red", width=0.8)
plt.subplot(2, 2, 3)
plt.bar(x, y, color="green", width=0.8)
plt.subplot(2, 2, 4)
plt.bar(x, y, color="orange", width=0.8)
plt.savefig("student_score_bar.png")
plt.show()
