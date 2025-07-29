# 1) Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0  

    def set_age(self, age):
        if age < 0:
            raise ValueError("Неверноооооо!!!!.")
        self._age = age

    def get_age(self):
        return self._age

chel = Person()
chel.set_age(25)
print(f"Возраст чела {chel.get_age()}")  


# 2) Наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof-Woof "

class Cat(Animal):
    def speak(self):
        return "Meow-meow neg**"


animals = [Dog("Aktosh"), Cat("Bagira")]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")


#  3) Полиморфизм

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

vehicles = [Car(), Bicycle()]

for vehicle in vehicles:
    print(move(vehicle))



# 4) Абстракция

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())   
print(round(circle.area(), 2)) 