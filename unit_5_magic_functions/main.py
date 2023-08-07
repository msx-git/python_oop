class LinearModul:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # This makes the object callable
    def __call__(self, x):
        output = self.a * x + self.b
        return output

    def compute(self, x):
        output = self.a * x + self.b
        return output


lm = LinearModul(2, 5)

# with callable object
out1 = lm(3)
print(out1)

# with object function
out2 = lm.compute(2)
print(out2)
