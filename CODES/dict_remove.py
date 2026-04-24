test=dict()
print("enter the items")
for _ in range(4):
    k=input()
    v=input()
    test[k]=v
temp=[]
res=dict()
for key,val in test.items():
    if val not in temp:
        temp.append(val)
        res[key]=val
print(temp)
print(res)
    
