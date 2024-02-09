party_size = input("How many people are in your party tonight? ")
party_size = int(party_size)

if party_size >= 8:
    print("You will have to wait until we have a table available.")
else:
    print("I have a table ready. Come this way!")