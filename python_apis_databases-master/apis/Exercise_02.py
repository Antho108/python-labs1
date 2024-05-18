'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

# import requests

# base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
# response = requests.get(base_url)
# print(response.status_code)

# print(f"Response Content: {response.content}")

import json
import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
data = response.json()

# array = response.content
# data  = json.loads(array)
# # print (data["Email"])
# print(data(json.dumps(["email"])))

response = requests.get(base_url)

for key, value in response.items():
    print(key, ":", value)


# data = response.content

# pprint(data)
# print (data['data'][0]['email'])
# print (data['data'][1]['email'])
# print (data['data'][2]['email'])
# print (data['data'][3]['email'])

# array = response.json()
# data  = json.loads(array)
# print (data['mail'])





