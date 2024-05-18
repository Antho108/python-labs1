# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

name = input(" Enter your name ")
greeting = "Hello"
text = "Wold is beautiful"

def greet(greeting, name):

    sentence = (f" {greeting}, {name}! How are you? ")
    return sentence

def write_letter(name, text): 
  
    greeting = greet("Welcome", name)
    bye_msg =  (f" It's been a pleasure to meet you {name} ")
    letter = greeting + text + bye_msg 
    
    return print(letter)


greet(greeting, name)
write_letter(name, text)



