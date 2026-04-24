n = int(input("Enter number of elements: "))

arr = {}
print("Enter the array elements:")
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

unique = []     # Create an empty list to store unique elements

for num in arr:  #num is the current element in the array. If the loop is like that - for i in range(n): then num will be arr[i], means num will use index to access the current element in the array.
    if num not in unique:
        unique.append(num)

print("Array after removing duplicates:", unique)