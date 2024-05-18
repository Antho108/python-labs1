# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.

# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5



list_poke = []
id_poke = []
type_poke = []
import requests

for x in range(1,7):
    base_url = f'https://pokeapi.co/api/v2/pokemon/{x}/'
    pokemon_response = requests.get(base_url)
    data_pokemon = pokemon_response.json()
    name_pokemeon = (data_pokemon['name'])
    id_pokemon = (data_pokemon['id'])
    type_pokemon = (data_pokemon['types'][0]['type']['name'])
     

    list_poke.append(name_pokemeon)
    id_poke.append(id_pokemon)
    type_poke.append(type_pokemon)

# print(list_poke)
# print(id_poke)
# print(type_poke)


result_poke = [*list_poke, *id_poke, *type_poke]
# print(result_poke)


resultat = [i + j for i, j in zip (list_poke, type_poke)]
print(resultat)