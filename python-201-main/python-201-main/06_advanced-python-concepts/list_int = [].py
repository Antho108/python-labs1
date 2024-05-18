# list_int = []
# list_int2 = []
# my_dict = {}

# for num in range(100): # yes this is good!
#    # ok, we have a num now, which is the num we want to turn base 10. 
        
    
#         for v in str(num):
#             list_int.append(v)
#             v = int(v)
#             my_dict[num] = list_int[v]

#             for c in str(num): 
#                 list_int2.append(c)
#                 c = int(c)
#             my_dict[num] = list_int[v]  list_int[c]
   
        
        
 

# print(my_dict) 
 
    # in step one you did
    # for v in toto
   # can you do something like
   # for v in str(num) ? and then make the list of ints?

def convert_int_to_components(value):
    return list(map(lambda x: int(x), [*str(value)]))


# def functional_solution(limit):
#     return {k: v for (k, v) in zip(range(limit), list(map(lambda x: convert_int_to_components(x), range(limit))))}

def imperative_solution(limit):
  result = {}
  for i in range(limit):
    result[i] = convert_int_to_components(i)
  return result

limit = 1000

# print('Using functional approach: \n')
# print(functional_solution(limit))
# print('\n')

# print('Using imperative approach: \n')
# print(imperative_solution(limit))
# print('\n')