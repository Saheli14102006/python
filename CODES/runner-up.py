n = int(input('range'))
arr=[]
i=0
print('Scores of Runner-up')
for i in range (0,n):
    ele=int(input())
    arr.append(ele)
max1=arr[0]
max2=arr[0]
for i in range (0,n):
    if(arr[i]>=max1):
        max2=max1
        max1=arr[i]
    elif (max1>arr[i]>max2):
        max2=arr[i]
print('Runner-up',max2)

    