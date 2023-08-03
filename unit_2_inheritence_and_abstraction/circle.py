from shape import Shape
import math


class Circle(Shape):
    def __init__(self, borderColor, borderThickness, location, radius):
        super().__init__(borderColor, borderThickness, location)
        self.radius = radius

    def __str__(self):
        return f'{super().__str__()}, radius-{self.radius}'

    def area(self):
        return math.pi * self.radius ** 2
