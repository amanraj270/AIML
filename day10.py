# Polymorphism
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhello(self):
        print("Hello everyone")


class Smith(Person):
    def sayhello(self):
        print(f"Hello, my name is {self.name}, and my age is {self.age}")


s1 = Smith("Smith", 20)
p1 = Person("Smith", 20)

# p1.sayhello()
# s1.sayhello()


# Encapsulation
class Student:
    def __init__(self, name):
        self.name = name  # Public

    def display(self):
        print(self.name)


s1 = Student("Allen")
# print(s1.name)
# s1.display()


class Student1:
    def __init__(self, name):
        self._name = name  # Protected

    def display(self):
        print(self._name)


s2 = Student1("Allen")
# print(s2._name)
# s2.display()