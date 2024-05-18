# Sentence Analysis Tool
# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.

# Example input:

# I love to work with dictionaries!
# Example output:

# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28

sentence = " I love to work with dictionaries! "

upper_case = 0
lower_case = 0
ponctuation = 0
total = 0


for x in sentence: 
    if x.islower():
        lower_case = lower_case + 1

for u in sentence: 
    if u.isupper():
        upper_case = upper_case + 1

for p in sentence: 
    if p in ("!", "," ,"\'" ,";" ,"\"", ".", "-" ,"?"): 
        ponctuation = ponctuation + 1

total = upper_case + lower_case + ponctuation

my_dict = {"upper case": upper_case,"Lower case": lower_case, "Ponctuation": ponctuation, "Total chars" : total}


for case, num in my_dict.items(): 
    print(case, num)

    




