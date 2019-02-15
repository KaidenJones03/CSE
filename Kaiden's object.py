class Computer (object):
    def __init__(self, charge_left):
        self.screen = True
        self.keyboard = True
        self.touchscreen = True
        self.power_button = True
        self.battery_left = charge_left
