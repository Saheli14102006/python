n = int(input("Enter number of elements: "))

arr = []
print("Enter the array elements:")
for i in range(n):
    arr.append(int(input()))

if n < 2:
    print("Need at least 2 elements")
else:
    max1 = float('-inf') # Initialize max1 to the smallest possible value, let max1 is the largest element
    max2 = float('-inf') # Initialize max2 to the smallest possible value, let max2 is the second largest element

    for i in range(n):   
        if arr[i] > max1:    # If current element is greater than max1
            max2 = max1      # Update max2 to the old max1
            max1 = arr[i]   # Update max1 to the current element    
        elif arr[i] > max2 and arr[i] != max1:  # If current element is greater than max2 and not equal to max1
            max2 = arr[i]   # Update max2 to the current element
        elif arr[i]<max1 and arr[i]<max2: # If current element is less than max1 and max2
            continue

    if max2 == float('-inf'):
        print("No second maximum") 
    else:
        print("Second maximum =",max2)