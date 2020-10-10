class Vehicle:

    def apply_brake(self):
        print('Com - Brake')

    def sound_horm(self):
        print('Com - Horn')


class Car(Vehicle):

    def turn_on_ac(self):
        print('AC')

class BMW(Car):

    def apply_brake(self):
        print('ABS - Brake')

drive = BMW()
drive.apply_brake()