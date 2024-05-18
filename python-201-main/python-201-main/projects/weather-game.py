# Include the current weather into your game mechanics.

# URL = "https://www.metaweather.com/api/"

# API Key: b6d8653676c24d54b3b95936221612


import requests 

# base_url = "https://api.weatherapi.com/v1/current.json?key=b6d8653676c24d54b3b95936221612&q=Kochi"
# response = requests.get(base_url)
# print(response.status_code)
# print(response.content)

user_location = input("Dear player write your city to know the weather of the dungeon")
base_url = f'https://api.weatherapi.com/v1/current.json?key=b6d8653676c24d54b3b95936221612&q={user_location}&aqi=yes'
response = requests.get(base_url)

# print(response.content)

data = response.json()
my_temp =  (data['current']['temp_c'])
my_weather = (data['current']['condition']['text'])
print(f' The temperature at your home is {my_temp}')
print(f' Your weather is {my_weather}')

# import requests
# # from pprint import pprint

# # base_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
# # response = requests.get(base_url)
# # # print(response.status_code)
# # # print(response.content)
# # data = response.json()
# # pprint(data)
# # my_drink =  (data['drinks'][0]['strDrink'])
# # my_drink_img = (data['drinks'][0]['strDrinkThumb'])
# # my_drink_descprtion = (data['drinks'][0]['strInstructions'])

# # print(f'this your recompense {my_drink}')
# # print(f'this is the way to serve {my_drink_descprtion}')
# # print(f' enjoy {my_drink_img}  ')
# # import requests

# # URL = "www.thecocktaildb.com/api/json/v1/1/search.php?i=vodka"

# # response = requests.get(URL)
# # print(f' your name is {response.text}')
# # print(response.status_code)

# old_name = str(input(" What is your name ? "))

# if len(old_name) < 3 or len(old_name) >= 40 : 
#     print("Your name is too short please insert a new name")
#     old_name = str(input(" What is your name ? "))
# max_len = len(old_name)


# URL = f"https://uzby.com/api.php?min={2}&max={max_len}"
# response = requests.get(URL)

# print(f' your new name for this dungeon is {response.text}')
# player_name = response.text
