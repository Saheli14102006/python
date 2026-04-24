n=5
s=[n]
top=-1
def push():
    data=int(input('enter'))
    global top,n,s
    if(top==n-1):
        print('stack overflow')
        return
    else:
        top=top+1
    s[top]=data
def pop():
    global top,s,n
    if(top==-1):
        print('stack Underflow')
        return 
    else:
        d=s[top]
        top=top-1
        print(d)
        return d
def display(data):
    global s,top,n
    for i in range(top,-1):
        print(s[i])
print('1 for push  \n 2 for pop \n 3 for display')
while(1):
    command=input('enter choice')
    match command:
        case '1':
            #data=int(input('enter'))
           #s.append(data)
            push()
        case '2':
            pop()
        case '3':
            display()
    
    