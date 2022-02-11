#date time in python
import datetime as dt

current_date=dt.date.today()
print(current_date)

new=dt.date(2021,10,25)
print(new)
print("year:",new.year)
print("month:",new.month)
print("day:",new.day)
print("------------------------------------")
b=dt.time(10,45,5,555505)
print(b)
print("hour;",b.hour)
print("min;",b.minute)
print("second;",b.second)
print("microsecond;",b.microsecond)
print("------------------------------------")
current_time=dt.datetime.now()
print("current time:",current_time)
print("------------------------------------")
new=dt.datetime(2022,2,6,6,10,2)
print(new)
print(new.date())
print(new.time())
print("------------------------------------")
current=dt.datetime.now()
newyear=dt.datetime(2023,1,1)
difference=newyear-current
print(difference)
print("------------------------------------")
current=dt.datetime.now()
print(current)
a=current.strftime("%A %B %D %Y")
print(a)




