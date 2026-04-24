n=int(input('enter the range:'))
count=0
for i in range(1,n+1):
    if i%7==0 and i%10==6:
        count=count+1
        print(i)
print('The count of numbers is:',count)