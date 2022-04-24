favorite_lanaguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_lanaguages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.\n")

print("\n")

# languages used so far
for language in set(favorite_lanaguages.values()): # <---- set pulls all non duplicates from a dictionary 
    print(language.title())

print("\n")

#names
for name in favorite_lanaguages.keys(): # keys is not required as the output will be the same
    print(name.title())

print("\n")

# values in dictionary
for name in favorite_lanaguages.values(): # <---- values 
    print(name.title())

print("\n")

