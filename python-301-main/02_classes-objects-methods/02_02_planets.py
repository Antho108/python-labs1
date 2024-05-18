# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    """ Planet descript """
    def __init__(self, name, color) -> None:
        self.name = name 
        self.color = color 
        pass
    
    def SolarSystem(self, solar):
        self.solar = solar

    def Bears_Life(self):
        if self.color == "blue":
            return True
        else: 
            return False

    def __str__(self) -> str:
        return f'{self.name} is in {self.solar} system and its {self.color}'


venus = Planet("Venus", "green")
venus.SolarSystem("sun")
print(venus)


print(venus.Bears_Life())