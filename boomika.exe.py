#in LCM multiply of number ehich is greater in input
#LCM canot be smaller the the greater value in input ( smaller or equal to)
#higher value is multiples only itself(n1 or n2 is higher value==0)

def compute_LCM(n1,n2):
    if n1>n2:
        higher=n1
        
    else:
        higher=n2
    value = higher
    
    while True: 
        if higher%n1==0 and higher%n2==0:
           print("LCM of",n1,"and",n2,"is",higher)
           break
        
        else:
           higher+=value

n1=int(input("enter your first number: "))
n2=int(input("enter your second number: "))

compute_LCM(n1,n2)
