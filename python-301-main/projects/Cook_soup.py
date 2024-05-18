# Cook soup https://platform.codingnomads.co/learn/mod/page/view.php?id=6631

# For this project, you'll create a custom Soup() class that can take Ingredient() and Spice() objects, 
# and use them to look up soup recipes on the Internet.

# Your Soup() objects should at least be able to:

# take an unlimited number of Ingredient() or Spice() objects during instantiation
# have a .cook() method that returns a search result for a soup recipe using all the added ingredients

# Info: Revisit the lessons on *args and **kwargs from the previous module, 
# and use concepts you learned when building your Ingredient() lookup in the previous section.

# When you're done with this functionality, you can continue to extend this project in a couple of ways, for example:

# take the amount of each Ingredient() into account. How can you work that into creating a recipe the user can actually cook?
# interface with a recipe API instead of concatenating a web search URL. Receive the API response data, format it, and display it as command-line output.
# create child classes to Soup() that have specific qualities.


import webbrowser

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
    



class Soup():
        
        toto = []

        def __init__(self, name, *ingredient, **spice):
            self.name = name 
            self.ingredient = ingredient
            self.spice = spice


        def cook(self):
            
           ingredient_names = [str(i).split(" ")[-1] for i in self.ingredient]
           ingredients_joints = "".join(ingredient_names).replace(".", " ")
           print(ingredients_joints)
           return webbrowser.open_new_tab(f"https://duckduckgo.com/?q=soup+{ingredients_joints}")
           

        def __str__(self) -> str:
            return f'{self.name} soup contains: {" ".join(str(i) for i in self.ingredient)}'
       
        

   
    

# Creer plusieurs ingredients. 
a = Ingredient("Apple", 10)
b = Ingredient("Banane", 27)
c = Ingredient("Carrot", 70)
d = Spice("Tumeric", 25)
e = Spice("Saltz", 45)

beautiful_soup = Soup("Nice_soup", a, e)
# print(beautiful_soup)


carrot_soup = Soup("Carrot_soup", Ingredient("Banane", 27), Ingredient("Carrot", 70), Ingredient("Apple", 10), Spice("Saltz", 45), Spice("Tumeric", 25))
# print(carrot_soup)


# test_soup = Soup("test_soup", [a, b, c], [d,e])
# print(test_soup)

carrot_soup.cook()
beautiful_soup.cook()