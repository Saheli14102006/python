l=["Harry","Rohan","Shubham","An"]
def rem(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n
print(rem(l,"R")) 
# strip removes letters from start and end only