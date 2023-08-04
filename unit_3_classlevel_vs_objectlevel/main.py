class BankAccount:
    # class attribute
    interestRate = 1.3
    customers = 0

    def __init__(self, number, holder, balance):
        # instance/object attribute
        self.number = number
        self.holder = holder
        self.balance = balance
        BankAccount.customers += 1

    def __str__(self):
        return f'Bank Account: number-{self.number}, holder-{self.holder}, balance-{self.balance}'

    def calculateInterest(self):
        interest = self.balance * BankAccount.interestRate
        return interest


acc1 = BankAccount(123, 'Tom', 25)
acc2 = BankAccount(456, 'Bob', 48)

print(acc1)
print(f'Interest rate: {BankAccount.interestRate} - Interest: {acc1.calculateInterest()}')
print(acc2)
print(f'Interest rate: {BankAccount.interestRate} - Interest: {acc2.calculateInterest()}')
