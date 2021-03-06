users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'priceton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'london',
    }
}

for username, user_info in users.items():
    print(f"\nusername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")