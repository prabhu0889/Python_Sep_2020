class Test_Data:

    def __init__(self, **kwargs):
        self.fname = kwargs['fname']
        self.lname = kwargs['lname']
        self.email = kwargs['email']
        self.pwd = kwargs['pwd']

# *************************************************************
print(Test_Data.fname)