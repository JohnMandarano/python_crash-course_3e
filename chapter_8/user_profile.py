def build_profile(first, last, **user_info):
    """Build a dictionary using everything we know about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')

user_profile = build_profile('john', 'mandarano',
                             location='maine',
                             music='eclectic',
                             condition='dog shit awareness')

print(user_profile)

# def build_dictionary(**dict_info):
#     return dict_info

# experimental = build_dictionary(name = 'John', game='nonduality')
# print(experimental)