#property decorator in python
class user():
     def __init__(self,name,age) :
         self.name=name
         self.age=age
         #self.msg=self.name +"is "+self.age+"your current age"

     @ property
     def msg(self):
         return self.name +" is "+str(self.age)+" old age !"


a=user("boonmika",25)
print(a.name)
print(a.age)
print(a.msg)
a.age=20
print(a.msg)
         
