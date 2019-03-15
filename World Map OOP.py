class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


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


R19A = Room("Mr. Wiebe's Room", "This is mr wiebe's room", 'parking_lot')
parking_lot = Room("Parking Lot", "The parking lot outside", None, "R19A")

battle = Room("BATTLE BUS", "You are in the battle bus "
                            "Now you can either go North to Retail Row or south to Paradise Palms ",
              "retail", "palms")
retail = Room("RETAIL ROW", "You are at retail row. if you go south you will be at Paradise Palm. \n"
                            "If you go north you will reach tomato temple",
              "tomato", "palms")
palms = Room("PARADISE PALMS", "You are at Paradise Palms. Its very dry here with a lot of mountains"
                               "You can either go north to retail row or west to fatal fields",
             "retail", None, None, "fatal")
tomato = Room("TOMATO TEMPLE", "You are at Tomato Temple. This place was a religious sanctuary for tomatoes"
                               "You can either go east to wailing woods, north to the block, or west to lazy links",
              "block", None, "wailing", "lazy",)
lazy = Room("LAZY LINKS", "You are at Lazy Links. This place has a mansion and alot of golf course"
                          "You can either go west to pleasant park, or east to the block",
            None, None, "block", "pleasant")
pleasant = Room("PLEASANT PARK", "You are at Pleasant Park. This place is a nice park but isnt pleasant"
                                 "You can go North to junk junction, or south to viking mountain",
                "junk", "viking",)
junk = Room("JUNK JUNCTION", "You are at junk junction.This place is a trash dump and smells really bad"
                             "You can either go south to Pleasant park or east to lazy links",
            None, "pleasant", "lazy")
block = Room("THE BLOCK", "You are at the block.This place is updated every week with player creations"
                          "You can go south to Wailing Woods,or west to lazy links",
             None, "wailing", None, "lazy")
wailing = Room("WAILING WOODS", "You are at Wailing Woods.This place is a calm forest"
                                "You can go south to retail row or west to tomato temple",
               None, "retail", None, "tomato")
fatal = Room("FATAL FIELDS", "You are at Fatal Fields. This place is a nice little farm ranch"
                             "You can west to happy hamlet or north to salty springs",
             "salty", None, None, "hamlet")
hamlet = Room("HAPPY HAMLET", "You are at happy hamlet. Its really cold here but there is a small town"
                              "You can either go west to frosty flights or north to tilted towers",
              "tilted", None, None, "frosty")
frosty = Room("FROSTY FLIGHTS", "You are at frosty flights. There are a few airplane hangars"
                                "You can either go north to viking mountain or east to happy hamlet",
              "VIKING MOUNTAIN", None, "HAPPY HAMLET", None)
viking = Room("VIKING MOUNTAIN""You are at Viking Mountain. This is a lost viking camp on a mountain"
                               "You can either go east to tilted towers, west to snobby shores, north to pleasant park"
                               "or south to frosty flights",
              "pleasant", None, "tilted", "snobby")
tilted = Room("TILTED TOWERS", "You are at Tilted towers. this place is the biggest city on the map"
                               "You can go north to pleasant park,west to viking mountain,or south to happy hamlet",
              "pleasant", "happy", None, "viking")
snobby = Room("SNOBBY SHORES", "You are at Snobby Shores. This place has a few modern apartments"
                               "you can either go east to viking mountain,south to frosty flights,"
                               " or north to junk junction",
              "junk", "frosty", "viking", None)


player = Player(retail)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit' 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I cant go that way")
    else:
        print("Command Not Found")
