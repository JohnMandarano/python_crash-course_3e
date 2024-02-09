favorite_places = {
    'garrett': ['taiwan', 'india', 'hong kong'],
    'amy': ['timbuktu', 'ohio', 'chinatown'],
    'veda': ['maine', 'pennsylvania', 'stuffyland'],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}, I know your favorite places are:")
    for place in places:
        print(f"\t{place}")

