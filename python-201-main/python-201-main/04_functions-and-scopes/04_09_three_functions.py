# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

# Restaurant programm! 

name = "John"

def greetings(name): 
    message = f" Welcome mister {name} to our famous restaurant "
    return message 

def sitting(place):
    ask = f" {name} would you like a table with a good view ? "
    return ask 

def order(waiter) :  
    text = f" Miser {name} is ready to order ? "
    return text 


print(greetings(name))
print(sitting("where"))
print(" The menu is on the table, feel free to ask question ")
print(order("waiter"))