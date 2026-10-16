"""Car class to be imported."""


class Car:
    def __init__(self, make, model, year):
        "Intializes attributes to describe a car."
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer_reading(self):
        """Return the odometer reading of a Car instance."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Increments the amount of the odometer_reading by mileage."""
        if mileage < self.odometer_reading:
            print("You cannot roll back an odometer!")
        else:
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles
