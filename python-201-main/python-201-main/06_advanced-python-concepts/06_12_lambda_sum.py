# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.

# x = 1 
# y = 2 
# z = 1 

# def sum_expression(x,y,z):
#     return x+y+z 

# print(sum_expression(x,y,z))

# three_num = lambda a:x+y+z
# print(three_num)

b = 2 
c = 3 

x = lambda a : a + b + c 
print(x(1))

x = lambda a, b, c : a + b + c
print(x(5, 6, 4))