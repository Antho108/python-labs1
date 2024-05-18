# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  # define the function here
  max_num = max(example_list)
  min_num = min(example_list)
  sum_list = sum(example_list)
  return print(f" Num max of the list is {max_num}, Num min is {min_num}, Total is {sum_list}")

# call the function below here
stats()