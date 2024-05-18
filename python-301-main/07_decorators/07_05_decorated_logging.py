# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.


import time


def my_time_decorator(func): 
    def wrapper_time(*args, **kwargs):
        start_time = time.time()
        print(f"This function starts at {start_time} ")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"This function end at that time {end_time} ")
        final_time = end_time - start_time
        print(f"This function total time  is {final_time}")
        return result
    return wrapper_time




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


@my_time_decorator
@make_decoration("§§§§§")
def make_beautiful(msg): 
    time.sleep(2)
    return msg

make_beautiful("Coucou")