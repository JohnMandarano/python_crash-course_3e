places = []

places.append("bora bora")
places.append("angkor wat")
places.append("uluru")
places.append("sea of tranquility")
places.append("grand canyon")

print(places)

cant_go = places.pop(3)
print(f"You can't go to {cant_go}, You don't own a rocket ship.")

print(sorted(places))
print(sorted(places, reverse=True))

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)

next_place = 'grand canyon'
places.remove(next_place)
print(places)
print(f"\nNext stop, {next_place}!")



