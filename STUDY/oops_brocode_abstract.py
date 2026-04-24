#Abstract Class- A class that cannot be instantiated and is often used as a base class. It can contain abstract methods (methods without implementation) that must be implemented by subclasses. 

from abc import ABC, abstractmethod  #Abstract Base Class (ABC) module provides the infrastructure for defining abstract base classes in Python. 
class Vehicle(ABC):       #This is an abstract class because it inherits from ABC and contains abstract methods.
  
  @abstractmethod
  def go(self):
    pass
  
  @abstractmethod
  def stop(Self):
    pass
  
class Car(Vehicle):
  def go(self):
    print('You drive the car.')
  def stop(self):
    print('You stop the car.')
    
class Motorcycle(Vehicle):      #We always need to add the methods of the abstract class in the derived class, otherwise we will get an error.
  def __init__(self,name): 
    self.name=name
  def go(self):
    print(f'I can ride {self.name}.')
  def stop(self):
    print(f'Stop the {self.name}.')
  def color(self):              #We can also add other methods in the derived class, which are not present in the abstract class.
    print(f'My {self.name} is blue and black gradient color.')

car= Car()
car.go()
car.stop()
motor=Motorcycle('Royal Enfield')
motor.go()
motor.color()