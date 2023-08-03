from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def getColor(self):
        return self.color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f'Circle: radius-{self.radius} color-{self.color}'


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'Rectangle: width-{self.width}, height-{self.height}, color-{self.color}'


circle = Circle('Red', 12)
rectangle = Rectangle('Blue', 8, 14)

print(circle)
print(rectangle)

print(circle.area())
print(rectangle.area())
