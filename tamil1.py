'''def welcome ():
    print(" hi there!")

welcome()    
 
#9 types of def functions in python

# 1.no return type wihout argument function

def add():
    a=int(input("enter your value of a: "))
    b=int(input("enter your value of b: "))
    c= a+b
    print("total: ",c)

add()    

#2. no return type with argument function

def sub():
     a=int(input("enter your value of a: "))
     b=int(input("enter your value of b: "))
     c= a-b
     print("difference: ",c)

sub()

#3.return type without argument function

def mul():
     a=int(input("enter your value of a: "))
     b=int(input("enter your value of b: "))
     c= a * b
     return c

x=mul()
print("mul",x)

#4.return type with argument function in python

def div():
     a=int(input("enter your value of a: "))
     b=int(input("enter your value of b: "))
     c= a/b
     return c

x=div()
print("division",x)

#5.arbitary arguments function in python

def class_10(* students):
    print(students)
    for user in students:
        print(user)

class_10("supraja","boomi","sudharsan")

#6. keyword arguments function in python function

def message(name,age):
    print(name,"age is ",age)

message( name= "supraja",age=18)

#7.arbitary keyword arguments in python function

def biodata(**data):
    print(data)

biodata(name="supraja",age=18, gender= "female")

#8.default parameter function in python

def user(name,city="vaniyambadi"):
    print(name,"is from",city)

user(name="supraja",city="chennai")
user(name="boomika")

#9.passing a list as an argument in python function

def total(marks):
    return sum (marks)

print("total is ",total([55,75,95,45]))

#10.recursive function

def factorial(x):
    if x==1:
        return 1
    else:
        return(x * factorial(x-1))

print( "factroial :",factorial(5))

#factorial(5):
  5 * factorial(4)
  5*4*factorial(3)
  5*4*3*factorial(2)
  5*4*3*2*factorial(1)
  5*4*3*2*1
  =120

 
#11.lambda function in python

c=lambda a : a+50
print(c(a=50))

c=lambda a,b : a /b
print(c(a=12,b=6))'''


















