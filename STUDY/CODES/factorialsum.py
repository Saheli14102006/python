x=int(input("enter the value of x"))
n=int(input("enter the value of n"))
sum=0.0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum=sum+x/fact
print("sum",sum)
    
