# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

import unittest

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

class MyFirstTest(unittest.TestCase): 
    
    # Test expire function it's work!
    def test_expire(self):
        coco = Ingredient("coco", 24)
        coco.expire()
        self.assertEqual(coco.name, "expired coco")

    # Test the amount of ground tumeric
    def test_grind_prepare(self):
        tume = Spice("Tumeric", 400)
        tume.grind()
        self.assertEqual(tume.amount, 400)

    # Test le output de la fonction STR
    def test_output_str(self):
        self.coco = Ingredient("coco", 24)
        actual_output = str(self.coco)
        excpeted_output = "You have 24 of coco"
        self.assertEqual(actual_output , excpeted_output)


c = Ingredient("Carrot", 24)
c.expire()



