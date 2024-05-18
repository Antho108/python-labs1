# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.
import pytest
import requests
from bs4 import BeautifulSoup


url = "https://codingnomads.github.io/recipes/"

def get_page_content(url):
    """Gets the response from a HTTP call to the URL."""
    page = requests.get(url)
    return page

def get_html_content(url):
    """Gets the HTML from a page."""
    html = get_page_content(url).text
    return html

#########################################

def test_page_content():
    content = requests.get(url).text
    assert content

def test_html_content():
    html = get_page_content(url).text
    assert html

def test_always_passes():
    assert True

if __name__ == "__main__":
    pytest.main()