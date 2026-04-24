from oops_brocode_car_method import car   #importing the class car from the file oops_brocode_car.py, it is used to create objects of the class car and access the attributes and methods of the class car.
    
car1= car('BMW', 2020, 'Black', True)   #car1 is an object of the class car, it is created by calling the constructor of the class car and passing the values of the parameters to the constructor.
car2= car('Audi', 2021, 'White', False)   #car2 is an object of the class car, it is created by calling the constructor of the class car and passing the values of the parameters to the constructor.

print(car1.model)   #it will print the model of the car1 object, it will access the model attribute of the car1 object using the dot operator.
print(car1.year)    #it will print the year of the car1 object, it will access the year attribute of the car1 object using the dot operator.
print(car1.color)   #it will print the color of the car1 object, it will access the color attribute of the car1 object using the dot operator.
print(car1.for_sale)    #it will print the for_sale of the car1 object, it will access the for_sale attribute of the car1 object using the dot operator.
car1.drive()   #it will call the drive method of the car1 object, it will access the drive method of the car1 object using the dot operator.
car1.stop()   #it will call the stop method of the car1 object
car2.describe()

print(car2.model)   #it will print the model of the car2 object, it will access the model attribute of the car2 object using the dot operator.