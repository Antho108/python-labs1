# # For this project, you should use OOP techniques to create 
# # a text-based command-line interface role-playing game or update your existing CLI game.

# Task Instructions
# Build a text-based role-playing game that has at least two classes:

# Hero(): the protagonist of your game that the player controls and identifies with. There should be only one hero.
# Opponent(): the challengers that the player meets throughout the gameplay. There should be multiple opponents.
# The hero should encounter multiple opponents of different strengths or levels. They should be able to perform different actions when meeting an opponent. 
# These actions should be at a minimum:

# attack
# or run away
# If the Hero chooses to attack, the program decides through a simulated dice throw that takes the current level into account, 
# whether the hero or the opponent wins this round:

# Rolling dice 

# Also implement consequences for winning and losing, e.g. forcing the hero to wait 
# a few seconds before continuing the game in case they lose. Or removing the opponent from the opponent pool in case the hero wins.

# Note: This project can be challenging. Push yourself to complete it and synthesize your learning by applying your knowledge practically. If you have questions, remember to post to your forum.
# You'll have to implement both attributes and methods for both of your classes. Think about what you'll need so you can model the described functionality. Map out the project before you start coding.

# Hints
# There is a small Python RPG Game available on GitHub, that implements the described tasks. It allows you to safely defuse your digital rage against Paywalls, PHP, and even Wordpress sites! You can look at the code to get some inspiration.

# However, I strongly suggest that you think about it deeply first and that you build your own idea. Translating ideas into code by yourself is an incredibly useful technique to facilitate your learning, and working on something that you are interested in makes coding more fun.




# Ce hero il peut interargir : soit il attaque, soit il run away. 
# Si il attaque simulation de lancement de des. Combat avec la classe opposante. 
# A l'isue de la confrontation, leverl +, vie - 



# Hero(): the protagonist of your game that the player controls and identifies with. 
# There should be only one hero

import random

class Hero():

    def __init__(self, name, level, attack):
        self.name = name 
        self.level = level 
        self.attack = attack

    def run_away(self): 
        pass 
    
    def battle(self, other):  
        print(f'{self.name} fights {other.name} ')
        
        # Determine the wiiner 
        random_num = random.randint(0, 7)
        self.hand = random_num * self.level
        other.hand = random_num * other.level
       
        print(f'{self.name} gets a {self.hand} with his {self.attack}')
        print(f'{other.name} gets a {other.hand} with his {other.attack}')

        if self.hand >= other.hand : 
            result = "win"
            self.level += 15
            print(f'Congratulations {self.name} you win one level. Your level is now {self.level} ')  

        else: result = "defeat"
        print(f' Reuslt is === {result} === for {self.name}')
    

    def __str__(self) -> str:
        return f' Your Hero is {self.name}, its special attack is : {self.attack} and his level is {self.level}'
   


#  Opponent(): the challengers that the player meets throughout the gameplay.
class Opponent():

    def __init__(self, name, level, special_attack) -> None:
        self.name = name 
        self.level = level  
        self.attack = special_attack 

    def __str__(self) -> str:
        return f' Crazy Opposant :  {self.name}, level : {self.level}'

   
class SmallOpponent(Opponent):

    def __init__(self, name, level, special_attack) -> None:
        super().__init__(name, level, special_attack)

    def __str__(self) -> str:
        return f' Little Opposant :  {self.name}, low level : {self.level}'
    
class Boss(Opponent): 

    def __init__(self, name, level, special_attack) -> None:
        super().__init__(name, level, special_attack)

    def __str__(self) -> str:
        return f' Big Boss  :  {self.name}, Too High Level : {self.level}'
    



# Welcome message! 
def Welcome(): 
    
    rules = """It's a pleasure to meet you, traveller. You can create your hero and choose a special 
    attack as well as a name, then join the labyrinth of the dead who kill.
    You will have the opportunity to face many opponents and to increase your level!
    When you have defeated every hero, you will be victorious. Strength & Honor! Never give up, 
    no matter how difficult it may seem to reach the big boss"""
    print(rules)
    pass


# # Starting the games
# def game():
       
#     Welcome()

#     # Creation hero 
#     name_hero = input("What is your name Hero ? ")
#     attack_hero = input("Wich Attack do you want ? ")
#     player_hero = Hero({name_hero}, 50, {attack_hero}) 

#     #  There should be multiple opponents.
#     opponents = [
#             Opponent("Hot_dog", 10, "Magnun_108"),
#             Opponent("Carambar_the caramel killer", 500, "Sugar_rayon") ,
#             Opponent("Mozza", 5, "Hard_slice"),
#             Opponent("Chapati", 48, "Roti_punch"),
#             Opponent("Big Mac", 100, "Burger_explosion"),
#             Opponent("Roquefort", 325, "Bad_smell"), 
#             Opponent("Croissant", 1000, "Too_good_for_you"), ]

#     small_opponents = [

#             SmallOpponent("Crayon", 15, "Pen"),
#             SmallOpponent("Chewing Gum", 5, "Hollywood"),
#             SmallOpponent("Sanjit", 1, "RedFire"),
#     ]


#     boss = Boss("Pikkle", 200000, "Death")

    
   

#     while True: 
#             cmd = 2 
#             current_opponent = random.choice(opponents)

#             print(f'Your next opponent is {current_opponent}')
#             print("What actions you would like to do ? ")
#             move = input("1: [Attack],  2: [Run away], 3: [Look around] ")

#             if move not in {'1', '2', '3', 'exit'}:
#                 print("Please enter number 1, 2, 3 for good selection")
#                 print('If you fear and wish to exit the games, tape exit')
            
#             # Quit games
#             if move in {'exit', 'EXIT', 'Exit'}:
#                 print('See you next time! Train yourself!')
#                 exit()
            
            
#             if move in {"1"}: # The battle start!
                
