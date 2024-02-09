pizzas = ['taco', 'hotwing', 'gas station', 'hawaiian', 'greek']

for pizza in pizzas:
    print(f"I love {pizza.title()} pizza.")

print("\nThere are many kinds of pizza, and I love them all.\n")

print("The first three items in the list are:")
print(pizzas[:3])

print("The middle three items are")
print(pizzas[1:4])

print("the final three items are")
print(pizzas[2:])

friend_pizzas = pizzas[:]
pizzas.append('meatball')
friend_pizzas.append('steak and cheese')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())