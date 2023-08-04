class ShoppingList:
    def __init__(self, items):
        self.items = items

    @classmethod
    def fromString(cls, textList):
        items = textList.split(',')
        return cls(items)


list1 = ShoppingList(['Banana', 'Apple'])
print(list1.items)
list2 = ShoppingList.fromString('Coke,Chips')
print(list2.items)
