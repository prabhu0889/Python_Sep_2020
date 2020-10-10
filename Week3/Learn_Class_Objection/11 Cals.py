class Cals:

    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.args = args

    def add_two_num(self):
        return self.a + self.b

    def add_items(self,):
        return sum(self.args)

    # def sum_items(self):
    #     count = 0
    #     for i in self.args:
    #         count = count + int(i)
    #     return str(count)
    #
1000
# obj1 = Cals(1000, 2000, 1, 2, 3, 4, 5, 10, 20, 30)
# x = obj1.add_two_num()
# print(x)

# y = obj1.add_items()
# print(y)
#
obj2 = Cals(10, 20, '1', '2', '3', '4')
z = obj2.sum_items()
print(z)
print(type(z))