list1=["abc",1,"def",2,3.5]
print(list1)
a=len(list1)
print("length",a)
print(list1[2:4])
print(list1[:4])
print(list1[1:])
list2=[]
n=int(input("enter the size"))
i=1
print("enter the number")
for i in range(n):
    ele=int(input())
    list2.append(ele)
print(list2)
list2.append("hi")
print(list2)
