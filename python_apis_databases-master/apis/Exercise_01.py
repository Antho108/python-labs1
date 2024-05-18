'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
print(response.status_code)

print(f"Response Content: {response.content}")
print(f"Response Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Encoding: {response.encoding}")
print(f"Response URL: {response.url}")

