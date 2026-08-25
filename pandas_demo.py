import pandas as pd
data=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(data)
student=pd.Series({
    "Name":["Vidya","Sachin","Priyanshu"],
    "City":["Lucknow","Kanpur","Goa"],
    "Mark":[78,89,56]
})
print(student)
print(student['Name'][1])
print(student['City'][2])
print(student['Mark'])
# for i in range(0,3):
#     print(student["city"][i])