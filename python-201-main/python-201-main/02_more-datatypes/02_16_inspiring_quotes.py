# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname




famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

# b= 0

# # print(famous_quotes[0])
# print(f" {famous_quotes[0]['quote']}, {famous_quotes[0]['full_name']}")

for x in famous_quotes:
    name = x['full_name']
    split = name.split()
    print(f" The inspirinq quote is - {x['quote']} from {split[1]} {split[0]}. ")
    # print(f" {x['quote']}, {x['full_name']}")



# for x in famous_quotes:
#     print(f" {famous_quotes[x]['quote']}, {famous_quotes[x]['full_name']}") 