dict1={}
n=int(input("Enter:"))
for i in range(n):
    name=input("key:")
    marks=float(input("value:"))
    dict1[name]=marks
print("The dictionary is:",dict1)
list=[]
for name,marks in dict1.items():
    first,last=name.split(" ")
    new=first[0]+" "+last
    list.append(new)
    print("Names:",list)
    #extract highest marks
list1=[]
dict2={}
for marks in dict1.values():
    list1.append(marks)
highest=max(list1)
for name,marks in dict1.items():
    if marks==highest:
        dict2[name]=marks
print("Details of Student who got the highest marks:",dict2)
list3=[]
dict3={}
for marks in dict1.values():
    list3.append(marks)
    for name,marks in dict1.items():
        if marks<3.0:
            dict3[name]=marks
print("Students who got less than 3.0 marks:",dict3)