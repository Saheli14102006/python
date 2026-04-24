a=(1,2,5,6,2,2)  #tuple is immutable. This means that we cannot change the values of a tuple once it is created. We can only read the values of a tuple, but we cannot modify them.
# a[0]=453
print(len(a))
#lets take an user input for tuple
store=input('Enter numbers')
list1=store.split(',')  #split() is used to split the string into a list of substrings based on the specified delimiter, which is a comma in this case. The resulting list will contain the individual numbers as strings.
tuple1=tuple(list1)  #tuple() is used to convert the list of strings into a tuple. The resulting tuple will contain the individual numbers as strings.
print(list1)
print(type(a))
no=a.count(2)
print(no)
i=a.index(5)
print(i)