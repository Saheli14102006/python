marks={
    'Saheli':100,
    'Tomojit':100,
    'Jhon':9
    }
# print(marks.items())
# print(type(marks))
# print(marks['Saheli'])
marks.update({'Jhon':99,'Hena':88})
print(marks.items())
print(marks.get('Hena'))
print(marks['Jhon'])
d={}
for _ in range (2):
    key=input()
    if key.isdigit():
        key=int(key)
    value=input()
    if value.isdigit():
        value=int(value)
    d[key]=value
print(d)