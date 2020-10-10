class TestLeaf:

    def python(self):               # Instance Method
        return 'python'

    def appium(self):
        return 'Appium'

    @classmethod
    def collect_info(cls):          # class Method
        print('class method')

    @staticmethod
    def use_umbrella():             # Static Method
        print('umbrella')


per2 = TestLeaf()

per2.collect_info()
TestLeaf.collect_info()

TestLeaf.use_umbrella()
per2.use_umbrella()
