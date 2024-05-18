# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.


file_in = open("words.txt", "r")
contents = file_in.read()
contents = contents.split()

reversed=''.join(reversed(contents)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string

file_new = open("words_reverse.txt", "a" )
file_new = file_new.write(reversed)

# Close the file 
file_in.close()
