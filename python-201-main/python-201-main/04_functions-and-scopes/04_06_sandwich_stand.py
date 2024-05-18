# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.


def make_sandwich(type_bread, toppings) -> str : 
    type_bread = input(" What bread do you want ? French Bread - Italian Bread - German Bread ")
    amount_toppings = int(input(" How many toppings you want ? "))
    toppings = amount_toppings * " tomatoes, pesto, mozzarella "
    sandwich = type_bread + toppings + type_bread


    return print(sandwich)


make_sandwich(1, 2)