import random

import requests


# randomly picks a pokemon using a random id number from 1 to 151
# returns the name, id, height and weigh of the pokemon
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }


def run():
    # displays the stats for the users' card
    my_pokemon1 = random_pokemon()
    my_pokemon2 = random_pokemon()
    my_pokemon3 = random_pokemon()

    if my_pokemon1 == my_pokemon2 or my_pokemon1 == my_pokemon3:
        my_pokemon1 = random_pokemon()
    elif my_pokemon2 == my_pokemon3 or my_pokemon2 == my_pokemon1:
        my_pokemon2 = random_pokemon()
    elif my_pokemon3 == my_pokemon1 or my_pokemon3 == my_pokemon2:
        my_pokemon3 = random_pokemon()

    print('Your cards:')
    print('CARD 1')
    print('NAME      {}'.format(my_pokemon1['name']))
    print('ID        {}'.format(my_pokemon1['id']))
    print('WEIGHT    {}'.format(my_pokemon1['height']))
    print('HEIGHT    {}'.format(my_pokemon1['weight']))
    print('')
    print('CARD 2')
    print('NAME      {}'.format(my_pokemon2['name']))
    print('ID        {}'.format(my_pokemon2['id']))
    print('WEIGHT    {}'.format(my_pokemon2['height']))
    print('HEIGHT    {}'.format(my_pokemon2['weight']))
    print('')
    print('CARD 3')
    print('NAME      {}'.format(my_pokemon3['name']))
    print('ID        {}'.format(my_pokemon3['id']))
    print('WEIGHT    {}'.format(my_pokemon3['height']))
    print('HEIGHT    {}'.format(my_pokemon3['weight']))
    print('')

    card_pick = int(input('Which card do you want to use? (1, 2 or 3) '))
    print('')
    if card_pick == 1:
        my_pokemon = my_pokemon1
        print('Your card:')
        print('NAME      {}'.format(my_pokemon1['name']))
        print('ID        {}'.format(my_pokemon1['id']))
        print('WEIGHT    {}'.format(my_pokemon1['height']))
        print('HEIGHT    {}'.format(my_pokemon1['weight']))
    elif card_pick == 2:
        my_pokemon = my_pokemon2
        print('Your card:')
        print('NAME      {}'.format(my_pokemon2['name']))
        print('ID        {}'.format(my_pokemon2['id']))
        print('WEIGHT    {}'.format(my_pokemon2['height']))
        print('HEIGHT    {}'.format(my_pokemon2['weight']))
    elif card_pick == 3:
        my_pokemon = my_pokemon3
        print('Your card:')
        print('NAME      {}'.format(my_pokemon3['name']))
        print('ID        {}'.format(my_pokemon3['id']))
        print('WEIGHT    {}'.format(my_pokemon3['height']))
        print('HEIGHT    {}'.format(my_pokemon3['weight']))
    else:
        card_pick = input('Which card do you want to use? (1, 2 or 3) ')

    print('')
    stat_choice = input('Which stat do you want to use? (id, height or weight) ')
    print('')

    opponent_pokemon = random_pokemon()

    print('Opponent card:')
    print('NAME      {}'.format(opponent_pokemon['name']))
    print('ID        {}'.format(opponent_pokemon['id']))
    print('WEIGHT    {}'.format(opponent_pokemon['height']))
    print('HEIGHT    {}'.format(opponent_pokemon['weight']))
    print('')

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')


run()
