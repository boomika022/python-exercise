number=0
n = int(input("enter your number: "))
for i in range ( 1,n+1):
    if n%i==0 :
        number+=1
if number==2:
   print(n,"it is a prime number")
else:
   print(n,"it is not a prime number")
