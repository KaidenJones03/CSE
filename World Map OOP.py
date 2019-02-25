class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


R19A = Room("Mr. Wiebe's Room", "This is mr wiebe's room", 'parking_lot')
parking_lot = Room("Parking Lot", "The parking lot outside", None, "R19A")

retail = Room("RETAIL ROW", "You are at retail row. if you go south you will be at Paradise Palm. \n"
                            "If you go north you will reach tomato temple",
              "tomato_temple", "palms")
palms = Room("PARADISE PALMS", "You are at Paradise Palms. Its very dry here with a lot of mountains"
                               "You can either go north to retail row or west to fatal fields",
             "retail", "fatal")
tomato = Room("TOMATO TEMPLE", "You are at Tomato Temple. This place was a religious sanctuary for tomatoes"
                               "You can either go east to wailing woods, north to the block, or west to lazy links",
              "THE BLOCK", None, "WAILING WOODS", "LAZY LINKS",)

