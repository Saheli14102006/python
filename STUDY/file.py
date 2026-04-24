# f=open('file.txt')
# line=f.readline()
# while(line!=''):
#     print(line)
#     line=f.readline()
# f.close()

# st='Hello World\nThis is a test file.\nHave a nice day!'
# f=open('file.txt','a')
# f.write(st)
# f.close()


f=open('file.txt')
print(f.read())
f.close()
with open('file.txt','r') as f:
    print(f.read())
# we don't need to close the file when we use with statement



# f=open('file.txt')
# line=f.readline()
# print(line)
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)

# f.close()





# st='Hello World'
# f=open('file.txt','w')
# f.write(st)
# f.close()



# f=open('file.txt','r')
# data=f.read()
# print(data)
# f.close()