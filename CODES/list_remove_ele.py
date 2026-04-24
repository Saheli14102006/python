n=int(input("Enter the range"))
i=0
l=[]
for i in range(n):
    ele=input("Enter")
    l.append(ele)
print(l)
loc=(input())
l.remove(loc)
print(l)