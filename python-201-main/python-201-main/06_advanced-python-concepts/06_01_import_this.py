# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.


# import codingnomads.recipes.soup as s 
# import codingnomads.cook as c
# import codingnomads.ingredients as i 

from codingnomads.recipes.soup import * 
from codingnomads.ingredients import potato


soup = make_soup(potato)
print(soup)
