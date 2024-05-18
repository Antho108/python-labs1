# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

file_in = open("words.txt", "r")
contents = file_in.read()
contents = contents.split()


# 1. The shortest word (if there is a tie, print all)
# Finding shortest word
shortest = min(contents, key=len)

# Displaying shortest word
print("Shortest word is: ", shortest)
print("And its length is: ", len(shortest))

# 2. The longest word (if there is a tie, print all)
# Finding longest word
longest = max(contents, key=len)

# Displaying longest word
print("longest word is: ", longest)
print("And its length is: ", len(longest))


# 3. The total number of words in the file.

num_words = 0 

for x in contents: 
    num_words += 1
    
print("The total number of words in the file is", num_words)


# Close the file 
file_in.close()