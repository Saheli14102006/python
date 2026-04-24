list1=[]
n=int(input("enter the size"))
print("enter the numbers")
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print(list1)
if(list1[0]==list1[n-1]):
    print("1st and Last are same")
list2=[]
n=int(input("enter the size"))
print("enter the numbers")
for i in range(0,n):
    ele=int(input())
    list2.append(ele)
print(list2)
if(list2[::n]==list2[::-n]):
    print("1st and Last are same")
