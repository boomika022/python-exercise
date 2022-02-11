num = int(input("enter an odd length number: "))
for i in range(num):
    for j in range(num):
        if( i==j or i+j==num-1):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
           
            
