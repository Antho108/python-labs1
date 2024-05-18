# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

# from resources import randlist
# print(randlist)

# unique_list = set(randlist)
# print(unique_list)


# toto = (1, 1, 2, 2, 4, 5, 'bonour', 'bonour')
# un_list = set(toto)
# print(un_list)


list_1 = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
new_list = []

for x in list_1 : 
    b =  list_1.count(x)
    if b < 2 : 
        new_list.append(x)
    
print(new_list)

# unique_list = [55, 'hi', 4, 13]
         