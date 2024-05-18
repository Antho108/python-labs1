import requests
from bs4 import BeautifulSoup


BASE_URL = "https://codingnomads.github.io/recipes/"

def get_page_content(url):
    """Gets the response from a HTTP call to the URL."""
    page = requests.get(url)
    return page


if __name__ == "__main__":
    index_html = get_html_content(BASE_URL)
    index_soup = make_soup(index_html)
    recipe_links = get_recipe_links(index_soup)
    # breakpoint()

    for r_link in recipe_links:
        URL = f"{BASE_URL}/{r_link}"
        soup = make_soup(get_html_content(URL))
        # breakpoint()
        author = get_author(soup)
        recipe = get_recipe(soup)
        print(f"({author})\t[{recipe}]\n\n\n")