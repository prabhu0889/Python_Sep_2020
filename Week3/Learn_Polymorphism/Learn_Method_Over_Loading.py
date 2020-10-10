class TestLeaf:
    ls = []
    def __init__(self, *args):
        self.ls = args
        print(self.ls)


obj1 = TestLeaf('Divya', 'Balaji', 'Mohan')   # Overloading
obj2 = TestLeaf('Babu', 'Sarath')             # Overloading


class T1:

    def __init__(self, **kwargs):
        print(kwargs)

d = T1(a = 10, b = 20, c = 30)
d1 = T1(aa = 100, bb = 200)


#***************************************************************************************

# Operator Overloading

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)

print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))