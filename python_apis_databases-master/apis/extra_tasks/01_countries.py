'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
import requests

# Setup URL with the response France
base_url = "https://restcountries.com/v3.1/name/France"
fr_response = requests.get(base_url)


# Get the data from the French country. 
data_fr = fr_response.json()
population_france = (data_fr[0]['population'])
print(f' the population in france is {population_france}')


# Get the data from the India country. 
base_url2 = "https://restcountries.com/v3.1/name/India"
india_response = requests.get(base_url2)
data_in = india_response.json()
population_india = (data_in[0]['population']) 
print(f'population in India is {population_india}')


# Compare the total population. 
if population_france >= population_india :
    print ("The population of France is larger")
else: print(" Indian population is Bigger")

# Difference between both 
calcul_diff = population_india  - population_france
print(f"The difference between the two is : {calcul_diff} ")

# * Print the native name of both countries, as well as their capitals

capital_france =  (data_fr[0]['capital'])
capital_inde = (data_in[0]['capital'])


print(f'the capital of France is {capital_france}')
print(f'the capital of India is {capital_inde}')






