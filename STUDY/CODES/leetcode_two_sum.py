n = int(input('range'))
nums = []
for i in range(n):
    nums.append(int(input('elements')))
target = int(input('target'))
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print(i, j)

