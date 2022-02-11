#handling diamond function problem in python (dimension problem)
#run the program with the pass and check

class a:
    def display(self):
        print("this is the display of a --> class")

class b(a):
    def display(self):
        print("this is the display of b --> class ")

class c (a):
    def display(self):
        print("this is the display of c --> class")

class d (b,c):
    def display(self):
        print("this is the display of d --> class")

o=d()
o.display()