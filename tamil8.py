#class method in python function
class student:
    name="boomika"
    age =19
    def printall():
        print("name:",student.name)
        print("age:",student.age)

student.printall()
print(student.__dict__)

print(getattr(student,"printall"))
getattr(student,"printall")()

student.__dict__["printall"]()


