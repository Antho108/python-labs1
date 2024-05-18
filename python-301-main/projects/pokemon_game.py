# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
        # water > fire 
        # warer = water 
        # water < grass 

        # fire > grass
        # fire = fire 
        # fire < water 

        # grass > water 
        # grass = grass 
        # grass < fire 
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

import random 

class Pokemon(): 

    def __init__(self, name, primary_type,  max_hp, hp) -> None:
        self.name = name 
        self.primary_type = primary_type
        self.hp = hp 
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

        
            

          
        

#     # call the function determine_winner to figure out who won
# def battle(my_pokemon, computer_hand) :
#      # 0 = scissor, 1 = rock, 2 = paper
#     outcomes = {('fire', 'fire'): "Draw",
#              (0, 1): "Defeat", 
#              (0, 2): "Victory ", 
#              (1, 1): "Draw",
#              (1, 0): "Victory", 
#              (1, 2): "Defeat", 
#              (2, 0): "Defeat", 
#              (2, 1): "Victory",
#              (2, 2): "Draw"}
#     return outcomes[(my_pokemon, computer_hand)]


    
    # Function declaration 
        def get_hand(hand):
    # 0 = water, 1 = fire, 2 = grass
         my_hand = ('Water', 'Fire', 'Grass')
         return my_hand[hand]


    def __str__(self) -> str:
        return f' Your pokemon is {self.name} of type : {self.primary_type} and his max_hp is {self.max_hp}. Current HP is {self.hp}'


################ Welcome to Pokemon Games ###########
player_name = str(input('What is your name? '))

print(f' Welcome {player_name} please create your pokemon and get ready for the battle! Wahou!!!')

#### Pokemon creation #### 
name_pokemon = input('Name of your pokemon ? ')
primary_type = input(' Choice a primary type : fire, water or grass ')
max_hp_pokemon = 100
hp_pokemon = 40

name_pokemon = Pokemon(name_pokemon, primary_type, max_hp_pokemon, hp_pokemon)
# print(name_pokemon)


#### Computer pokemon ###
 # Generate a random number 0-2 to use for the computer's hand
computer_hand = random.randint(0, 2)
# print(computer_hand)


#### Feed them ####
name_pokemon.feed()
print(name_pokemon)