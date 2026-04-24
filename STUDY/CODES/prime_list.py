list1=[]
n=int(input("enter the size"))
i=1
print("enter elements")
for i in range(n):
    ele=int(input())
    list1.append(ele)
print(list1)
for i in range(0,n):
    c=0
    for j in range(1,list1[i]):
        if(list1[i]%j==0):
            c=c+1
    if(c<=2):
        print("prime",list1[i])
