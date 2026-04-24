#super()= is used to call the parent class method in the child class. It is used to access the methods of the parent class from the child class. It is also used to call the constructor of the parent class from the child class. Allows you to extend the functionality of inherited methods.
class Shape:
  def __init__(self,color,filled):
    self.color=color
    self.filled=filled
  def describe(self):
    print(f'This is a {self.color} shape and it is {"filled" if self.filled else "not filled"}.')
class Circle(Shape):
  def __init__(self,color,filled,radius):
    super().__init__(color,filled)  #super() is used to call the constructor of the parent class (Shape) and pass the color and filled parameters to it. This way we don't have to write the code to initialize the color and filled attributes in the Circle class, we can just call the parent class constructor.
    self.radius=radius
    
  def describe(self):
    super().describe() #super() is used to call the describe method of the parent class (Shape) and then we can add our own code to it. This way we can extend the functionality of the describe method in the Circle class without having to rewrite the code of the describe method in the Shape class. 
    print(f'This is a {self.color} circle and it is {"filled" if self.filled else "not filled"}The radius of the circle is {self.radius}.')  #If the child class share the same method as the parent class, then it will print the method of the child class, this is called method overriding. If we want to call the method of the parent class, we can use super() to call the method of the parent class.
    
class Square(Shape):
  def __init__(self,color,filled,width):
    super().__init__(color,filled)
    self.width=width
class Triangle(Shape):
  def __init__(self,color,filled,width,height):
    super().__init__(color,filled)
    self.width=width
    self.height=height
    
circle=Circle(color='Red',filled=True,radius=5)
square=Square(color='Blue',filled=False,width=4)
triangle=Triangle(color='Green',filled=True,width=3,height=4)
print(circle.color)
print(circle.filled)
print(f'Radius of the circle is {circle.radius}.')
print(square.color)
print(square.filled)
print(f'Width of the square is {square.width}.')
print(triangle.color)
print(triangle.filled)
print(f'Width of the triangle is {triangle.width} and height of the triangle is {triangle.height}.')
circle.describe()
