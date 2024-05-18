# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def my_decorator(initial_func): 
    def my_wraper_quotes(): 
        return f"'{initial_func()}'"
    return my_wraper_quotes 


@ my_decorator
def hello(): 
    return "Hello world"

print(hello())

