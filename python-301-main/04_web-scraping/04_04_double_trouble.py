# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests
import pprint

poem = []


for x in range(3):
                        #  Query the chucknorris api for a sentence
  base_url = f'https://api.chucknorris.io/jokes/random'
  chuck_response = requests.get(base_url)
  chuck_data = chuck_response.json()
  # pprint.pprint(chuck_data)

                        #  Printing Quote
  chuck_quote = (chuck_data['value'])

                       # Get the last word of that sentence
  last_word = chuck_quote.split()
  last_word = last_word[-1]
 
                         # Remove the dot of the last word
  last_word = last_word.replace('.', '')

                # send a query to the Datamuse API
        # use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
  base_url = f'https://api.datamuse.com/words?rel_rhy={last_word}'
  data_reponse = requests.get(base_url).json()
  #  pprint.pprint(data_reponse)
                    # New rhyme word
  data_muse = (data_reponse[1]["word"])
 
                      # Remove last word from the quote.
  new_sentence = chuck_quote
  new_sentence = new_sentence.rsplit(' ', 1)[0]
  new_poem = new_sentence + " " +  data_muse
  
                 # * Synthesize the collected results into an avant-garde poem and post on the forum ;)
  poem.append(new_poem)
  
  
print(poem)
