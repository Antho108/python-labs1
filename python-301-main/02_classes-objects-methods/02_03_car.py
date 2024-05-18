# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.


class CarModel():
    """Create the best car in the world please. 
    """
    def __init__(self, name, year, max_speed) -> None:
        self.name = name 
        self.year = year 
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 5

    def __str__(self) -> str:
        return f'the car is {self.name}, built in {self.year}, max speed is {self.max_speed}'



volvo = CarModel("Volvo", 1990, 100)
print(volvo)
volvo.increase_speed()
print(volvo)

ferrari = CarModel("Formula1", 1950, 350)
print(ferrari)
ferrari.increase_speed()
print(ferrari)