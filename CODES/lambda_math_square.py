import math

n = int(input("Enter number of elements: "))

nums = []
print("Enter elements:")

for i in range(n):
    nums.append(int(input()))

squared = list(map(lambda x: math.pow(x, 2), nums))   # Using lambda function to calculate the square of each element in the list, and map to apply it to each element in the list. list() is used to convert the map object to a list. 

print("Squared list:", squared)