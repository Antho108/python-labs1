'''
Using the PokéAPI https://pokeapi.co/docs/v2#pokemon-section
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''

      
# importing  module  
import requests

              # Create a folder Pokemon

# main_dir = "C:/Users/Ranganath/Desktop/Pokemon"
# os.mkdir(main_dir) 
# print("Directory '% s' is built!" % main_dir)

# Range to change webpage
for x in range(1, 5): 
                     
                     # Url pokemon
       base_url = f'https://pokeapi.co/api/v2/pokemon/{x}/'
       pokemon_response = requests.get(base_url)

                     # Get the data from the pokemon 
       data_pokemon = pokemon_response.json()
              
                     # Name of the pokemon
       name_pokemeon = (data_pokemon['name'])
                     # print(name_pokemeon)

                     # Height of the pokemon
       height_pokemeon = (data_pokemon['height'])
                     # print(f' the height of the pokemon is {height_pokemeon}')    

                     # Front_default of the pokemon 
       front_pokemon = (data_pokemon['sprites']['front_default'])



                     # Save the image # Bonus 

       # r = requests.get(front_pokemon)
       # # Open a local file with wb ( write binary ) permission.
       # with open('pokemon image','wb') as f:
       #          f.write(r.content)



                     # Write in a document text
       name = str(name_pokemeon) 
       height = str(height_pokemeon)
       with open('pokemon.txt', 'a') as f:
                            f.writelines(name)
                            f.writelines('\n')
                            f.writelines(f' the height of the pokemon is {height}')
                            f.writelines('\n')
                            f.writelines(front_pokemon)
                            f.close()




print('Congratulations you catch them all !')
   

