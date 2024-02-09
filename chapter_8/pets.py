def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet(animal_type='dog', pet_name='willie')
# describe_pet(pet_name='snowball', animal_type='guinea pig')
    
describe_pet(pet_name='willie')