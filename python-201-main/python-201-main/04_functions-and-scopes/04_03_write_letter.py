# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name, text): 
    name = input("  What is your name ? " )
    text = input(" Enter your letter please ! ")

    greeting = (f" I am very happy to see you, {name} ")
    bye_msg =  (f" It's been a pleasure to meet you {name} ")

    letter = greeting + text + bye_msg 
    
    return print(letter)

(write_letter("x", "y"))