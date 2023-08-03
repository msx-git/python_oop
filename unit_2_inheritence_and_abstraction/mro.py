class A:
    def hello(self):
        print("Hello from A")


class B(A):
    def hello(self):
        print("Hello from B")


class C(A):
    def hello(self):
        print("Hello from C")


class D(B, C):
    pass


# MRO for class D
print(D.__mro__)
d_instance = D()
d_instance.hello()
