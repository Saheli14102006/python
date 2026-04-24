s=input("enter a string")
vowels="aeiou"
l=len(s)
print(l)
c=0;
for i in range(0,l):
    if s[i] in vowels:
        c=c+1
print("NO. OF VOWElS",c)
        
