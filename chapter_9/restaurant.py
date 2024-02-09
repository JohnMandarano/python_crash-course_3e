class Restaurant:
    """A simulation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Assign values"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """For the Zagat's Guide"""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"You can get {self.cuisine_type} food there.")

    def open_restaurant(self):
        """To let people know the restaurant is open."""
        print(f"{self.restaurant_name} is open for business!")

    def set_number_served(self, number_of_customers):
        """Sets the number of customers served in a day."""
        self.number_served = number_of_customers

    def increment_number_served(self, number_of_customers):
        """Increment the number of customers served."""
        self.number_served += number_of_customers

# restaurant = Restaurant('Casa Guido', 'Italian')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
        
joes_diner = Restaurant("Joe's Diner", 'Greasy Comfort Food')
print(joes_diner.number_served)

joes_diner.set_number_served(30)
print(joes_diner.number_served)

joes_diner.increment_number_served(10)
print(joes_diner.number_served)