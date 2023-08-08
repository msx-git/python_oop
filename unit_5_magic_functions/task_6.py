class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle ({self.width},{self.height})'

    def surface(self):
        return self.width * self.height

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.surface() > other.surface()
        elif isinstance(other, (int, float)):
            return self.surface() > other
        else:
            raise ValueError('Invalid comparison')


r1 = Rectangle(2, 6)
r2 = Rectangle(2, 3)

if r1 > r2:
    print('r1 is bigger than r2')
else:
    print('r2 is bigger than r1')

if r1 > 10:
    print('r1 is a big rectangle')

# error case
# if r2 > '25':
#     print('error')
