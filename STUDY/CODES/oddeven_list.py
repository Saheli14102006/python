l=[]
n=int(input('Enter the range'))
i=0
for i in range(n):
    ele=int(input())
    l.append(ele)
print(l)
for i in range(n):
    if(l[i]%2==0):
        print('Even',l[i])
    else:
        print('Odd',l[i])
