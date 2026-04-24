test=dict()
print("enter the items")
for _ in range(4):
    k=input()
    v=input()
    test[k]=v
temp=[]
res=dict()
c=0
for key,val in test.items():
    
    if val not in temp:
        temp.append(val)
        c=c+1

print("duplicates ", 4-c,temp)


    
