# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.





# while True: 
#     try:
#         file_in = open('python-301-main/05_exceptions/integers.txt', "r")
#     except OSError:
#         print(" Please select the good path for your file ")
#         break
#     first_number  = int(file_in.readline().strip())

#     user = input(" Choose a number ")
#     try : 
#         user = int(user)
#     except: 
#         print(" Please enter a digit ")
#         continue
    
#     sum = first_number + user 
#     print(f" The resulst is {sum}")

#     choice = input("Do you wish to continue? [y/n] ")
#     if choice.lower() == 'n': 
#      break
 


try:
    with open('python-301-main/05_exceptions/integers.txt', 'r') as file:
        first_number = int(file.readline().strip())
        result = 10 / first_number
        print(result)
except IOError:
    print('Could not read file')
except ValueError:
    print('File does not contain a valid integer')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print('Calculation successful')