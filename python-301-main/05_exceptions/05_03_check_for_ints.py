# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True: 

    try :
     user = int(input("Please enter an integer: "))
    except ValueError:
        print("Please enter a digit")
        continue

    if type(user) == int: 
        print(" This is a int! Thanks you!")
        break

 
    

   
    # if type(user) == int: 
    #     print("Bravo ")

