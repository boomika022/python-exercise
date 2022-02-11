#GCD=greatest common divisor OR HCF=highest common factor
#example:64,48
#64=48*x+remainder
#64=48*1+16
#48=16*3+0
#16=0
#gcd=16

def compute_GCD(a,b):
    if b == 0:
        return a
    else:
        return compute_GCD(b,a%b)
num1=int(input("enter your number1:"))
num2=int(input("enter your number2:"))
print(compute_GCD(num1,num2))
