# Templates
class TestLeaf:

    # variable
    # methods
    # const

    def python(self):
        print("Python for Dev")

    def appium(self):
        print("Appium for Mobile Automation")
#*************************************************************

per1 = TestLeaf()               # Object 1
per1.python()
print(id(per1))
#****************************************************************

per2 = TestLeaf()               # Object 2
per2.appium()
print(id(per2))