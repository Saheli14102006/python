s1={}
print(type(s1)) #empty dictionary
e=set()
print(type(e)) #empty set
s={1,5,70,9,5,5,5,'saheli'} #duplicate values are not allowed in set, it will only store unique values, it is unordered, it is iterable, it is a collection of items that are unordered, unchangeable, and do not allow duplicate values.
s.add('tom')
s.add(99)
print(s,type(s))
s1={'hello',19,'tom',9}
print(s.union(s1))
print(s1.intersection(s))
print({1,5}.issubset(s))
print(s-s1)
s2=set()
for i in range(4):
    e=input()
    if e.isdigit():
        s2.add(int(e))
    else:
        s2.add(e)
print(s2,type(s2))