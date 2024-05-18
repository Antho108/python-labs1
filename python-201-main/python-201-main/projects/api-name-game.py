# Add an API call to your CLI game that assigns a name to your player.

import requests


# Ask the player for their name. # Choice the size of your name 

toto_name = input("What is your name")
toto_name = len(toto_name)
print(toto_name)
URL = f"https://uzby.com/api.php?min={toto_name}&max={toto_name}"
response = requests.get(URL)

print(f' your name is {response.text}')


player_name = response.text