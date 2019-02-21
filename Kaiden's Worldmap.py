world_map = {
    'Battle Bus': {
        'NAME': "Battle Bus",
        'DESCRIPTION':"You are in the battle bus "
                      "Now you can either go North to Retail Row or south to Paradise Palms ",
        'PATHS': {
            'NORTH': "RETAIL ROW",
            'SOUTH': "PARADISE PALMS"
        }
    },
    'RETAIL ROW': {
        'NAME': "RETAIL ROW",
        'DESCRIPTION': "You are at retail row. if you go south you will be at Paradise Palm"
                       "If you go north you will reach tomato temple",
        'PATHS': {
            'SOUTH': "PARADISE PALMS",
            'NORTH': "TOMATO TEMPLE"

        }
    },
    'PARADISE PALMS': {
        'NAME': "PARADISE PALMS",
        'DESCRIPTION': "You are at Paradise Palms. Its very dry here with a lot of mountains"
                       "You can either go north to retail row or west to fatal fields",
        'PATHS': {
            'NORTH': "RETAIL ROW",
            'WEST': "FATAL FIELDS"

        }
    },
    'TOMATO TEMPLE': {
        'NAME': "TOMATO TEMPLE",
        'DESCRIPTION': "You are at Tomato Temple. This place was a religious sanctuary for tomatoes"
                       "You can either go east to wailing woods, north to the block, or west to lazy links",
        'PATHS': {
            'NORTH': "THE BLOCK",
            'WEST': "LAZY LINKS",
            'EAST': "WAILING WOODS"


        }
    },
    'LAZY LINKS': {
        'NAME': "LAZY LINKS",
        'DESCRIPTION': "You are at Lazy Links. This place has a mansion and alot of golf course"
                       "You can either go west to pleasant park, or east to the block",
        'PATHS': {
            'WEST': "PLEASANT PARK",
            'EAST': "THE BLOCK"

        }
    },
    'PLEASANT PARK': {
        'NAME': "PLEASANT PARK",
        'DESCRIPTION':"You are at Pleasant Park. This place is a nice park but isnt pleasant"
                      "You can go North to junk junction, or south to viking mountain",
        'PATHS': {
            'NORTH':"JUNK JUNCTION",
            'SOUTH':"VIKING MOUNTAIN"
        }
    },
    'JUNK JUNCTION': {
        'NAME':"JUNK JUNCTION",
        'DESCRIPTION':"You are at junk junction.This place is a trash dump and smells really bad"
                      "You can either go south to Pleasant park or east to lazy links",
        'PATHS': {
            'SOUTH':"PLEASANT PARK",
            'EAST':"LAZY LINKS"
        }
    },
    'THE BLOCK': {
        'NAME':"THE BLOCK",
        'DESCRIPTION':"You are at the block.This place is updated every week with player creations"
                      "You can go south to Wailing Woods,or west to lazy links",
        'PATHS': {
            'SOUTH':"WAILING WOODS",
            'WEST':"LAZY LINKS"
        }
    },
    'WAILING WOODS': {
        'NAME':"WAILING WOODS",
        'DESCRIPTION': "You are at Wailing Woods.This place is a calm forest"
                       "You can go south to retail row or west to tomato temple",
        'PATHS': {
            'SOUTH':"RETAIL ROW",
            'WEST':"TOMATO TEMPLE"
        }
    },
    'FATAL FIELDS': {
    'NAME':"FATAL FIELDS",
    'DESCRIPTION': "You are at Fatal FIelds. This place is a nice little farm ranch"
                   "You can west to happy hamlet or north to salty springs",
    'PATHS': {
        'WEST':"HAPPY HAMLET",
        'NORTH':"SALTY SPRINGS"
        }
    },
    'HAPPY HAMLET': {
        'NAME':"HAPPY HAMLET",
        'DESCRIPTION':"You are at happy hamlet. Its really cold here but there is a small town"
                      "You can either go west to frosty flights or north to tilted towers",
        'PATHS': {
            'WEST':"FROSTY FLIGHTS",
            'NORTH':"TILTED TOWERS"
        }
    },






}


playing = True
current_node = world_map['Battle Bus']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']


while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit' 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
        current_node = world_map[room_name]
        except KeyError:
        print("I cant go that way")
    else:
        print("Command Not Found")