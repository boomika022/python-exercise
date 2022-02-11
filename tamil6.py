#class attributes in python

class student():
    name="supraja"
    age=18

#getattr method
print(getattr(student,"name"))
print(getattr(student,"age"))
print(getattr(student,"gender","no such attributes found"))

#dot notation
print(student.name)
print(student.age)

#setattr
setattr(student,"name","boomika")
print(student.name)

setattr(student,"gender","female")
print(student.gender)

student.city="chennai"
print(student.city)

print(student.__dict__)

delattr (student,"city")
print(student.__dict__)

del student.gender
print(student.__dict__)
