with open('donkey.txt','w')as f:
    f.write('A donkey is a hardworking animal.\n')
    f.write('donkey carries loads and helps farmers.\n')
    f.write('Donkeys are known for their patience and strength.\n') 
with open('donkey.txt','r')as f:
    content=f.read()
contentnew=content.replace('donkey','#####')
print(contentnew)
with open('donkey.txt','w')as f:
    f.write(contentnew)