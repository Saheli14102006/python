f=open('poem.txt')
if 'twinkle' in f.read():
    print('found')
else:
    print('not found')
f.close()