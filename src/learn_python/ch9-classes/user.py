"""Exercise 9-3 Users"""

import random


def greet_user(user: User):
    random_formats = [
        f"Howdy! {user.first_name}",
        f"Sup, {user.last_name}",
        f"Looking good! {user.first_name} {user.last_name}.",
    ]

    print(random_formats[random.randint(0, len(random_formats) - 1)])


class User:
    def __init__(self, first_name, last_name, followers=0, is_active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.followers = followers
        self.is_active = is_active

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} has {self.followers} followers.")

    def greet_user(self):
        greet_user(self)


class Admin(User):
    """Class for admins."""

    def __init__(self, first_name, last_name, followers=0, is_active=True):
        super().__init__(first_name, last_name, followers, is_active)
        self.privileges = Privileges()

    def show_privileges(self):
        for privilege in self.privileges.privileges:
            print(f"{privilege}")


class Privileges:
    """A class for privileges"""
    def __init__(self, privileges=["can add post"]):
        self.privileges = privileges


new_admin = Admin("Michael", "You")
new_admin.show_privileges()

# user_1 = User("Michael", "Jackson", 30000)
# user_2 = User("Eric", "Clapton")
#
# user_1.describe_user()
# user_2.describe_user()
#
# user_1.greet_user()
# user_2.greet_user()
