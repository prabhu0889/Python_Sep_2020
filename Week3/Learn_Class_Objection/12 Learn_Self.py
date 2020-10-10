class Cals:

    def add(self, a, b):
        print("from self", self)
        #return a + b

    def mul(self, a, b):
        return a * b


obj1 = Cals()
print("form obj1", obj1)
obj1.add(10, 20)

obj2 = Cals()
print("form obj2", obj2)
obj2.add(100, 200)








