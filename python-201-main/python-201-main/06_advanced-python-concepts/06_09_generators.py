# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.


generator = (x*2 for x in range(5))
print(generator) 


list_ = [x*2 for x in range(5)]
print(list_)  # OUTPUT: [0, 2, 4, 6, 8]
print(type(list_))  # OUTPUT: <class 'list'>

gen = (x*2 for x in range(5))
for i in gen:
    print(i)