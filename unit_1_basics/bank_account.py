class BankAccount:
    def __init__(self, number, holder, balance=0):
        print('Bank account is created')
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Not enough money for withdrawal')

    def __str__(self):
        return f'Bank account: {self.number} - {self.holder} - {self.balance}'
