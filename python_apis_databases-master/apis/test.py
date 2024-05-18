# import json

# array = '{"Technology": ["AI", "ML", "DataScience"]}'
# data  = json.loads(array)
# print (data['Technology'])


import json
stringA = "[21,42, 15]"
# Given string
print("Given string", stringA)
print(type(stringA))
# String to list
res = json.loads(stringA)
# Result and its type
print("final list", res)
print(type(res))