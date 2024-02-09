# create an empty dictionary to store names and response
# and a flag to loop polling
vacations = {}
polling_active = True

while polling_active:
    #Take inputs to create the keys and values
    name = input("\nWhat is your name? ")
    response = input("\nWhere would you go on your dream vacation? ")

    #Add name and response to dictionary
    vacations[name] = response

    prompt = input("Would someone else like to take the poll? (yes/no) ")
    if prompt == 'no':
        polling_active = False

print("\nHere is where people would take their dream vacations:")
for name, response in vacations.items():
    print(f"\n{name.title()} would go to {response.title()}")