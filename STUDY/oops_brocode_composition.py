#Composition = The Composed onject directly owns it's components, which cannot exist 
#              independently "owns -a" relationship

# Engine class represents the engine of a car
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

# Wheel class represents a wheel of a car
class Wheel:
    def __init__(self, size):
        self.size = size

# Car class is composed of Engine and Wheels
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        # Car CREATES its own Engine (composition)
        self.engine = Engine(horse_power)
        # Car CREATES its own Wheels (composition)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
        
    # Method to show car details
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

# Creating Car objects (with their own Engine and Wheels)
car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

# Display details of each car
print(car1.display_car())
print(car2.display_car())