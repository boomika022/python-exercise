#singel inheritance
class Nokia:
    company="Nokia"
    website="nokiacompany@gmail.com"

    def productdetail(self):
        print("vadapalani,chennai,637358")

class Nokia1000(Nokia):
    def __init__(self):
        self.name="Nokia1000"
        self.year=1998
    
    def printall(self):
        print("name:",self.name)
        print("year:",self.year)
        print("company:",self.company)
        print("website:",self.website)
       
mobile=Nokia1000()
mobile.printall()
mobile.productdetail()


      