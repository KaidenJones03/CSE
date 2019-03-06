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


class Shield_Pot(Consumable):
    def __init__(self):
        super(Shield_Pot, self).__init__("Shield Potion", "A Shield Potion grants you 50 shield points", 1)
        

class Bandages(Consumable):

