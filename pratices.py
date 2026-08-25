import pandas as pd
# data=pd.Series([1,2,3,4,5,6,7,8,9,10])
# print(data)
student=pd.DataFrame({
    "Name":["Vidya","Sachin","Priyanshu","Vikash Singh"],
    "City":["Lucknow","Kanpur","Goa","Thailand"],
    "Mark":[78,89,56,99]
})
print(student)
# print(student['Name'].iloc[1])
# def get_stu(student):
#     if student["Mark"].max() >= 90:
#         print(student[student["Mark"] >= 90])

# get_stu(student)

# # Create a function to print the students who belong to Lucknow

# def get_lucknow_students(student):
#     print(student[student["City"] == "Lucknow"]["Name"])
# get_lucknow_students(student)

# def get_avg_stu_mark(student):
#     print(student["Mark"].sum()/3)
# get_avg_stu_mark(student)

df=pd.DataFrame(student)

df.to_csv('Data_Scientists_data.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
        
    