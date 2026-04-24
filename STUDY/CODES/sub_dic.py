s1=dict()
for _ in range(3):
    k=input("enter student id")
    v=list(input("Enter name,age,subject").split(','))
    s1[k]=v
print(s1)

c=0
for key in s1.keys():
    info=s1[key]
    subject=(info[2])
    if subject=="comp":
        c=c+1
  

print(c)
        

