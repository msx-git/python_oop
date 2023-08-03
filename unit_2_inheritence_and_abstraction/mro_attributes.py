class A:
    def __init__(self):
        self.x = 25


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 5


class C(A):
    def __init__(self):
        super().__init__()
        self.z = 15


class D(B, C):
    pass


print(D.__mro__)

d1 = D()
print(d1.y, d1.x, d1.z)
