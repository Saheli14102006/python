def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count<=2):
        print("Prime",n)
    else:
        print("Not Prime",n)
    
x=int(input("enter"))
prime(x)
