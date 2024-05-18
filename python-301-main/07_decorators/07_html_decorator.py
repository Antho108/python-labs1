# PROJECT: HTML Element Decorator
# Write a decorator function that wraps text passed to it in a specified HTML tag. 
# The user should be able to decide which tag to use.

# For example, you should be able to use the decorator like so:
# Define the greet function that takes a name parameter and returns a greeting message
# @tagify("p")
# def greet(name):
#   return f"Hello, {name}"

# Call the greet function with the "Bessy" argument and print the result, wrapped in a <p> tag
# print(tagify("Bessy"))  # OUTPUT: <p>Hello, Bessy</p>

# You should be able to pass any HTML tag name to your decorator, irrespective of how many arguments 
# the function that you're wrapping takes. The wrapped function should output their returned string 
# wrapped in the relevant HTML tag:

# Define the lorem
# return "Lorem ipsum dolor sit amet, ..."

# print(lorem())  # OUTPUT: <div>Lorem ipsum dolor sit amet, ...</div>
# You can accomplish all this with just one decorator, but you'll need to apply all the concepts 
# that you've learned throughout this section.

# This project can be challenging. Push yourself and attempt to complete it in order to synthesize 
# your learning and apply your knowledge practically. If you have questions, post to your CodingNomads forum.

# When you've built a functioning decorator for wrapping text content into HTML text, 
# you can use it in your automatic website generator script.


def tagify(tag): 
    def decorator_html(func): 
       def wrapper_html(*args, **kwargs): 
          result = func(*args, **kwargs)
          html_code = f"<{tag}> {result} </{tag}>"
          return html_code
       return wrapper_html
    return decorator_html



@tagify("p")
def greet(name):
  return f"Hello, {name}"


@tagify("div")
def lorem():
    return "Lorem ipsum dolor sit amet, ..."

print(lorem())  # OUTPUT: <div>Lorem ipsum dolor sit amet, ...</div>
print(greet("Jean Marc"))


