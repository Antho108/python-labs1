# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.


list_ = ["hello world!"]

try: 
    print(list_[1])
    pass  # The code to try
except IndexError:
    print("List out of range, try another times")
      # What to do if an exception occurred