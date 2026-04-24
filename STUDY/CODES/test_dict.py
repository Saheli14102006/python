s1=dict()
for _ in range(3):
    k=input("enter student id")
    v=list(input("Enter name,age,subject").split(','))
    s1[k]=v
print(s1)
max=0
for key in s1.keys():
    info=s1[key]
    age=int(info[1])
    if age>max:
        max=age
print(max)
        
