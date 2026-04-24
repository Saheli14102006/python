list1=[]
n=int(input("enter the size"))
i=1
print("enter elements")
for i in range(n):
    ele=int(input())
    list1.append(ele)
print(list1)
odd=[]
even=[]
for i in range(0,n):
    if(list1[i]%2==0):
        even.append(list1[i])
    else:
        odd.append(list1[i])
print("Even",even)
print("Odd",odd)

