def make_shirt(shirt_size='L', shirt_message='I Love Python'):
    message = f"You ordered an {shirt_size} shirt."
    message += f"\nAnd it will say {shirt_message}"
    print(message)

make_shirt()
make_shirt(shirt_size='M')
make_shirt('XL', "I prefer Javascript")