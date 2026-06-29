# OOPS - Object Oriented Programming System

class Example:

    def __init__(self):
        print("This is class constructor")

    def sayHello(self):
        print("Hello Everyone")

    def sayGoodbye(self):
        print("Good Bye")


# obj1 = Example()
# obj1.sayHello()

# obj2 = Example()
# obj2.sayGoodbye()


# Default Constructor

class Student:

    def __init__(self):
        self.name = "Smith"
        self.age = 20


s1 = Student()
s2 = Student()

# print(s1.name, s1.age)
# print(s2.name, s2.age)


# Parameterized Constructor

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age


e1 = Employee("Smith", 20)
e2 = Employee("John", 30)

# print(e1.name, e1.age)
# print(e2.name, e2.age)

# Non-Parameterized Constructor

class Animal:

    def __init__(self):
        print("Animal Created")


a1 = Animal()
a2 = Animal()

