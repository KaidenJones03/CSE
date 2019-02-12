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
        'NAME': "RETAIL ROw",
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






        },

    }
