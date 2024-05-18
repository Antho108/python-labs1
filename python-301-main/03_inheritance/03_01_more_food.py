# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")



class Vegetables(Ingredient):

    def prepare(self):
        print(f"You have {self.amount} {self.name} ready to be cook ")
    
    def expire(self):
        if self.name == "ognion" :
            print(f'Remove bad skin ')
        else : 
            print(f"your {self.name} has expired. Drop it to the trash")
            self.name = "Trash " + self.name    
    
    pass


c = Ingredient("Tomatoes", 46)
print(c)