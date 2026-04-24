a=int(input("enter"))
s=0
n=a
while a>0:
    r=int(a%10)
    a=int(a/10)
    m=r*r*r
    s=s+m
if s==n:
    print("ARMSTRONG",n)
else:
    print("NOT ARMSTRONG",n)

