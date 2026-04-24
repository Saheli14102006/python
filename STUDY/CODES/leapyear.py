a=int(input("Enter a no."))
if a%400==0:
    print("Leapyear",a)
elif(a%4==0 and a%100!=0):
    print('Leapyear',a)
else:
    print("Not",a)
