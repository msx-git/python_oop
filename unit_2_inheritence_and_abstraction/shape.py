class Shape:
    def __init__(self, borderColor, borderThickness, location):
        self.borderColor = borderColor
        self.borderThickness = borderThickness
        self.location = location

    def __str__(self):
        return f'{self.__class__.__name__}: color-{self.borderColor}, thickness-{self.borderThickness}, location-{self.location}'

    def changeBorderColor(self, color):
        self.borderColor = color

    def changeBorderThickness(self, thickness):
        self.borderThickness = thickness
