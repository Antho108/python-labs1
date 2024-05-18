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


#  It’s a more advanced concept called a lookup table, which you can explore to make determining the winner easier. You’ll need to understand both dictionaries and tuples, so if you’re not there yet, no worries – ignore the rest of this until later.

# In your determine_winner() function, you have a series of if statements to figure out who won. The combinations never change – if the player has scissors (0) and the computer has rock (1), the outcome is always the same.

# Rather than use if statements, what if you could use that fact to just lookup the answer, given the player’s and computer’s hands?

# Here’s how you might do this: You can group each combination of hand values as tuples, with the player’s hand first and the computer’s hand second. In this case, you would have six tuples: (0,1), (0,2), (1,0), (1,2), (2, 0), and (2, 1).

# Now, you can use those tuples as the keys in a dictionary, with the value for each key being the outcome of the game. It might look something like this:

# outcomes = { (0, 1): "Defeat", 
#              (0, 2): f"Victory {player_name}", 
#              (1, 0): f"Victory {player_name}", 
#              (1, 2): "Defeat", 
#              (2, 0): "Defeat", 
#              (2, 1): f"Victory {player_name}" }
# Now, instead of a series of if statements, the expression outcomes[(player_hand, computer_hand)] will give you the proper result, after checking for a draw. You can even expand the lookup table to include the three draw conditions as well, so your determine_winner() function is just a lookup table with a single return.

# You can also use this same concept in your get_hand() function, using just a simple list. The hand is the index into the list, which contains the three hand values.

# If you implement these two lookup tables, you may see another optimization as well, but I’ll leave that for later.

# As I said, the lookup table is a more advanced concept. If you decided to skip it, your game is still well made and shows some great understanding of how to structure a program.

# *----------------------------------------------------------------------------*

# Module for random number 
import random

# Function declaration 
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    my_hand = ('Scissor', 'Rock', 'Paper')
    return my_hand[hand]

# call the function determine_winner to figure out who won
def determine_winner(player_hand, computer_hand) :
     # 0 = scissor, 1 = rock, 2 = paper
    outcomes = {(0, 0): "Draw",
             (0, 1): "Defeat", 
             (0, 2): "Victory ", 
             (1, 1): "Draw",
             (1, 0): "Victory", 
             (1, 2): "Defeat", 
             (2, 0): "Defeat", 
             (2, 1): "Victory",
             (2, 2): "Draw"}
    return outcomes[(player_hand, computer_hand)]


# Welcome message & rules 
print(f' Welcomee to Rock Scissor games! Choice your hand and beat the computer ! ')

# Ask name & cheer
player_name = str(input(" What is your name ? "))
print(f' Good luck, {player_name}')

# Keep track of how many wins, losses, and draws they had.
track_player = {'Victory': 0, 'Defeat' :0, 'Draw': 0}

# Ask if the play want to play or exit the games, loop to continue the game if the user wanted.
play_game = True

while play_game == True: 

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
                result_game = determine_winner(player_hand, computer_hand)

                # Print out the winner
                print(f' The result is a {result_game}')
                 
                # Adding & printing history games
                if result_game in {'Draw'}:
                   track_player['Draw'] += 1
                
                elif   result_game in {'Victory'}:
                       track_player['Victory'] += 1

                else:  
                        track_player['Defeat'] += 1

               
                print(f' Your game history is  {track_player}')
         
                
        else: play_game = False

print(f'Have a good day {player_name} and come back later')
exit()
