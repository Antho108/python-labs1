# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import requests
from pathlib import Path

#Geeting a quote
# base_url = f'https://quotes.rest/qod?category=management'
# response = requests.get(base_url).json["quotes"]
# data = response.json()

# my_quote = (data['contents']['quotes'])
# print(my_quote)


# Geeting img 
base_url = f'https://shibe.online/api/shibes'
response = requests.get(base_url)
data_img = response.json()
print(data_img)


# print both 
print(data_img)


# Function_Name = open("Toto","w")

# Function_Name.write("<html>\n<head>\n<title> \nOutput My first page with python \
#            </title>\n</head> <body><h1>Welcome to <u>GeeksforGeeks</u></h1>\
#            \n<h2>A <u>CS</u>  h2> \n <p> Salut c'est toto  <p>\n </body></html>")
# Function_Name.close()


html = f"<img src='{data_img}'>"
f = Path().home().joinpath("Desktop").joinpath("index.html")
f.write_text(html)
print(html)
