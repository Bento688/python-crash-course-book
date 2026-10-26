import privileges
from user import User

new_admin = privileges.Admin("Michael", "You")

user_1 = User("Michael", "Jackson", 30000)
user_2 = User("Eric", "Clapton")

user_1.describe_user()
user_2.describe_user()

user_1.greet_user()
user_2.greet_user()
