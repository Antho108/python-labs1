# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

# Write a function that prints out nicely formatted information about a
# real estate advertisement



lista=[]
def display_nice(**kwargs):
    for k,v in kwargs.items():
        lista.append(f"The {k} of the property is {v}")
    return(lista)

b=display_nice(size="1000 m2",water_available="Yes",permits="all",school_area="2 miles away")


print(lista)