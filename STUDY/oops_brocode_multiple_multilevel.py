#Multiple Inheritance: A class can inherit from multiple classes, and can use the methods of all the classes it inherits from. This is called multiple inheritance.

#Multilevel Inheritance: A class can inherit from a class that inherits from another class. This is called multilevel inheritance.

class Animal:             #base class, means that other classes will inherit from this class.
  def __init__(self,name):
    self.name=name
  def eat(self):         
    print(f'{self.name} is eating') 
  def sleep(self):
    print(f'{self.name} is sleeping')
    
class Prey(Animal):       #derived class, means that this class inherits from the base class, and can use the methods of the base class.
  def flee(self):
    print(f'{self.name} is fleeing')
    
class Predator(Animal):   #derived class
  def hunt(self):
    print(f'{self.name} is hunting')
    
class Rabbit(Prey):       #derived class, means that this class inherits from the Prey class, and can use the methods of the Prey class, and also the methods of the Animal class. Rabbit is multilevel inheritance because it inherits from Prey, which inherits from Animal.
  pass

class Hwak(Predator):   #derived class, means that this class inherits from the Predator class, and can use the methods of the Predator class, and also the methods of the Animal class.
  pass

class Fish(Prey,Predator): #derived class, means that this class inherits from both the Prey class and the Predator class, and can use the methods of both classes, and also the methods of the Animal class. Here Fish is multiple inheritance because it inherits from both Prey and Predator.
  pass

rabbit=Rabbit('Bugs')
hawk=Hwak('Tony')
fish=Fish('Nemo')
rabbit.eat()
rabbit.flee()
fish.flee()
fish.hunt()
    
  
  
    