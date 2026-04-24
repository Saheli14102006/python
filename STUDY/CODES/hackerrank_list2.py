lst=[]
n=int(input('Range:'))
c=0
while(1):
    command=input()
    match command:
        case "insert"|"append":
            i=int(input('Index'))
            e=int(input('Element'))
            lst.append(e)
            c=c+1
        case "prints":
            print(lst)
        case "remove":
            e=int(input('Element'))
            lst.remove(e)
        case "sort":
            sort(lst)
        case 'pop':
            lst.pop(i)
        case "reverse":
            reverse(lst)
        
            
            
                
