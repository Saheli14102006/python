list=[]
n=int(input("Enter:"))
for i in range(n):
    ele=int(input("Element:"))
    list.append(ele)
print("The list is:",list)
for i in range(n):
    for j in range(i+1,n):
        if list[i]<list[j]:
            print(list[i])
        elif list[i]>list[j+1]:
            list.remove(list[i])
            # list[i]=list[j]
            continue
        elif list[i]>list[j]:
            print(list[i])
        elif list[i]<list[j+1]:
            list.remove(list[i])
            # list[i]=list[j]
            continue
        else:
            print("Nil")
        
print("final list",list)