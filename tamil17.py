#multiple inheritance

class father:
    def fishing(self):
        print("the work of father is earning money by fishing")

    def chess(self):
        print("playing chess with father after his work completed")

class mother:
    def cooking(self):
        print("the work of mother is cooking the delicious foods")

    def chess(self):
        print("playing chess with mother after her work completed")

class son(father,mother):
    def homework(self):
        print("the work of son is completeing homework")

o=son()
o.homework()
o.fishing()
o.cooking()
o.chess()
























