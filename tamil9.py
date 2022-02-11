#init method in python
class user():
      def __init__(self,name):
          print("call when new init has created")
          self.name=name
      def printall(self):
          print("name: ",self.name)

a1=user("boomika")
a1.printall()
print(a1.__dict__)
a2=user("boomi")
a2.printall()
print(a2.__dict__)
print(user.__dict__)



          