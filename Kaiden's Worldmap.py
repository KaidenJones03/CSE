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
                      ""
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