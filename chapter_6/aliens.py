# alien_0 = {'color': 'green', 'points': 5,}
# alien_1 = {'color': 'yellow', 'points': 10,}
# alien_2 = {'color': 'red', 'points': 15,}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

#Make an empty list of aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow',}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created
print(f"Total number of aliens is {len(aliens)}")