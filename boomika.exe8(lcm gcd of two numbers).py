def compute_gcd(a,b):
    if b==0:
        return a
    else:
        return compute_gcd( b, a%b)
    
n1=int(input("enter your first number: "))
n2=int(input("enter your second number: "))
LCM=(n1*n2)//compute_gcd(n1,n2)
print(LCM)
