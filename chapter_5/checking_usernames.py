current_users = ['SexySadie69', 'BigFatJohn', 'BubbaGump',
                  'FreakInDaSpreadsheets', 'Fartzilla']
new_users = ['sexysadie69', 'Englebert Humperdinck', 'RamonaQuimby8',
              'Fartzilla', 'LonelyBoy']

to_compare = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in to_compare:
        print(f"The username {new_user.lower()} already exists. Try again")
    else:
        print(f"Welcome aboard, {new_user}!")