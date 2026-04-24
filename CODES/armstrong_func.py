def armstrong(n):
    p=n
    q=n
    c=0
    sum=0
    while q>0:
        r1=int(q%10)
        q=int(q/10)
        c=c+1
    while n>0:
        r=int(n%10)
        n=int(n/10)
        m=pow(r,c)
        sum=sum+m
    if sum==p:
        print("Armstrong",p)
    else:
        print("Not Armstrong",p)

x=int(input("enter"))
armstrong(x)
