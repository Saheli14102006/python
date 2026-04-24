weight=float(input('Enter Your Weight'))
unit=input('Kilograms or Pound? (K or L):')
if unit=='K':
    weight=weight*2.205
    unit='lbs.'
elif unit=='L':
    weight=weight/2.205
    unit='Kgs.'
else:
    print(f"{unit} was not valid")
print(f"Your weight is: {weight} {unit}")