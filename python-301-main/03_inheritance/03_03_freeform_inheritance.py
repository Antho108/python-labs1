# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.


class Restaurant() :  

    def __init__(self, name, type,):
        self.name = name 
        self.type = type 
        pass
    
    def menu(self):
        print(f'This restaurant have a normal menu')

    
    def __str__(self):
        return f"This restaurant is {self.name} and have a menu {self.type} "


class Gourmet(Restaurant): 
    
    def menu(self):
        print(f'This restaurant have a gourmet menu whaou!')
        self.name = "Gourmet" + self.name
    pass 

    def __str__(self):
     return f"This restaurant is {self.name} and have a menu {self.type} "

class FastFood(Restaurant): 
    
    def __init__(self, name, type, delivery):
        super().__init__(name, type)
        self.delivery = delivery
    pass

    def menu(self): 
        print(f'This restaurant have a junk menu')
    pass

        
    def __str__(self):
        return f"This restaurant is {self.name} and have a menu {self.type} and delivery is {self.delivery}"

mcdo = FastFood("McDo", "fastfood", "yes")
# print(mcdo)

bert = Gourmet("Seafood", "Gourmet")


mcdo.menu()
bert.menu()

print(bert)