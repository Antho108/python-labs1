def lowercase(func):
    """A decorator that avoids digital screaming."""
    def wrapper(text):
        initial_result = func(text)
        new_result = initial_result.lower()
        return new_result
    return wrapper

@lowercase
def say_something(text):
    return text

@lowercase 
def say_hello(text): 
    return text 


print(say_something("HOW TO UNDERSTAND IT!!"))  # OUTPUT: hei what's up?
print(say_hello("HOW ARE YOU ??? "))