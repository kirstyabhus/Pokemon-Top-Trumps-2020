import requests

#list to store pokemon id's
pokemon_ids = [1, 2, 3, 4, 5, 6]

pokemon_values = []

#get pokemon data for each pokemon
for pokemon_id in pokemon_ids:
    # get names and moves
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()
    name = pokemon['name']
    moves = pokemon['moves']


poke_data = {'Name': name, 'Moves': moves}
pokemon_values.append(poke_data)

with open ('pokemon.txt', '+w') as text_file:
   # text_file.write(pokemon_values)