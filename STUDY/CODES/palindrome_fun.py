def palindrome(a):
    rev=0
    n=a
    while(a>0):
      r=int(a%10)
      a=int(a/10)
      rev=rev*10+r
    if(n==rev):
        print("Palindrome",n)
    else:
        print("Not Palindrome",n)
    print(n)

x=int(input("enter a number"))
palindrome(x)
