#property function in python 
class student():
    def __init__(self,total):
        self._total =total

    def average(self):
        return self._total/5.0

    def getter(self):
        return self._total

    def setter(self , t):
        if  t > 0 or t<500:
            print("invalid total and can't change")
        else:
            self._total=t

    total= property(getter,setter)

a=student(450)
print("Total :",a.total)
print("average:",a.average())
a.total=500
print("Total :",a.total)
print("average:",a.average())