#Polymorphism - Greek word that means to have 'Many forms or faces'.
#poly - many
#morph - forms
#2 ways to achieve polymorphism in python: 1. Inheritance 2. Duck Typing

#write a polimorphism program using inheritance. We will create a base class called Shape, and then we will create three derived classes called Circle, Square, and Triangle. Each derived class will have its own implementation of the describe method, which will print out the details of the shape. We will then create an instance of each shape and call the describe method on each instance to see the polymorphism in action.

from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius ** 2

class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2

class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5 * self.base * self.height

class Pizza(Circle):
  def __init__(self, topping, radius):
    super().__init__(radius)
    self.topping = topping


shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
  print(f"{shape.area()} cm squared")



