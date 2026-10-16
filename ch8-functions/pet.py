"""
This is pet.py
"""

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet("dog", "michael")
describe_pet(pet_name="michael")



