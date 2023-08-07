class ShoppingList:
    def __init__(self):
        self.items = ['Cheese', 'Bread', 'Tomato', 'Meat']

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)


shoppingList = ShoppingList()
print(shoppingList[0])
print('--------------------')
for item in shoppingList:
    print(item)

print('--------------------')
if 'Bread' in shoppingList:
    print('There is bread in the shopping list.')

