class Animal:
  def __init__(self, name):
    self.name=name
    self.is_alive=True
  def eat(self):
    print(f'{self.name} is eating')
  def sleep(self):
    print(f'{self.name} is sleeping')
    
#Inheritance - Inheritance is a feature of oops that allows a new class to inherit the properties and methods of an existing class. The new class is called the child class or subclass, and the existing class is called the parent class or superclass. The child class can also have its own properties and methods in addition to the properties and methods of the parent class. Inheritance promotes code reusability and helps to create a hierarchical relationship between classes.
    
class Dog(Animal): 
  def speak(self):
    print(f'{self.name} says Woof!')

class Cat(Animal):
  def speak(self):
    print(f'{self.name} says Meow!')

class Mouse(Animal):
  def speak(self):
    print(f'{self.name} says Squeak!')

dog=Dog('Scooby')
cat=Cat('Tom')
mouse=Mouse('Jerry')
print(dog.name)
print(f'{cat.name} is Alive = {cat.is_alive}')
dog.eat()
cat.sleep()
mouse.speak()
dog.speak()
cat.speak()

  