# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


class Players():
    """ Create your players """

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality 

    
    def __str__(self):
        return f"{self.name} ({self.nationality})"

class Teams(): 
    """ Teams of players """

    def __init__(self, name, color):
        self.name = name
        self.color = color

        
    def __str__(self):
        return f"{self.name} ({self.color}) ({self.nationality})"

    
class League(): 
    """ League of the players """
    def __init__(self, name, country):
        self.name = name
        self.country = country 

            
    def __str__(self):
        return f"{self.name} ({self.country})"



toto = Players("Toto", 20, "French")
toto = Teams("Psg", "blue")

print(toto)


