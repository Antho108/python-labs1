# # Use your `Ingredients` class to create a URL to an online search
# # that allows to look for recipes for dishes made from the
# # available ingredients.

# Implement the Ingredient() class, where each ingredient has at least a .name and an .amount attribute.
# Add an instance method called .get_info() that takes the .name attribute of an Ingredient() and creates a Wikipedia URL.
# The .get_info() method should then automatically open the corresponding Wikipedia page in your web browser:
import webbrowser

class Ingredient:

    """Models a food item used as an ingredient."""
   
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def getinfo(self):
         webbrowser.open(f'https://en.wikipedia.org/wiki/{self.name}')
       
    
    def __str__(self) -> str:
        return f'{self.name} {self.amount}'

  


carrot = Ingredient("Carrot", 25)
carrot.getinfo()
print(carrot)

tomatoes = Ingredient("Tomatoes", 35)
tomatoes.getinfo()
print(tomatoes)


