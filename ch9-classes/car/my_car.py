"""The Car Class"""

from car import Car


class ElectricCar(Car):
    """
    Initializes the parent class.
    And then define attributes specific to electric cars.
    """

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    """Battery model for electric car"""

    def __init__(self, battery_size=75) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a battery size of {self.battery_size}-kWh")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        self.battery_size = 100


my_tesla = ElectricCar("tesla", "model s", 2022)
# print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(23)
# my_new_car.read_odometer_reading()
#
