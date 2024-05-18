# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

# - take in a number from the user between 1 and 1,000,000,000

num = int(input("Enter a number between 1 and 1,000,000,000 "))

# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean

def div1(num):
    if  num%7 == 0 or num%4 == 0  :
        print(f'{num} is divisible by 4 or 7')
        return print(True)
    else:
        print(f'{num} is not divisible by 4 or 7')
        return print(False)


# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean

def div2(num):
    if  num%7 == 0 and num%4 == 0  :
        return print(True)
        print(f'{num} is divisible by 4 & 7')
        
    else:
        print(f'{num} is not divisible by 4 & 7')
        return print(False)


div1(num)
div2(num)
