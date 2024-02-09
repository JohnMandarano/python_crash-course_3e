def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary with information about an album"""
    album_info = {
        'artist': artist_name,
        'title': album_title,
    }
    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs

    return album_info

# print(make_album('the beatles', 'revolver'))
# print(make_album('prince', 'purple rain', 13))
# print(make_album('the clash', 'london calling'))

while True:
    print("\nPlease give me some information about an album.")

    artist = input("What is the name of the artist? ")
    title = input("what is the album title? ")
    print(make_album(artist, title))

    another_album = input("Would you like to add another album? (yes / no)")
    if another_album == 'no':
        break
