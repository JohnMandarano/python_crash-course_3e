#Create a list of unfinished sandwiches
#And a list of finished sandwiches to which they can be transferred.
unfinished_sandwiches = ['tuna', 'pastrami', 'reuben', 'ham and cheese',
                          'pastrami', 'grilled cheese', 'pastrami']
finished_sandwiches = []

print("We have no pastrami today.")
while 'pastrami' in unfinished_sandwiches:
    unfinished_sandwiches.remove('pastrami')

while unfinished_sandwiches:
    current_sandwich = unfinished_sandwiches.pop()
    print(f"I am making your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nHere are the sandwiches I have made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} Sandwich")