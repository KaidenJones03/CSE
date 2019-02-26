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

        def move(self, new_location):
            """

            :param new_location: The room object of which you are
            :return:
            """
            self.current_location = new_location


def find_next_room(direction):
    """This method searches the current room so ee if a room exists in that direction

    :param direction: The direction that you want to move to
    :return: The room object if it exists, or None if it doe
    """
    return getattr(self.current_location, direction)
# option 1 define as we go
R19A = Room("Mr. Wiebe's Room", "This is mr wiebe's room", 'parking_lot')
parking_lot = Room("Parking Lot", "The parking lot outside", None, "R19A")

player = Player(R19A)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
while playing:
    print(Player.current_location.name)
    print(current_location.description)
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
            print(" Command not found")
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I cant go that way")
    else:
        print("Command Not Found")


retail = Room("RETAIL ROW", "You are at retail row. if you go south you will be at Paradise Palm. \n"
                            "If you go north you will reach tomato temple",
              "tomato_temple", "palms")
palms = Room("PARADISE PALMS", "You are at Paradise Palms. Its very dry here with a lot of mountains"
                               "You can either go north to retail row or west to fatal fields",
             "retail", "fatal")
tomato = Room("TOMATO TEMPLE", "You are at Tomato Temple. This place was a religious sanctuary for tomatoes"
                               "You can either go east to wailing woods, north to the block, or west to lazy links",
              "THE BLOCK", None, "WAILING WOODS", "LAZY LINKS",)

