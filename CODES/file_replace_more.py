words=['donkey','animal','farmers']
with open('donkey.txt','w')as f:
    f.write('A donkey is a hardworking animal.\n')
    f.write('donkey carries loads and helps farmers.\n')
    f.write('Donkeys are known for their patience and strength.\n') 
with open('donkey.txt','r')as f:
    content=f.read()
for i in words:
    content=content.replace(i,'#'*len(i))
print(content)
with open('donkey.txt','w')as f:
    f.write(content)