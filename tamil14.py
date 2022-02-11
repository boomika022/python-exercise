#static method function in python

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printdetail(self):
        print("name:",self.name,"age:",self.age)

    @staticmethod
    def welcome():
        print("welcome to our institution!")

a=student("boomika",19)
a.printdetail()
a.welcome()
a2=student("boomi",20)
a2.printdetail()
a.welcome()

