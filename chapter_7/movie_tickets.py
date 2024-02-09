prompt = "Please enter your age to determine the ticket price: "
prompt += "\nIf you do not need any further tickets, please enter 'quit'. "

age = ""

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("\nYour ticket is free.")
    elif 3 <= age <= 12:
        print("\nYour ticket will cost $10.")
    else:
        print("\nYour ticket will cost $15.")
        