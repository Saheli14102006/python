w=input("enter a string")
n=w.split()
s=input("enter a searching string")
p=len(n)
f=0
for i in range(p):
   if s==n[i]:
      f=1
      break
if f==1:
    print("found")
else:
    print("not found")
