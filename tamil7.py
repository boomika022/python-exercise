#instance attributes type in python function
class user():
    course="java"

x=user()
print(user.__dict__)
print(user.course) #print class attributes
print(x.__dict__)
print(x.course)
x.course="c++"
print(x.__dict__)
print(x.course)

x2=user()
print(x2.course)









































