class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def __str__(self):
        return f'Product: title - {self.title}, quantity - {self.quantity}'

    def changeQuantity(self, newQuantity):
        self.quantity = newQuantity
