n=int(input("enter"))
p=n
q=n
c=0
sum=0
while q>0:
    r1=int(q%10)
    q=int(q/10)
    c=c+1
while n>0:
    r=int (n%10)
    n=int (n/10)
    m=pow(r,c)
    sum=sum+m
if sum==p:
    print("armstrong",p)
else:
    print("not armstrong",p)
