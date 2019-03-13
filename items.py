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
        super(SlurpJuice, self).__init__("SlurpJuice", "SlurpJuice restores  25 shield point")


class Weapon(Item):
    def __init__(self, name, description, bullets, damage):
        super(Item, self).__init__(name)
        self.description = description
        self.bullets = ()
        self.damage = ()
        
        
class TacticalShotgun(Weapon):
    def __init__(self):
        super(TacticalShotgun, self).__init__("Tactical Shotgun", "The tactical shotgun is a rapid firing shotgun,"
                                              , 8, 74)


class AssaultRifle(Weapon):
    def __init__(self):
        super(AssaultRifle, self).__init__("Assault Rifle", "The Assault Rifle is a all around military gun", 30, 33)
        

class Character(object):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon


# items
sword = Weapon("Sword", 10)


# characters
orc = Character("Orcl", 100, sword, Armor("generic armor"))


def attack(self, target):
    print("%s attacks %s for %d" % (self.name, target.name, self.weapon.damage))
    target.take_damage




