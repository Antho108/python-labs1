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


class Spices(Ingredient): 

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste 
    
    def expire(self):
        if self.name == "salt" :
            print(f'Salt never expire')
        else : 
            print(f"your {self.name} has expired. it's probably still good.")
            self.name = "old " + self.name
     

    def grind(self): 
        print(f'You have now {self.amount} of ground {self.name}')
    
    def hacher(self): 
        print(f'You have now {self.amount} of hacher {self.name}')  
    pass

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

s = Spices('jojo', 200, "so hot")
p = Ingredient('salt', 42)
j = Vegetables('ognion', 100 ) 

j.prepare()
j.expire()
print(s)
print(j)
print(s.taste)
p.taste