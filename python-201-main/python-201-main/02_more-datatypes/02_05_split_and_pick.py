# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.


from collections import Counter




script = input(" Write something! ")
zozo = script.split()
print(zozo)

tozo = Counter(zozo)
print(tozo.most_common(1)[0][0])
