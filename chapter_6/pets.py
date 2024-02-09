pets = [
    {
        'name': 'boopsie',
        'kind': 'poodle',
        'owner': 'ken',
    },
    {
        'name': 'oswald',
        'kind': 'penguin',
        'owner': 'jed',
    },
    {
        'name': 'hubert',
        'kind': 'whale',
        'owner': 'leonard',
    },
]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']}, and {pet['owner'].title()}"
          " is their owner.")