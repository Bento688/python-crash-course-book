import json
from pathlib import Path

def get_stored_number(path: Path):
    if path.is_file():
        try:
            number = int(json.loads(path.read_text()))
            return number
        except Exception as e:
            print(f"Invalid value!: {str(e)}")
            return None

def ask_for_number(path: Path):
    """Store new number if there isn't one"""
    number = int(input("What is your favorite number? "))
    path.write_text(json.dumps(number))
    return number

def favorite_number():
    """Spell out the user's favorite number if available"""
    path = Path("fav_number.json")
    number = get_stored_number(path)

    if number:
        print(f"Your favorite number is {number}!")
    else:
        ask_for_number(path)
        print(f"{number} it is!")

favorite_number()

