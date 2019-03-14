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


class ChugJug(Consumable):
    def __abs__(self):
        super(ChugJug, self).__init__("ChugJug", "ChugJug restores all of your health and shield points")


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


class SMG(Weapon):
    def __init__(self):
        super(SMG, self).__init__("SMG", "The SMG is a medium damage fast firing weapon", 30, 24)


class P90(Weapon):
    def __init__(self):
        super(P90, self).__init__("P90", "The P90 has medium damage, fastest firing gun in its class", 40, 21)


class HeavySniper(Weapon):
    def __init__(self):
        super(HeavySniper, self).__init__("heavy Sniper", "The Heavy Sniper has the slowest fire rate, but most damage"
                                                          "in its class", 1, 150)


class SilencedSniper(Weapon):
    def __init__(self):
        super(SilencedSniper, self).__init__("Silenced Sniper", "The silenced sniper has the fastest reload speed, and "
                                                                "enough damage to take out someone in 2 shots", 1, 105)


class Scar(Weapon):
    def __init__(self):
        super(Scar, self).__init__("Scar", "The Scar is the best AR in its class, has a high damage too", 30, 36)



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




