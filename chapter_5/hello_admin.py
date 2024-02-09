users = ['bert', 'ramona', 'craig', 'andy', 'ramit', 'admin']
#users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello, you big, sexy {user.title()}.")
        else:
            print(f"oh, it's just you, {user.title()}.")

else:
    print("We need to find some users!")
