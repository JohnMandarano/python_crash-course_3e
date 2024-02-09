favorite_numbers = {
    'veda' : [8],
    'sun ra' : [88, 44, 11],
    'john' : [11, 23, 37, 41],
    'amy' : [37, 0, 9],
    'jan' : [5, 7],
}

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}, your favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
