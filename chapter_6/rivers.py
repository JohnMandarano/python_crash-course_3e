rivers = {
    'kennebec' : 'maine',
    'susquehanna' : 'pennsylvania',
    'colorado' : 'colorado',
    'rio grande' : 'texas',
    'missisipi' : 'missisipi',
}

for river, state in rivers.items():
    print(f"The {river.title()} runs through the state of {state.title()}")

for river in rivers.keys():
    print(river.title())

for state in rivers.values():
    print(state.title())