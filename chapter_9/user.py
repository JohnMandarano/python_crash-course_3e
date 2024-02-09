class User:
    """Create a model user"""
    def __init__(self, first_name, last_name, user_name, number_of_followers):
        """assign values to attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.number_of_followers = number_of_followers

    def full_name(self):
        """Create a string with user's full name"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def describe_user(self):
        """Give a description of the user"""
        print(f"{self.full_name()}'s user name is {self.user_name}"
              f" and they have {self.number_of_followers} followers.")
        
    def greet_user(self):
        """Print a greeting to the user."""
        print(f"Hello, {self.full_name()}")

radical_mushroom = User('Tom', 'Coolbaugh', 'radical_mushroom', 679)
sexy_panda = User('Lily', 'Tomlin', 'sexy-panda', 9801)

radical_mushroom.describe_user()
radical_mushroom.greet_user()
sexy_panda.describe_user()
sexy_panda.greet_user()
        