# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]





user = input(" Enter a text ! ")
user = list(user)
print(user)

for take in user: 
    print(take)

test = [tuple(WORD) for WORD in user]
print(test)

# string = tuple(user)
# print(string)


