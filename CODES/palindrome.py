a=int(input("enter"))
m=0
n=a
while a>0:
    r=int(a%10)
    a=int(a/10)
    m=m*10+r
if m==n:
    print("PALINDROME",n)
else:
    print("NOT PALINDROME",n)

