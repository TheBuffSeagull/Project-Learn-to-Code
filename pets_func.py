def describe_pet(pet_name, animal_type= 'dog'):
    """Display information abouty a pet."""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie
describe_pet(animal_type ='hampster', pet_name = 'harry')
# A hamster named Harry
describe_pet(pet_name = 'willie') # we dont have to specify since we added a default in line 1
                                # we also dont have put pet_name