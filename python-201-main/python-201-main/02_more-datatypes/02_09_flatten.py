# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
new_list = []

for x in starter_list: 
    for i in x : 
        new_list.append(i)
print(new_list)

starter_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = [key for sublist in starter_list for key in sublist]

print(flat_list)

