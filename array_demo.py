import numpy as np
mark=np.array([
    [85,80,90],
    [75,85,80],
    [92,88,95],
    [60,72,68],
    [78,82,80]
])
print(mark)
#(1)total marks of each student
total_marks=np.sum(mark,axis=1)
print("Total marks of each student:", total_marks)
#(2)average marks of each student
average_marks=np.mean(mark,axis=1)
print("Average marks of each student:", average_marks)
#(2)average marks of each subject
average_subject_marks=np.mean(mark,axis=0)
print("Average marks of each subject:", average_subject_marks)

#highest score of each subject
highest_score_of_each_subject=np.all(mark,axis=1)
print("Highest_score_of_each_subject :",highest_score_of_each_subject)