#                 opponents.remove(current_opponent)
#                 player_hero.battle(current_opponent)
      
#             pass
      
        
#             if move in {"2"} :
            
#               print("Nice you are in a secure zone and rest for a while")  
#               print("You are rested and come back in the fight")
#               print("Do you wish to train yourself versus low opponent ? ")
            
#               cmd = input(" 1: Yes  2: No ")

#             if cmd in {"1"}: 
#                     small_opponent = random.choice(small_opponents)
#                     print(f'Your next opponent is {small_opponent}')
#                     print("What actions you would like to do ? ")
#                     move_small = input("1: [Attack],  2: [Run away], 3: [Look around] ")
                    
#                     if move_small in {"1"}: # The battle start!
                    
#                         small_opponents.remove(small_opponent)
#                         player_hero.battle(small_opponent)

#                     pass

#             if cmd in {"2"}: 
#                      pass

#             pass

#             if move in {"3"}: 

#                 for x in range(len(opponents)):
#                   print(opponents[x])
                  
#             pass
    

   
#             if opponents == []: 
#                 boss_opponent = boss
#                 print(f'***************** BIG BOSS ******************')
#                 print(f'Your next opponent is {boss_opponent}')
#                 player_hero.battle(boss_opponent)
                

#             if opponents == []: 

#                 print(f' Your hero have reach level {player_hero.level}')
#                 print("You fight again all the opponents, congratulations !!!")
#                 last_round = input("Do you want  1 : [New_game] or 2 : [Exit] ? ")

#                 while last_round not in ['1', '2', 'Exit', 'exit']:
#                     last_round = input("Do you want  1 : [New_game] or 2 : [Exit] ? ")

#                 if last_round == "2": 
#                     exit()
                    
#                 if last_round == "1":
#                     game()
                    
                
#                 exit()
            
          

# game()


def game():
    Welcome()

    # Create hero
    name_hero = input("What is your name Hero? ")
    attack_hero = input("Which attack do you want? ")
    player_hero = Hero(name_hero, 50, attack_hero)

    # Create opponents
    opponents = [
        Opponent("Hot_dog", 10, "Magnun_108"),
        Opponent("Carambar_the caramel killer", 500, "Sugar_rayon"),
        Opponent("Mozza", 5, "Hard_slice"),
        Opponent("Chapati", 48, "Roti_punch"),
        Opponent("Big Mac", 100, "Burger_explosion"),
        Opponent("Roquefort", 325, "Bad_smell"),
        Opponent("Croissant", 1000, "Too_good_for_you")
    ]

    small_opponents = [
        SmallOpponent("Crayon", 15, "Pen"),
        SmallOpponent("Chewing Gum", 5, "Hollywood"),
        SmallOpponent("Sanjit", 1, "RedFire")
    ]

    boss = Boss("Pikkle", 200000, "Death")

    while True:
        current_opponent = random.choice(opponents)

        print(f'Your next opponent is {current_opponent}')
        while True:
            player_choice = input("What action would you like to take? 1: [Attack], 2: [Run away], 3: [Look around], exit: [Quit game] ")

            if player_choice == "1":
                opponents.remove(current_opponent)
                player_hero.battle(current_opponent)
                break

            elif player_choice == "2":
                print("You are in a secure zone and can rest for a while.")
                print("You are rested and can come back to fight.")
                print("Do you wish to train yourself versus a weaker opponent?")
                while True:
                    cmd = input("1: [Yes], 2: [No] ")
                    if cmd == "1":
                        small_opponent = random.choice(small_opponents)
                        print(f'Your next opponent is {small_opponent}')
                        while True:
                            move_small = input("What action would you like to take? 1: [Attack], 2: [Run away],                            3: [Look around], exit: [Quit game] ")

                            if move_small == "1":
                                small_opponents.remove(small_opponent)
                                player_hero.battle(small_opponent)
                                break

                            elif move_small == "2":
                                print("You run away and continue resting.")
                                break

                            elif move_small == "3":
                                for x in range(len(small_opponents)):
                                    print(small_opponents[x])
                                continue

                            elif move_small == "exit":
                                print('See you next time! Train yourself!')
                                exit()

                            else:
                                print("Please enter number 1, 2, 3 for a valid selection.")
                                continue

                        break

                    elif cmd == "2":
                        break

                    else:
                        print("Please enter number 1 or 2 for a valid selection.")
                        continue

                break

            elif player_choice == "3":
                for x in range(len(opponents)):
                    print(opponents[x])
                continue

            elif player_choice == "exit":
                print('See you next time! Train yourself!')
                exit()

            else:
                print("Please enter number 1, 2, 3 for a valid selection.")
                continue

        if not opponents:
            boss_opponent = boss
            print(f'***************** BIG BOSS ******************')
            print(f'Your next opponent is {boss_opponent}')
            player_hero.battle(boss_opponent)

            print(f' Your hero have reached level {player_hero.level}')
            print("You have fought against all the opponents, congratulations!!!")
            last_round = input("Do you want to play again? 1: [New game], 2: [Exit] ")

            while True:
                if last_round == "2" or last_round.lower() == "exit":
                    print('See you next time! Train yourself!')
                    exit()

                elif last_round == "1":
                    game()

                else:
                    last_round = input("Please enter number 1 or 2 for a valid selection. ")
                    continue

        pass


game()





# # Create a hero 
# def Creation_hero():
#     name_hero = input("What is your name Hero ? ")
#     attack_hero = input("Wich Attack do you want ? ")
#     player_hero = Hero({name_hero}, 50, {attack_hero})  
#     # player_hero = Hero("toto", 50, "test")
#     return player_hero  

