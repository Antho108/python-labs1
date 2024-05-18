# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


def make_decoration(type): 
    def decorator_func(func): 
        def wrapper_func(*args, **kwargs):
            print(type * 7)
            result = func(*args, **kwargs)
            print(result)
            print(type* 7)
            return result
        return wrapper_func
    return decorator_func


@make_decoration("§§§§§")
def make_beautiful(msg): 
    return msg

make_beautiful("Coucou")




# Other way ***************

# def decorate(symbol):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(symbol * len(symbol) * 10)
#             result = func(*args, **kwargs)
#             print(result)
#             print(symbol * len(symbol) * 10)
#             return result
#         return wrapper
#     return decorator



# @decorate("*")
# def greet():
#     return "Hello"

# greet()

