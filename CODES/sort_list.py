list1=[]
n=int(input("enter the size"))
i=0
print("enter the number")
for i in range(n):
    ele=int(input())
    list1.append(ele)
print(list1)
for i in range(0,n):
    for j in range(0,(n-i-1)):
        if(list1[j]>list1[j+1]):
             list1[j],list1[j+1]=list1[j+1],list1[j]
print("sorted list")
print(list1)

