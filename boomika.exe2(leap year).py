import calendar
year=int(input("enter the year: "))
if calendar.isleap(year):
   print("the year is leap year")
else:
    print("the year is not a leap year")
