class A:

    def __init__(self):
        print("I'm from A - init")


class B(A):

    def __init__(self):
        print("I'm from B")
        super().__init__()

x = B()


