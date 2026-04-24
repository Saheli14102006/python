w=input("Enter a string")
n=w.split()
print(n)
q=int(len(n))
print(q)
for i in range(q):
  m=n[i]
#p=n[-1]
  x=m[0].upper()
  y=m[-1].upper()
  #print(x)
  #print(y)
  r=''.join([x+m[1:-1]+y])
  print(r)
