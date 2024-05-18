# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

class Pokemon(): 

    def __init__(self, name, primary_type,  max_hp) -> None:
        self.name = name 
        self.primary_type = primary_type
        self.hp = max_hp 
        self.max_hp = max_hp 
        
    # Feed my pokemon 
    def feed(self): 
    # Dans cette fonction, je souhaite pouvoir l'appeller pour que mon pokémon sois feed et regane de la vie
        # self.hp = self.hp + 30 
    # Comment faire pour bloquer le hp de mon pokemon à 100 
        if self.hp < self.max_hp : 
            self.hp += 5
            print (f"Your {self.name} gain 5 pv and have {self.hp} HP")
        else:
            print("Your pokemon is full life")

    #make them battle and decide winner
    def battle(self, other):  
      
     print(f'Battle {self.name} and {other.name}')
     result = self.typewheel(self.primary_type, other.primary_type)
     print(f' {self.name} fights {other.name} and he {result}')
     if result == "lose":
        self.hp -=20
        print(f' {self.name} have now {self.hp} HP')
      
    # witch type wil win
    @staticmethod
    def typewheel(type1, type2): 
        result = {0: "lose", 1: "win", -1: "draw"}
        # mapping between types and win condition 
        games_maps = {"water": 0, "fire": 1,"grass": 2}
        #implement win-lose matrix 
        wl_matrix = [
                [-1, 1, 0], # water 
                [0, -1, 1], # fire
                [1, 0, -1], # grass 
        ]

        # declare a winner 
        
       
        wl_result = wl_matrix[games_maps[type1]][games_maps[type2]]
        return result[wl_result]
        pass 


    def __str__(self) -> str:
        return f' Your pokemon is {self.name} of type : {self.primary_type} and his max_hp is {self.max_hp}. Current HP is {self.hp}'


c = Pokemon("Raoul", primary_type="grass", max_hp=100)
d = Pokemon("Blanca", primary_type="fire", max_hp = 2000)
# e = Pokemon("George", "water", 250, 100 )

c.battle(d)


