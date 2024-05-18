# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

list_2 = set(list_)
print(list_2)

list3 = []

for x in list_ : 
    if x not in list3 :
        list3.append(x)
        print(list3)

