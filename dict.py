dict = {1: "Vidya", 2: "Shivam", 3: "Rohit", 4: "Priyanshu",
        1: "Vidyasagar", 5: "Vidya", 6: "Shivam"}
dict1 = {"name": "Vidya", "rollno": 45, "city": "lucknow"}
print(dict1["city"])
print(dict1["name"])
print(dict1["rollno"])
print(dict[1])
print(dict[2])
print(dict[3])
print(dict[4])
print(dict)
dict1.pop("name")

# non parameterized


def methodName():
    print("This is my Method")
methodName()

# parameterized method


def myName(name):
    print(name)
myName("Viyda")

# 1- create a method to check no is even or odd


def evwn_Odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("Odd")
evwn_Odd(52)

# 2- create a function to check no is prime or not

# def prime_no(number):
#     if number % 2
