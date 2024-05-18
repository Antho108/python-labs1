# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from math import prod
from resources import randlist

print(randlist)

max_number = max(randlist)
print(f' the highest number is {max_number}')

prod_list = prod(randlist)
print(f' the prod of the list is {prod_list}')

