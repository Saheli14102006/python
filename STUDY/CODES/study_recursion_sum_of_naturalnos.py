n=int(input("Enter a natural number: "))
def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n
print("Sum of first",n,"natural numbers is:",sum(n))