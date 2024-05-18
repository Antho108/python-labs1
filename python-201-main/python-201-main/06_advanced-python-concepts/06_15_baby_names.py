# You're about to adopt a baby and you don't have a name yet. 😱
# You and your partner agree that the name should start with an 'M',
# but that's about all you've got so far.
#
# To save the day, use the filter() method and a lambda expression
# to map all the baby names that begin with a 'M' to an output list.

names = ['Olivia', 'Noah', 'Ava', 'Oliver', 'Isabella', 'Mason', 'Sophia', 'Logan', 'Emma', 'Liam', 'Amelia', 'Lucas', 'Mia', 'Elijah', 'Charlotte', 'Ethan', 'Harper', 'James', 'Mila', 'Aiden', 'Aria', 'Carter', 'Ella', 'Jackson', 'Evelyn', 'Alexander', 'Avery', 'Sebastian', 'Abigail', 'Michael', 'Emily', 'Benjamin', 'Luna', 'Jacob', 'Riley', 'William', 'Scarlett', 'Grayson', 'Chloe', 'Jack', 'Sofia', 'Daniel', 'Layla', 'Owen', 'Lily', 'Luke', 'Madison', 'Henry', 'Ellie', 'Wyatt', 'Zoey', 'Jayden', 'Elizabeth', 'Leo', 'Penelope', 'Gabriel', 'Victoria', 'Julian', 'Grace', 'Matthew', 'Nora', 'David', 'Aubrey', 'Jaxon', 'Camila', 'Levi', 'Hannah', 'Mateo', 'Bella', 'Asher', 'Aurora', 'Lincoln', 'Addison', 'John', 'Stella', 'Samuel', 'Skylar', 'Muhammad', 'Paisley', 'Ryan', 'Savannah', 'Adam', 'Maya', 'Isaac', 'Natalie', 'Nathan', 'Elena', 'Josiah', 'Emilia', 'Isaiah', 'Violet', 'Joseph', 'Hazel', 'Caleb', 'Nova', 'Anthony', 'Niamey', 'Hunter', 'Eva', 'Eli']


choice_names = filter(lambda  x : "m" in x,  names)
print(list(choice_names))


# Python Lambda Function Syntax
# Syntax: lambda arguments: expression

# This function can have any number of arguments but only one expression, which is evaluated and returned.
# One is free to use lambda functions wherever function objects are required.
# You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
# It has various uses in particular fields of programming, besides other types of expressions in functions.




