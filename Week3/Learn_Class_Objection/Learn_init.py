class Test_Leaf:

    def __init__(self, name, ph, email):
        self.name = name                        # instance variable
        self.ph = ph
        self.email = email


    def register(self):                         # instance method #class method #static method
        print('name---->', self.name)
        print("ph----->",self.ph)
        print("email---->",self.email)



per1 = Test_Leaf("Divya", "123457", "divya@gmail.com")   # Divya
per1.register()
#
per2 = Test_Leaf("Sindu", "232323", "sindu@gmail.com")   # Sindu
per2.register()
#
#
# per3 = Test_Leaf()   # Tonie