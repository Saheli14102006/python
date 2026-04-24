class car:   #car is a class
  def __init__(self, model, year, color, for_sale): #It's a Dunder Method and only init func is automatically called. The function with double underscore is called Dunder.
    self.model = model    #self.model is an instance variable
    self.year = year
    self.color = color
    self.for_sale = for_sale   #init is a constructor, it is used to initialize the attributes of the class, it is called when an object of the class is created. self,model, year, color, for_sale are the parameters of the constructor, self is a reference to the current object of the class, it is used to access the attributes and methods of the class.
    
    #Method - Method is a function that is defined inside a class, it is used to perform a specific action, it is called by using the dot operator and the name of the method.
    
  def drive(self):
      print(f'The car is driving {self.model}')   #drive is a method of the class car.
  def stop(self):
      print('The car is stopped')   #stop is a method of the class car.
  def describe(self):
      print(f'{self.model} is produced in {self.year} its color is {self.color} and it is for sale {self.for_sale}')   #describe is a method of the class car, it will print the details of the car object.