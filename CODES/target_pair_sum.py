n=int(input('Enter the taget number: '))
list1=[10,30,20,40,50,60]
i=0
j=0
for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[i]+list1[j]==n:
            print('The pair is:',list1[i],'+',list1[j],'=',(list1[i]+list1[j]))