# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.

# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests 
from pprint import pprint
from bs4 import BeautifulSoup

base_url = "https://www.blogetudiantscompta.fr/mon-parcours/"
page = requests.get(base_url, "html.parser")


play = BeautifulSoup(page.text)

print(play.text)
# content = play.find("p", class_="elementor-clearfix")
# print(content.text)
# # <div class="elementor-widget-container"> <div class="elementor-text-editor elementor-clearfix"> <p>Diplômée d’un bac Scientifique spécialité Mathématiques en 2016, j’intègre dans la foulée la classe préparatoire au DCG en initial.</p><p>Après son obtention en 3 ans, et ayant bien rodé la méthode de travail qui m’a permis d’obtenir le diplôme avec 15 de moyenne générale, je décide de me lancer un challenge de taille :&nbsp;</p><p>Valider le DSCG <strong>en 1 an en alternance</strong> !</p><p class="nitro-offscreen">3 mots d’ordre :&nbsp;</p><ul class="nitro-offscreen"><li>Audace</li><li>Détermination</li><li>Travail&nbsp;</li></ul> </div> </div>

# # toto = play.find_all("p")
# # print(toto)
# # <p class="site-description" itemprop="description">

##" How to get a simple element when you have a wordress function with elementor? "
