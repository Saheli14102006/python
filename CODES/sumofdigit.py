a=int(input("enter"))
s=0
while a>0:
    r=int(a%10)
    a=int(a/10)
    s=s+r
print("sum",s)
