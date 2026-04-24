with open('poem.txt') as f:
    lines = f.readlines()
lineno=1
for line in lines:
    if ('dicta' in line):
        print("Found line no.:",lineno)
        break
    lineno+=1
    
else:
    print("Not Found")