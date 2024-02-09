# def greet_user(username):
#     """Display a simple greeting to the user."""
#     print(f"Hello, {username.title()}")

# greet_user('jesse')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name.")
    print("enter 'q' at any time to quit")
    f_name = input("What is your first name? ")
    if f_name == 'q':
        break
    l_name = input("What is your last name? ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")