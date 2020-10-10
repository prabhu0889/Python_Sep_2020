class GA:
    def com123(self):
        print("My name is com from Class GA")

class GB:
    def com(self):
        print("My name is com from Class GB")


class A(GA):

    def a(self):
        print("I'm from Class A")

class B:

    def b(self):
        print("I'm from Class B")

    def com(self):
        print("My name is com from Class b")

class C(A, B):

    def c(self):
        print("I'm from Class C")

z = C()
z.com()

print(C.__mro__)    # Method Resolution Order (MRO)