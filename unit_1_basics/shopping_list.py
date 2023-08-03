from product import Product


class ShoppingList:
    def __init__(self, title):
        self.title = title
        self.items = []

    def __str__(self):
        print(f'Shopping list: title - {self.title}, items - {len(self.items)}')

    def addProduct(self, newItem):
        if isinstance(newItem, Product):
            self.items.append(newItem)
            print('New product was added')
        else:
            print('Item is not a Product')

    def showProducts(self):
        print(f'Number of item in the list: {len(self.items)}')
        for product in self.items:
            print(product.title, product.quantity)
