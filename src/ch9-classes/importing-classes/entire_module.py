import car
from electric_car import ElectricCar as EC

my_beetle = car.Car("volkswagen", "beetle", 1960)
print(my_beetle.get_descriptive_name())

my_tesla = EC("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())
