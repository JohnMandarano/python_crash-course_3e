cities = {
    'tokyo': {
        'country': 'japan',
        'population': 20_000_000,
        'fact': 'has been destroyed by Godzilla several times',
        'been_there': False,
    },
    'new york city': {
        'country': 'unites states',
        'population': 12_000_000,
        'fact': 'is called the Big Apple',
        'been_there': True,
    },
    'scranton': {
        'country': 'united states',
        'population': 100_000,
        'fact': 'was the setting for The Office',
        'been_there': True,
    },
}

print(f"Here is a list of cities.\n")

for city, city_info in cities.items():
    print(f"Here are some things you should know about {city.title()}.")
    for key, value in city_info.items():
        if key == 'country':
            print(f"\t{city.title()} is in {value.title()}.")
        elif key == 'population':
            print(f"\tIt's population is {value}.")
        elif key == 'fact':
            print(f"\t{city.title()} {value}.")
        elif key == 'been_there':
            if value == True:
                print("\tI've been there!")
            else:
                print("\tI've never been there.")
            

