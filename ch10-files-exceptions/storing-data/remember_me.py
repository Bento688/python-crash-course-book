import json
from pathlib import Path


def get_stored_user(path: Path):
    """Get stored user if available"""
    if path.is_file() and len(path.read_text()) > 0:
        content = path.read_text()
        return json.loads(content)
    else:
        return None


def get_new_user(path: Path):
    """Store new user if there isn't one"""
    user_dict = {}
    username = input("What is your name? ")
    age = input("What is your age? ")
    sex = input("What is your sex? ")
    new_user = {"username": username, "age": age, "sex": sex}
    user_dict = {**new_user}

    dict_str = json.dumps(user_dict)
    path.write_text(dict_str)

    return user_dict["username"]


def greet_user():
    """Greet a user by name or ask for their name on first try."""
    path = Path("user.json")

    user_dict = get_stored_user(path)
    if user_dict:
        print(f"Hello! {user_dict["username"]}! Good to have you back!")
        print(f"You are {user_dict["age"]} years old!")
        print(f"You are a {user_dict["sex"]}!")
    else:
        username = get_new_user(path)
        print(f"We will remember you next time, {username}!")


greet_user()
