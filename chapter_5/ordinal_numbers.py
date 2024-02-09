numbers = list(range(1,10))
ordinals = []

for number in numbers:
    if number == 1:
        print("\n1st")
    if number == 2:
        print("\n2nd")
    if number == 3:
        print("\n3rd")
    elif number > 3:
        print(f"\n{str(number)}th")