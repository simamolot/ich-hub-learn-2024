# . Реализуйте класс Employee, представляющий сотрудника компании.
# Класс должен иметь статическое поле company с названием компании, а также методы:
# set_company(cls, name): метод класса для изменения названия компании
# __init__(self, name, position): конструктор, принимающий имя и должность сотрудника
# get_info(self): метод, возвращающий информацию о сотруднике в виде строки (имя, должность, название компании)
#
# Пример использования:
# employee1 = Employee("John", "Manager")
# employee2 = Employee("Alice", "Developer")
# print(employee1.get_info())  # Вывод:
#
# """
#
# Name: John
#
# Position: Manager
#
# Company: ABC Company
#
# """
#
# Employee.set_company("XYZ Company")
#
# print(employee2.get_info())  # Вывод:
#
# """
#
# Name: Alice
#
# Position: Developer
#
# Company: XYZ Company
#
# """


class Employee:
    company = 'abc company'

    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def set_company(cls, company_name):
        cls.company = company_name

    def get_info(self):
        return f'{self.name}\n{self.position}\n{self.company}\n'


employee1 = Employee("John", "Manager")
employee2 = Employee("Alice", "Developer")
employee3 = Employee("Bob", "Junior")
print(employee1.get_info())  # Вывод:
print(employee2.get_info())
print(employee3.get_info())

Employee.set_company('amazon')
print(employee1.get_info())


# 2. Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте классы Rectangle (прямоугольник) и
# Circle (круг). Класс Shape должен иметь абстрактный метод area, который должен быть реализован в каждом дочернем
# классе. Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра. Выведите площадь и
# периметр прямоугольника и круга на экран.
#
# Пример использования:
# rectangle = Rectangle(5, 3)
# circle = Circle(2)
#
# print(f"Rectangle area: {rectangle.area()}")  # Вывод: Rectangle area: 15
#
# print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Вывод: Rectangle perimeter: 16
#
# print(f"Circle area: {circle.area()}")  # Вывод: Circle area: 12.566370614359172
#
# print(f"Circle perimeter: {circle.perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172
import abc
import math
from abc import ABC, abstractmethod


class Shape(abc.ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius



rectangle = Rectangle(5, 3)
circle = Circle(2)

print(f"Rectangle area: {rectangle.area()}")  # Вывод: Rectangle area: 15

print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Вывод: Rectangle perimeter: 16

print(f"Circle area: {circle.area()}")  # Вывод: Circle area: 12.566370614359172

print(f"Circle perimeter: {circle.perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172
