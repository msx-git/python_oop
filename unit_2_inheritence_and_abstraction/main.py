from circle import Circle

circle = Circle('black', 5, (5, 3), 8)
print(circle)

circle.changeBorderColor('Red')
circle.changeBorderThickness(6)
print(circle)
print(circle.area())
