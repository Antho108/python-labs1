# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

# from collections import Counter

# my_dict= {}
# xValue = 0
# user = input(" Write a word ")
# user = {}

# res = Counter(user)
# print(res)



my_dict= {}
xValue = 1
user = input(" Write a word ")

for x in user: 
    xValue = user.count(x)
    my_dict.update({x: xValue})
print(my_dict)



   

# Reflexion par ecrit. 
# Je souhaite que l'ordinateur compte les lettres dans mon dico et me dise combien de fois elle apparait. 
# Et cela representera la valeur
# comment faire ca ?  Ben je peux faire une boucle dans le dico 



