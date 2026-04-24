n=int(input("Enter the range"))
i=0
l=[]
for i in range(n):
    ele=input("Enter")
    l.append(ele)
print(l)
loc=int(input())
l.pop(loc)
print(l)