#multiple level inheritance 
class grandfather:
    def ownhouse(self):
        print("own house ,only once in the lifetime own house is builed :) !")

class father(grandfather):
    def ownbike(self):
        print("own bike has a seprate respect !")

class son(father):
    def ownbook(self):
        print("book is more important to gain knowledge !")

o=son()
o.ownbook()
o.ownbike()
o.ownhouse()

