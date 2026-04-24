list1=[]
n=int(input("enter the size"))
i=1
print("enter elements")
for i in range(n):
    ele=int(input())
    list1.append(ele)
print(list1)
s=int(input("enter the search elements"))
low=0
up=n-1
flag=0
while(low<=up):
    mid=int((low+up)/2)
    if(list1[mid]>s):
        up=mid-1
    elif(list1[mid]==s):
        flag=1
        break
    else:
        low=mid+1
if(flag==1):
    print("item found=%d at loc %d",list1[mid],mid)
else:
    print("not found")
