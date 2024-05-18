# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!

from bs4 import BeautifulSoup
import requests

BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)
# print(page.text)

html_text = BeautifulSoup(page.text, "html.parser")
# print(html_text)


# soup = BeautifulSoup(page.text)
# # print(soup)

links = html_text.find_all("a")

for link in links:
     print(link["href"])

# newlist = [links["href"] for links in links]
# print(newlist)


# import requests
# from bs4 import BeautifulSoup

# URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

# page = requests.get(URL)
# soup = BeautifulSoup(page.text)
# # print(soup.prettify())

# author = soup.find("p", class_="author")
# # print(author.text)
# # print(author.text.strip("by "))

# title = soup.find("h1", class_="title")
# # title = soup.title
# print(title.text)


# body = soup.find("ol", class_="div.md")
# print(body)