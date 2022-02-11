#class method decorator function in python
class student:
    #wants to find total students (tasks)
    count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1

    def printdetail(self):
        print("name:",self.name,"age:",self.age)

    @classmethod
    def total(cls):
        return cls.count


a=student("boomika",20)
a.printdetail()
b=student("boomi",19)
b.printdetail()

print("total admission:", student.total())
print("totaladmission:",a.total())









