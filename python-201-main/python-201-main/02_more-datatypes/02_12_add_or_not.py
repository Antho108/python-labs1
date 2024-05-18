# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

b = set()
counter = 0 
print( " Welcome to Memory Game! For win you have to create a set of 10 digit number ! ")
print( " Good luck ! ")

while counter <= 5 or counter == 5 :  
     num = int(input(" Enter a number "))
     if num not in b :
        b.add(num)
        
     else: counter +=1 ; print(f' Number already exist!  {6 - counter} opportunity remains  ')
    #  print(counter)
    #  print(b)
    #  print(len(b))
     if len(b) >= 10 : 
        print(" You win the games ! ")
        exit()
print( "Games over ")
exit()

