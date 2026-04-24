a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
r=int(b%a)
n=a*b;
while(r!=0):
    r=int(b%a)
    b=a;
    a=r;
print("GCD",b)
LCM=int(n/b)
print("LCM",LCM)
