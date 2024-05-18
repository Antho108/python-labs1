# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

# def my_enumerate(toto, index=0 ):  # add your arguments
#       # add your code implementation
      
#       for item in toto: 
#             print(item)
#             index += 1
#             # print(index)
#       pass

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']


def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
   

for index, courses in my_enumerate(courses):
    print(f"{index}: {courses} Python")



