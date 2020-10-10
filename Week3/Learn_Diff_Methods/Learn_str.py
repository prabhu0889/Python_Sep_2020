class A:

    def __init__(self, a):
        print(self)
        print(a)

    def __str__(self):
        a = b = 0
        return 'ABC'


x = A(100)
print(x)
