class A:

    def a(self):
        print("I'm from Class A")


class B(A):

    def b(self):
        print("I'm from Class B")


x = A()
x.a()

y = B()
y.b()
y.a()
