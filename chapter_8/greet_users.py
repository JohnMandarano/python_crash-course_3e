def greet_users(names):
    """Print a simple greeting to each user in a list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'bert']
greet_users(usernames)
