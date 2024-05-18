# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.

import codingnomads.recipes.soup  as s
import codingnomads.ingredients as i 


digestible = i.prepare(i.potato)
mix = i.carrot + i.potato + i.salt
soup = s.make_soup(mix)
print(soup)
