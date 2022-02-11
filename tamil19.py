#  function overriding in python
#super function is created and used
class emplooye:
    def workhrs(self):
        self.workhrs=50

    def total_hrs(self):
        print("total hours of the person: ",self.workhrs)

class traineer(emplooye):
    def workhrs(self):
        self.workhrs=70

    def total_hrs(self):
        print("total hours of the person: ",self.workhrs)

    def reset_hrs(self):
        super().workhrs()

e=emplooye()
e.workhrs()
e.total_hrs()

t=traineer()
t.workhrs()
t.total_hrs()

#reset working hours
t.reset_hrs()
t.total_hrs()




