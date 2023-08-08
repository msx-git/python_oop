class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point {(self.x, self.y)}'

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError('Unsupported operand')

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


p1 = Point(2, 3)
p2 = Point(3, 5)

print(p1)
print(p2)
print('--------------------------')
print(p1 + p2)
print('--------------------------')
print(p1 - p2)
print('--------------------------')
print(p1 + 10)
print(10 + p2)
