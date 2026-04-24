def krishnamurty(n):
    sum=0
    m=n
    while(n>0):
        r=int(n%10)
        n=int(n/10)
        fact=1
        for i in range(1,r+1):
             fact=fact*i
            
        sum=sum+fact
    if(m==sum):
       print("Krishnamurty",m)
    else:
       print("Not Krishnamurty",m)
    print(sum)
   
x=int(input("enter"))
krishnamurty(x)
