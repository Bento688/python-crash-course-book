"""Set of classes for extended user behaviors."""

from user import User


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
