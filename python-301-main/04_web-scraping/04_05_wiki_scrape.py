# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.

# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

from bs4 import BeautifulSoup
import requests
from pprint import pprint

base_url = "https://en.wikipedia.org/wiki/Web_scraping"
page = requests.get(base_url)

html_text = BeautifulSoup(page.text, "html.parser")

# Extract all the links on the page
links = html_text.find_all("a")

for link in links:
    pprint(link["href"])

# newlist = [links["href"] for links in links]
# print(newlist)

    

 
# navigation links are excluded.
# Filter out the navigation links
filtered_links = [link for link in links if not link.startswith('#')]

print(filtered_links)


# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint
# # Send a GET request to the URL for the Wikipedia page on Web scraping
# url = 'https://en.wikipedia.org/wiki/Web_scraping'
# response = requests.get(url)

# # Parse the HTML content of the page
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all the links on the page
# links = [link.get('href') for link in soup.find_all('a')]

# # Filter out the navigation links
# filtered_links = [link for link in links if not link.startswith('#')]

# pprint(filtered_links)





