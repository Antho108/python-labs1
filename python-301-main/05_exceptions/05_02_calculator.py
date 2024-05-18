# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.


def calcul(x, y):
    
    try : 
        result = x / y 
    
    except ZeroDivisionError:

        print("Error: cannot divide by zero. Please try again.")
        
        return None
    else :
        return result
        
         
  
    
while True:
     x = input(" Please enter a number: ")
     y = input(" Enter the number by which you want to divide ")
     try : 
            x = int(x)
            y = int(y)
     except ValueError:
            print("Please use only digits in your input.")
            continue
  
     result = calcul(x, y)

     if result is not None:
        print(f" The resulst is {result}") 

     whatodo = input(" Do you wish to quit [y/n] ? ")
     if whatodo.lower() == 'n':
        break

        # choice = input("Do you want to perform another division? (y/n): ")
        # if choice.lower() == 'n':
        #  break




