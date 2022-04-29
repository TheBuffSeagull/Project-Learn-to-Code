def build_profile(first, last, **user_info): # "**" accepts items as new dictionary items rather than a tuple
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                            location = 'princeton', 
                            field = 'physics')
print(user_profile)
