class BankAccount:
    def __init__(self, number, holder, balance):
        self.number = number
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f'Bank account - number:{self.number}, holder:{self.holder}, balance:{self.balance}'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return BankAccount(self.number, self.holder, self.balance + other)

        elif isinstance(other, Check):
            if self.number == other.number:
                return BankAccount(self.number, self.holder, self.balance + other.amount)
            else:
                raise ValueError('Account number and check number didn\'t match')
        else:
            raise ValueError(f'+ is not defined between Bank account and {other.__class__.__name__}')

    def __radd__(self, other):
        self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            if self.balance < other:
                raise ValueError(f'Amount exceeds the balance limit')
            else:
                return BankAccount(self.number, self.holder, self.balance - other)
        else:
            raise ValueError(f'- is not defined between Bank account and {other.__class__.__name__}')

    def __rsub__(self, other):
        self - other


class Check:
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount


acc1 = BankAccount(1425, 'Tom', 60)
print(acc1)
acc1 = acc1 + 20
print(acc1)
acc1 = acc1 - 30
print(acc1)

# error case, withdrawing more amount than balance
# acc1 = acc1 - 130

check1 = Check(1425, 70)
check2 = Check(1815, 150)

acc1 = acc1 + check1
print(acc1)

# error case, check number doesn't match
# acc1 = acc1 + check2
