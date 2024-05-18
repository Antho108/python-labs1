# Add type annotations to the three functions shown below.


num1 = 1 
num2 = 2 
greeting = "salut"
name = "jhhn"
args = [1,2,3]

def multiply(num1, num2) -> int :
    return print(type(num1 * num2))

def greet(greeting, name) -> str :
    sentence = f"{greeting}, {name}! How are you?"
    return print(type(sentence))

def shopping_list(*args) -> tuple  :
    [print(f"* {item}") for item in args]
    return print(type(args))

multiply(num1, num2)
greet(greeting, name)
shopping_list(*args)