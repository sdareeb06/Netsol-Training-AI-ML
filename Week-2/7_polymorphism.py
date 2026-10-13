""" Polymorphism & Operator Overloading"""
# class cat:
#     def speak(self):
#         print("Meow")

# class Dog:
#     def speak(self):
#         print("woof")

# for animal in [cat(), Dog()]:
#     animal.speak()


# class Square:
#     def Area(self):
#         print("Area og Square")
# class Circle:
#     def Area(self):
#         print("Area of Circle")
# for shape in [Square(), Circle()]:
#     shape.Area()

# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return self.x + other.x, self.y + other.y

# p1 = point(1,2)
# p2 = point(3,4)
# print(p1 + p2)

""" Magic / Dunder Functions"""

# class Book:
#     def __init__(self, title):
#         self.title = title

#     def __str__(self):
#         return f"Book: {self.title}"

# b = Book("Python OPP")
# print(b)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f" The price of {self.name} is {self.price}"

# p1 = Product("Burger", 300)
# print(p1)

# class Items:
#     def __init__(self, list):
#         self.list = list

#     def __len__(self):
#         return len(self.list)

# p1 = Items(["Burger", "Pizza", "Biryani", "Cake"])
# print(len(p1))


""" Dynamic Polymorphism (Subclass as Base Class)"""

# class Shape:
#     def area(self):
#         print("Area not defined")
# class Circle(Shape):
#     def area(self):
#         print("Area = pi r^2")

# shapes = [Shape(), Circle()]
# for s in shapes:
#     s.area()

# class Employee:
#     def pay(self):
#         print("Employee receives salary")


# class Manager(Employee):
#     def pay(self):
#         print("Manager receives salary and bonus")


# e = Employee()
# m = Manager()

# e.pay()
# m.pay()

# class Employee:
#     def pay(self):
#         print("payment is granted")
# class Manager(Employee):
#     def pay(self):
#         print("payment is not granted")

# Employees = [Employee(), Manager()]
# for e in Employees:
#     e.pay()

"""Abstract Class"""

# from dataclasses import dataclass
# @dataclass
# class point:
#     x: int
#     y: int
# p = point(x= 3, y= 4)
# print(p)


# from dataclasses import dataclass
# @dataclass
# class Student:
#     name: str
#     age:int

# info = Student(name = "Ali", age = 25)
# print(info)

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Reactangle(shape):
    def area(self):
        print("Area Of reactangle")
A = Reactangle()
A.area()