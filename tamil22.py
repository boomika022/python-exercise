from abc import ABC, abstractmethod

class bank(ABC):
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def credit(self):
        pass
    @abstractmethod
    def debit(self):
        pass

class HDFC(bank):
 
    def loan(self):
        print("HDFC provides 7.5%")
    
    def credit(self):
        print("HDFC provides credit")
    
    def debit(self):
        print("HDFC provides debit")

    def card(self):
        print("HDFC provides the required cards")

o=HDFC()

o.loan()
o.credit()
o.debit()
o.card()









