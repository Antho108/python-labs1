# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

# Random list 
print(randlist)

# Sorted Random List 
randlist.sort()
print(randlist)

#stores the numbers in tuples of two in a new list

# x = list(zip(randlist))
# print(x)

# zlist = []
# for i in range(4):
#     zlist.append((x[i], y[i]))


# def convert(list):
#     return tuple(list)


# x = convert(randlist)
# print(x)

# tup_1 = ()
# tup_2 = () 

# for i in x: 
#     i.append(tup_1)


# Python3 code to demonstrate working of 
# Convert Tuple to Tuple Pair
# Using product() + next()
from itertools import product
  
# initializing tuple
test_tuple = str(randlist)
  
# printing original tuple
print("The original tuple : " + str(test_tuple))
  
# Convert Tuple to Tuple Pair
# Using product() + next()
test_tuple = iter(test_tuple)
res = list(product(next(test_tuple), test_tuple))
  
# printing result 
print("The paired records : " + str(res))