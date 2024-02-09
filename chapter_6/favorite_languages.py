favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'javascript',
    'emile' : 'python',
}

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

#for name in favorite_languages:
#    print(name.title())

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in sorted(favorite_languages.keys()):
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"{name.title()}, I know your favorite language is {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print("\t" + language.title())

# invited_to_poll = ['sarah', 'phil', 'jerry', 'adam', 'lou ann']

# for name in invited_to_poll:
#     if name in favorite_languages.keys():
#         print(f"Thank you for taking our poll, {name.title()}.")
#     else:
#         print(f"Would you like to take our poll, {name.title()}?")

favorite_languages = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['javascript', 'c#'],
    'emile' : ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language}")