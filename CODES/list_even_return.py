n=int(input('Enter the range'))
arr=[]
for i in range(n):
  arr.append(int(input('Enter element: ')))
print('Original array:',arr)
even=[]
for j in arr:
  if j%2==0 and j not in even:
    even.append(j)
print('Even numbers in the array:',even)
