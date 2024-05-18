import requests





# Ask the player for their name. # Choice the size of your name 

print(" Please choice the min & max len of your name")
min_len = input(" Minimun len, choice more than 2 characters ")
max_len = input(" Choice max leng: Max 40 characters ")

URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}"
response = requests.get(URL)

print(f' your name is {response.text}')


player_name = response.text
sword = None 
fight_dragon = None
sword_on = None




# Display a message that greets them and introduces them to the game world.

print(f"""Dungeon & Dragons ! Welcome {player_name}, who has just defied the dragon in his dungeon!
 Go through the dungeon and get the infinity sword to defeat the dragon! Good luck to you """)

# Present them with a choice between two doors.

flag = True



# If they choose the left door, they'll see an empty room.
while flag == True:
    doors_selection = input(" Choose your direction enter left or right ! ")

    if doors_selection == "left":
     
     print(f' You are in the empty room')

     # When in the seemingly empty room, they can choose to look around.
     #  If they do so, they will find a sword. They can choose to take it or leave it.
     level_selection = input("Do you wish to  - look around - or  - to go back ? ")

    #  if level_selection == "B" or "b": 
    #     flag = True
    #     continue
    
    
     if level_selection == "look around" : 
        print(f"Dear {player_name} it's look like, there is sword. ")
        sword_selection = input(" The power of the sword can kill a dragon - Choice A - Take it - or B - Leave it - ")

        if sword_selection in {"A", 'a'}: # "Take it"
            sword = True 
            flag == True
            print(f'Dear {player_name} you are now ready to fight the Dragon, you get the magic sword!')
            #Encouter the dragon 
            if  sword_selection in {"B" or "b"}:  # "Leave it"
                sword = None 
                flag = False
                pass
                # Go back to the two doors. 
    else: pass
     


# If they choose the right door, then they encounter a dragon.

    if doors_selection == "right" :
        
        print(f' This room is guard by the Dragoon. If you want to win, you need to have a sword.')
        fight_dragon = input(" Are you ready to fight, yes or no ? ")
        

# When encountering the dragon, they have the choice to fight it.
        if fight_dragon == "yes" and sword == None:
            print("The dragon is to strong, you die, come back next time with a magic sword! ")
            exit("Game over")

# If they have the sword from the other room, then they will be able to defeat it and win the game.

        if fight_dragon == "yes" and sword == True:
            print(f'You meet the dragon and kill him with your sword! Congratulations {player_name} ')
            exit(f'You win')


# If they don't have the sword, then they will be eaten by the dragon and lose the game.
    if fight_dragon == "no":
        door_selection = None
        level_selection = None
        flag = True 
    pass
        
        
print("im outside of the game")
            
