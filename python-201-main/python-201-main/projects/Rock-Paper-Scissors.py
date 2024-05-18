# Rock-Paper-Scissors Game
# Code a game of rock paper scissors.

# Instructions

# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner



# Some Tips

# Creating a function that gets a "hand" based on a number.
# The function should take in a number and return the string representation of the hand. E.g.:
# def get_hand(hand):
#     # 0 = scissor, 1 = rock, 2 = paper

#     # for example if the variable hand is 0, it should return the string "scissor"
#     pass

# ---------------------------------------------------------------------------------------------

# One thing you could add is a loop to continue the game if the user wanted. 
# If you did that, you could also keep track of how many wins, losses, and draws they had.


# ---------------------------------------------------------------------------------------------

# Module for random number 
import random

# Function declaration 
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    # for example if the variable hand is 0, it should return the string "scissor"
    if hand == 0 :
        return 'Scissor'
    if hand == 1 :
        return 'Rock'
    if hand == 2 : 
        return 'Paper'  
    pass

# call the function determine_winner to figure out who won
def determine_winner(player_hand, computer_hand) :
     # 0 = scissor, 1 = rock, 2 = paper
    if player_hand == computer_hand:      
     return "Draw" 
    
    if player_hand == 0 and computer_hand == 1 :      
            return f"Defeat" 
    if player_hand == 0 and computer_hand == 2 :      
            return f"Victory"
    if player_hand == 1 and computer_hand == 0 :      
            return f"Victory" 
    if player_hand == 1 and computer_hand == 2 :      
            return f"Defeat" 
    if player_hand == 2 and computer_hand == 0 :      
            return "Defeat" 
    if player_hand == 2 and computer_hand == 1 :      
            return f"Victory"  
    pass




# Welcome message & rules 
print(f' Welcomee to Rock Scissor games! Choice your hand and beat the computer ! ')

# Ask name & cheer
player_name = str(input(" What is your name ? "))
print(f' Good luck, {player_name}')

# Keep track of how many wins, losses, and draws they had.
track_player = {'Victory': 0, 'Defeat' :0, 'Draw': 0}

# Ask if the play want to play or exit the games, loop to continue the game if the user wanted.
play_game = True

while play_game : 

        new_game = str(input(f' Do you wish to play or exit the games ? Yes or No ') )

        if new_game in {'Yes', 'yes'}: 

                # Take in a number 0-2 from the user that represents their hand 
                print(f' Please Choose your hand, 0 - Scissor, 1 - Rock, 2 - Paper. ')
                player_hand = int(input(' What is your choice ? '))

                # Generate a random number 0-2 to use for the computer's hand
                computer_hand = random.randint(0, 2)


                # Call the function get_hand to get the string representation of the user's hand
                # Print out the player hand and computer hand
                print(f' Hand player is {get_hand(player_hand)}')


                # Call the function get_hand to get the string representation of the computer's hand
                print(f' Computer hand is {get_hand(computer_hand)}')


                # Call the function determine_winner to figure out who won
                determine_winner(player_hand, computer_hand)

                # Print out the winner
                print(f' The result is a {determine_winner(player_hand, computer_hand)}')
                
                
                
                # Adding & printing history games
                result_game = determine_winner(player_hand, computer_hand)
                
                # if result_game in {'Draw'}:
                #    track_player['Draw'] += 1
                
                # elif   result_game in {'Victory'}:
                #        track_player['Victory'] += 1

                # else:  
                #         track_player['Defeat'] += 1
                track_player[result_game] += 1

               
                print(f' Your game history is  {track_player}')
         
                
        else: play_game = False

print(f'Have a good day {player_name} and come back later')
exit()


