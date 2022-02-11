#operator overloading method in python
#so many math operations can be used 

class addition:
    def __init__(self,a):
        self.a=a
    def __add__(a1,a2):
        return a1.a + a2.a
    def __sub__(a1,a2):
        return a1.a - a2.a


a1=addition(10)
a2=addition(20)

print("total addition  :",(a1 + a2))
print("total difference:",(a1 - a2))
