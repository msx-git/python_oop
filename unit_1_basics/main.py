from bank_account import BankAccount
from product import Product
from shopping_list import ShoppingList

acc1 = BankAccount(86002515, 'John')
# print(acc1)

# print(f'number: {acc1.number}')
# print(f'holder: {acc1.holder}')
# print(f'balance: {acc1.balance}')

# acc1.deposit(150)
# print(f'balance: {acc1.balance} (after deposit)')

# acc1.withdraw(120)
# print(f'balance: {acc1.balance} (after withdrawal)')

# ------------------------------------------

shoppingList = ShoppingList('Grocery')
shoppingList.showProducts()
#
# product1 = Product('Oranges', 6)
# product2 = Product('Milk', 1)
# product3 = Product('Bread', 2)
#
# shoppingList.addProduct(product1)
# shoppingList.addProduct(product2)
# shoppingList.addProduct(product3)
#
# shoppingList.addProduct('Meat')
#
# shoppingList.showProducts()
