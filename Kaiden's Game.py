class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None, item=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = item
        self.first_time = True


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """

        :param new_location: The room object of which you are
        :return:
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so ee if a room exists in that direction

        :param direction: The direction that you want to move to
        :return: The room object if it exists, or None if it doe
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


class Character(object):
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class SkullTrooper(Character):
    def __init__(self):
        super(SkullTrooper, self).__init__("Skull trooper", 200, PumpShotgun)


class DefaultBoy(Character):
    def __abs__(self):
        super(DefaultBoy, self).__init__("Default Boy", 75, Pistol)


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


class ShieldPot(Consumable):
    def __init__(self):
        super(ShieldPot, self).__init__("Shield Potion", "A Shield Potion grants you 50 shield points", 1)


class Bandages(Consumable):
    def __init__(self):
        super(Bandages, self).__init__("Bandages", "Bandages restore you 15 health points", 5)


class Medkits(Consumable):
    def __init__(self):
        super(Medkits, self).__init__("Medkit", "Medkit restore all of your health points", 1)


class SlurpJuice(Consumable):
    def __init__(self):
        super(SlurpJuice, self).__init__("SlurpJuice", "SlurpJuice restores  25 shield point", 1)


class ChugJug(Consumable):
    def __init__(self):
        super(ChugJug, self).__init__("Chug Jug", "ChugJug restores all of your health and shield points", 1)


class Weapon(Item):
    def __init__(self, name, description, bullets, damage):
        super(Weapon, self).__init__(name)
        self.description = description
        self.bullets = bullets
        self.damage = damage


class TacticalShotgun(Weapon):
    def __init__(self):
        super(TacticalShotgun, self).__init__("Tactical Shotgun", "The tactical shotgun is a rapid firing shotgun,", 8,
                                              74)


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


class PumpShotgun(Weapon):
    def __init__(self):
        super(PumpShotgun, self).__init__("Pump Shotgun", "The pump is a reliable medium firing rate shotgun", 5, 105)


class Pistol(Weapon):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", "The pistol is a small damage medium firing handgun", 16, 23)


pistol = Pistol()
pump_Shotgun = PumpShotgun()
scar = Scar()
silenced_Sniper = SilencedSniper()
heavy_Sniper = HeavySniper()
p90 = P90()
sMG = SMG()
tactical_Shotgun = TacticalShotgun()
assault_Rifle = AssaultRifle()
bandages = Bandages()
med_kits = Medkits()
chug_Jug = ChugJug()
shield_Pot = ShieldPot()
slurp_Juice = SlurpJuice()
mini = Mini()


R19A = Room("Mr. Wiebe's Room", "This is mr wiebe's room", 'parking_lot', None, None, None, mini)


parking_lot = Room("Parking Lot", "The parking lot outside", None, "R19A", None, None, med_kits)

battle = Room("BATTLE BUS", "You are in the battle bus "
                            "Now you can either go North to Retail Row or south to Paradise Palms ",
              "retail", "palms", None, None, )
retail = Room("RETAIL ROW", "You are at retail row. if you go south you will be at Paradise Palm. \n"
                            "If you go north you will reach tomato temple",
              "tomato", "palms", None, None, pistol)
palms = Room("PARADISE PALMS", "You are at Paradise Palms. Its very dry here with a lot of mountains"
                               "You can either go north to retail row or west to fatal fields",
             "retail", None, None, "fatal", tactical_Shotgun)
tomato = Room("TOMATO TEMPLE", "You are at Tomato Temple. This place was a religious sanctuary for tomatoes"
                               "You can either go east to wailing woods, north to the block, or west to lazy links",
              "block", None, "wailing", "lazy", bandages)
lazy = Room("LAZY LINKS", "You are at Lazy Links. This place has a mansion and alot of golf course"
                          "You can either go west to pleasant park, or east to the block",
            None, None, "block", "pleasant", heavy_Sniper)
pleasant = Room("PLEASANT PARK", "You are at Pleasant Park. This place is a nice park but isnt pleasant"
                                 "You can go North to junk junction, or south to viking mountain",
                "junk", "viking", None, None, silenced_Sniper)
junk = Room("JUNK JUNCTION", "You are at junk junction.This place is a trash dump and smells really bad"
                             "You can either go south to Pleasant park or east to lazy links",
            None, "pleasant", "lazy", None, shield_Pot)
block = Room("THE BLOCK", "You are at the block.This place is updated every week with player creations"
                          "You can go south to Wailing Woods,or west to lazy links",
             None, "wailing", None, "lazy", assault_Rifle)
wailing = Room("WAILING WOODS", "You are at Wailing Woods.This place is a calm forest"
                                "You can go south to retail row or west to tomato temple",
               None, "retail", None, "tomato", bandages)
fatal = Room("FATAL FIELDS", "You are at Fatal Fields. This place is a nice little farm ranch"
                             "You can west to happy hamlet or north to salty springs",
             "salty", None, None, "hamlet", p90)
hamlet = Room("HAPPY HAMLET", "You are at happy hamlet. Its really cold here but there is a small town"
                              "You can either go west to frosty flights or north to tilted towers",
              "tilted", None, None, "frosty")
frosty = Room("FROSTY FLIGHTS", "You are at frosty flights. There are a few airplane hangars"
                                "You can either go north to viking mountain or east to happy hamlet",
              "VIKING MOUNTAIN", None, "HAPPY HAMLET", None, heavy_Sniper)
viking = Room("VIKING MOUNTAIN""You are at Viking Mountain. This is a lost viking camp on a mountain"
                               "You can either go east to tilted towers, west to snobby shores, north to pleasant park"
                               "or south to frosty flights",
              "pleasant", None, "tilted", "snobby", sMG)
tilted = Room("TILTED TOWERS", "You are at Tilted towers. this place is the biggest city on the map"
                               "You can go north to pleasant park,west to viking mountain,or south to happy hamlet",
              "pleasant", "happy", None, "viking", scar)
snobby = Room("SNOBBY SHORES", "You are at Snobby Shores. This place has a few modern apartments"
                               "you can either go east to viking mountain,south to frosty flights,"
                               " or north to junk junction",
              "junk", "frosty", "viking", None, chug_Jug)
player = Player(retail)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
command = ''
while playing:
    if command != 'look':
        print(player.current_location.name)
    if player.current_location.first_time:
        print(player.current_location.description)
        player.current_location.first_time = False

    def attack(self, target):
        print("%s attacks %s for %d" % (self.name, target.name, self.weapon.damage))
        target.take_damage
    command = input(">_")
    if command.lower() in ['q', 'quit' 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I cant go that way")
    elif command == "look":
        print(player.current_location.name, player.current_location.description, player.current_location.item.name)
    elif command.lower() == "inventory":
        print("You have the following items:")
        if len(player.inventory) == 0:
            print("You have no items")
        for item in player.inventory:
            print(item.name)
    elif command == "take item":
        player.inventory.append(item)
    else:
        print("Command Not Found")
    print()


# Put items in room
# show items in room
# pick up item
# use item
