class Item(object):
    def __init__(self, name):
        self.name = name


class Consumable(Item):
    def __init__(self, name, description, quantity=1):
        super(Consumable, self).__init__(name)
        self.description = description
        self.quantity = quantity


class Mini(Consumable):
    def __init__(self):
        super(Mini, self).__init__("Mini Shield", "A mini Shield increases your shield points by 25", 3)


billy_bob_joe = Mini()
print(billy_bob_joe.quantity)


class ShieldPot(Consumable):
    def __init__(self):
        super(ShieldPot, self).__init__("Shield Potion", "A Shield Potion grants you 50 shield points", 1)


class Bandages(Consumable):
    def __init__(self):
        super(Bandages, self).__init__("Bandages", "Bandages restore you 15 health points", 5)


class Medkits(Consumable):
    def __init__(self):
        super(Medkits, self).__init__("Medkits", "Medkits restore all of your health points", 1)


class SlurpJuice(Consumable):
    def __init__(self):
        super(SlurpJuice, self).__init__("SlurpJuice", "SlurpJuice 25 shield point")





