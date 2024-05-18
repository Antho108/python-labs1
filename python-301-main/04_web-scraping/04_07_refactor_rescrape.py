# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.


from bs4 import BeautifulSoup
import requests

base_url = "https://codingnomads.github.io/recipes/"
page = requests.get(base_url)

def gettext():
    # BASE_URL = "https://codingnomads.github.io/recipes/"
    # page = requests.get(base_url)
    return print(page.text)


def gethtml():
    # page = requests.get(base_url)
    html_text = BeautifulSoup(page.text, "html.parser")
    return print(html_text)


def getlink(base_url):
    page = requests.get(base_url)
    html_text = BeautifulSoup(page.text, "html.parser")
    links = html_text.find_all("a")

    for link in links:
         print(link["href"])


# getlink( "https://codingnomads.github.io/recipes/")


def getauthor(base_url):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")
    author = soup.find("p", class_="author")
    print(author.text)
    print(author.text.strip("by "))

# getauthor("https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html")

def gettitle(base_url):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")
    title = soup.find("h1", class_="title")
    title = soup.title
    print(title.text)

# gettitle("https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html")

gettext()










        