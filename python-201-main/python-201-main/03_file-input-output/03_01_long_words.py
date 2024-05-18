# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


file_in = open("words.txt", "r")
contents = file_in.read()
contents = contents.split()

for x in contents:
    if len(x) >= 20 : 
        print(x)

file_in.close()