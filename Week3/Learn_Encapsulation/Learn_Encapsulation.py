class testleaf:

    mentors = ['B', 'B', 'D', 'S', 'S', 'H', 'N']
    account_num = 120435789
    __atm_pin = '1122'          # data hidding

    def __private_method(self): # implementation hidding
        return 1000

    def get_priv_method(self):
        return testleaf.__private_method(self)


    def get_data(self):
        return testleaf.__atm_pin

    def set_data(self, val):
        testleaf.__atm_pin = val

x = testleaf()
print(x.get_data())
x.set_data('3344')
print(x.get_data())

print(x.get_priv_method())





