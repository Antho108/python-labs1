# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tup = tuple(string)
print(tup)

tup2 = list(string)
new_task = tup2.remove("c")
new_taks2 = tup2.insert(0, "k")
print(tup2)

tup3 = tuple(tup2)
print(tup3)
