class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, mileage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.mileage = mileage

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on")

    def move_forward(self):
        self.fuel -= 1
        print("The car moves forward")

    def turn_left(self):
        self.fuel -= 1
        print("The car turns left")

    def turn_off(self):
        self.engine_status = False
        print("You turn off the car")


class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__("Impala", 25)


class Keylesscar(Car):
    def __init__(self, name, mileage):
        super(Keylesscar, self).__init__(name, mileage)

    def start_engine(self):
        self.engine_status = True
        print("Engine is on")
Jacob_car = Impala()
Jacob_car.start_engine()
Jacob_car.move_forward()
Jacob_car.turn_left()
Jacob_car.move_forward()
Jacob_car.turn_off()
