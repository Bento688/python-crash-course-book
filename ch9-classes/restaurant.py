"""Exercise 9-1 Restaurant"""

from typing import List


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} cooks {self.cuisine_type} food!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors: List[str], cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors: List[str] = flavors

    def show_flavors(self):
        print(f"Here are the flavors!")
        for flavor in self.flavors:
            print(f"{flavor}")


new_restaurant = Restaurant("Mack Donholds", "American")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

ice_cream_stand = IceCreamStand("Rick's Ice Cream", ["Vanilla", "Chocolate"])
ice_cream_stand.show_flavors()
