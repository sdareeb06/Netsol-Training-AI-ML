# Exception Handling
# try:
#     num = int(input("Enter a name: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("That is not a valid number")
# finally:
#     print("Done Trying.")

# print("---------------------------------")

# try:
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("That is not a valid number")
# finally:
#     print("Task Done.")


# Object Oriented Programming

# class And Object
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hi, I am {self.name}")
#         print(f"Hi, I am {self.age}")

# s1 = Student("Ali", 20)
# s1.greet()

# print("--------------------------------")

# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#     def start_engine(self):
#         print(f"Car Brand, {self.brand} {self.year}'s Model")
# s1 = Car("BMW", 2026)
# s1.start_engine()


# class Car:
#     def __init__(self, mileage, maxSpeed):
#         self.mileage = mileage
#         self.maxSpeed = maxSpeed
#     def Display(self):
#         print(f"Civic Max Speed is {self.maxSpeed}Km/h with Mleage {self.mileage}")
# s1 = Car(20, 220)
# s1.Display()


# class Student:
#     school = "NAVTTAC"

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Ali")
# s2 = Student("Sara")
# print(s1.school, s2.school)
# print(s1.name)

# print("------------------------")

# class Employee:
#     company_name = "NETSOl"

#     def __init__(self, name):
#         self.name = name

# Employee1 = Employee("john")
# Employee2 = Employee("Ali")
# Employee3 = Employee("Hassan")
# print(f"{Employee1.name} work at {Employee1.company_name}")
# print(f"{Employee2.name} work at {Employee2.company_name}")
# print(f"{Employee3.name} work at {Employee3.company_name}")


# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} created")

#     def __del__(self):
#         print(f"{self.name} destroyed")

# s1 = Student("Ali")
# del s1


# class Book:
#     def __init__(self, name):
#             self.name = name
#             print(f"{self.name} book has been added")
#     def __del__(self):
#           print(f"{self.name} book has been removed")
# book1 = Book("The Life")
# del book1

""" Inheritance """

# class Animal:
#     def eat(self):
#         print("Eating...")

# class Dog(Animal):
#     def bark(self):
#         print("Barking...")

# d = Dog()
# d.eat()
# d.bark()

# class vehicle:
#     def start(self):
#         print("Starting...")
# class car(vehicle):
#     def honk(self):
#         print("honking...")
# d = car()
# d.start()
# d.honk()


# class Shape:
#     def area(self):
#         print("Calculating Area")
# class Circle(Shape):
#     def areaCircle(self):
#         print("Area Of circle")
# class Square(Shape):
#     def areaSquare(self):
#         print("Area of Square")

# circ = Circle()
# circ.areaCircle()
# squ = Square()
# squ.areaSquare()
      
""" Multiple Inheritance & MRO"""

# class Flayer:
#     def move(self):
#         print("Flying")
# class Swimmer:
#     def move(self):
#         print("Swimming")
# class duck(Flayer, Swimmer):
#     pass

# duck().move()

# class Camera:
#     def Work(self):
#         print("clicking")
# class Phone:
#     def Work(self):
#         print("Ringing")
# class SmartPhone(Camera, Phone):
#     pass
# SmartPhone().Work()


class Camera:
    def Work(self):
        print("clicking")
class Phone:
    def Work(self):
        print("Ringing")
class SmartPhone(Camera, Phone):
    pass
print(SmartPhone.__mro__)

print(SmartPhone.mro())


""" Access Sepecifier and Name Mangling"""

# class Account:
#     def __init__(self, balance):
#         self.balance = balance
#         self._pin = 1234
#         self.__pasword = "secret"
# a = Account(500)
# print(a.balance)
# # print(a.__pasword) #Error


# class BankAccount:
#     def __init__(self, name, branch):
#         self.account_holder = name
#         self._branch = branch
#         self.__pin = "secret"
# account = BankAccount("Ali", "UBL")
# print(account.account_holder)
# print(account._branch)
# print(account.__pin) #Error

""" Inner Classes, Association, Aggregation & Composition"""

# class Engine:
#     def start(self):
#         print("Engine Started")
# class Car:
#     def __init__(self):
#         self.engine = Engine() #commposite

#     def drive(self):
#         self.engine.start()
# Car().drive()


# class Library:
#     def place(self):
#         print("Library is open")

# class Book:
#     def __init__(self):
#         self.library = Library()

#     def reading(self):
#         self.library.place()
# Book().reading()