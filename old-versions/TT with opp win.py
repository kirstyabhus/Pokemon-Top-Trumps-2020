import random

import requests

import time


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


# this function happens when the user loses
# if the opponent wins, the opponent chooses the stat to compare
def opponent_win():
    # list of different stats
    stats = ['id', 'height', 'weight']

    # the opponents' stat choice is randomly chosen from the stat list
    stat_choice = random.choice(stats)

    # opponents' card is randomly chosen
    opponent_pokemon = random_pokemon()

    # the stat of the pokemon
    opponent_stat = opponent_pokemon[stat_choice]

    # randomly generates 3 cards
    my_pokemon1 = random_pokemon()
    my_pokemon2 = random_pokemon()
    my_pokemon3 = random_pokemon()

    # makes sure that none of the randomly generated cards are the same
    # if they are the same new cards are given
    if my_pokemon1 == my_pokemon2 or my_pokemon1 == my_pokemon3:
        my_pokemon1 = random_pokemon()
    elif my_pokemon2 == my_pokemon3 or my_pokemon2 == my_pokemon1:
        my_pokemon2 = random_pokemon()
    elif my_pokemon3 == my_pokemon1 or my_pokemon3 == my_pokemon2:
        my_pokemon3 = random_pokemon()

    # outputs a choice of 3 random cards for the user to choose from, with the stats name, id, height and weight
    print('Your cards:')
    print('CARD 1')
    print('NAME      {}'.format(my_pokemon1['name']))
    print('ID        {}'.format(my_pokemon1['id']))
    print('WEIGHT    {}'.format(my_pokemon1['weight']))
    print('HEIGHT    {}'.format(my_pokemon1['height']))
    print('')
    print('CARD 2')
    print('NAME      {}'.format(my_pokemon2['name']))
    print('ID        {}'.format(my_pokemon2['id']))
    print('WEIGHT    {}'.format(my_pokemon2['weight']))
    print('HEIGHT    {}'.format(my_pokemon2['height']))
    print('')
    print('CARD 3')
    print('NAME      {}'.format(my_pokemon3['name']))
    print('ID        {}'.format(my_pokemon3['id']))
    print('WEIGHT    {}'.format(my_pokemon3['weight']))
    print('HEIGHT    {}'.format(my_pokemon3['height']))
    print('')

    # asks the user which card from the randomly generated they want to pick
    card_pick = int(input('Which card do you want to use? (1, 2 or 3) '))
    print('')

    # outputs the stats of the card they have chosen
    if card_pick == 1:
        my_pokemon = my_pokemon1
        print('Your card:')
        print('NAME      {}'.format(my_pokemon1['name']))
        print('ID        {}'.format(my_pokemon1['id']))
        print('WEIGHT    {}'.format(my_pokemon1['weight']))
        print('HEIGHT    {}'.format(my_pokemon1['height']))
    elif card_pick == 2:
        my_pokemon = my_pokemon2
        print('Your card:')
        print('NAME      {}'.format(my_pokemon2['name']))
        print('ID        {}'.format(my_pokemon2['id']))
        print('WEIGHT    {}'.format(my_pokemon2['weight']))
        print('HEIGHT    {}'.format(my_pokemon2['height']))
    elif card_pick == 3:
        my_pokemon = my_pokemon3
        print('Your card:')
        print('NAME      {}'.format(my_pokemon3['name']))
        print('ID        {}'.format(my_pokemon3['id']))
        print('WEIGHT    {}'.format(my_pokemon3['weight']))
        print('HEIGHT    {}'.format(my_pokemon3['height']))

    my_stat = my_pokemon[stat_choice]

    # displays the stat the opponent chose to use
    print('')
    print('The opponent has chosen the stat: {}'.format(stat_choice))
    print('')
    time.sleep(5)  # 5 second delay

    # displays the opponents card
    print('Opponent card:')
    print('NAME      {}'.format(opponent_pokemon['name']))
    print('ID        {}'.format(opponent_pokemon['id']))
    print('WEIGHT    {}'.format(opponent_pokemon['height']))
    print('HEIGHT    {}'.format(opponent_pokemon['weight']))
    print('')

    #
    if my_stat > opponent_stat:
        print('You Win!')
        print('')
        time.sleep(5)  # 5 second delay before next round
        run()
    elif my_stat < opponent_stat:
        print('You Lose!')
        print('')
        time.sleep(5)  # 5 second delay before next round
        opponent_win()
    else:
        print('Draw!')


# main function & for if the user wins
def run():
    # randomly generates 3 cards
    my_pokemon1 = random_pokemon()
    my_pokemon2 = random_pokemon()
    my_pokemon3 = random_pokemon()

    # makes sure that none of the randomly generated cards are the same
    # if the cards are the same, new random cards are assigned
    if my_pokemon1 == my_pokemon2 or my_pokemon1 == my_pokemon3:
        my_pokemon1 = random_pokemon()
    elif my_pokemon2 == my_pokemon3 or my_pokemon2 == my_pokemon1:
        my_pokemon2 = random_pokemon()
    elif my_pokemon3 == my_pokemon1 or my_pokemon3 == my_pokemon2:
        my_pokemon3 = random_pokemon()

    # outputs the choice of 3 random cards for the user to choose from, with the stats name, id, height and weight
    print('Your cards:')
    print('CARD 1')
    print('NAME      {}'.format(my_pokemon1['name']))
    print('ID        {}'.format(my_pokemon1['id']))
    print('WEIGHT    {}'.format(my_pokemon1['weight']))
    print('HEIGHT    {}'.format(my_pokemon1['height']))
    print('')
    print('CARD 2')
    print('NAME      {}'.format(my_pokemon2['name']))
    print('ID        {}'.format(my_pokemon2['id']))
    print('WEIGHT    {}'.format(my_pokemon2['weight']))
    print('HEIGHT    {}'.format(my_pokemon2['height']))
    print('')
    print('CARD 3')
    print('NAME      {}'.format(my_pokemon3['name']))
    print('ID        {}'.format(my_pokemon3['id']))
    print('WEIGHT    {}'.format(my_pokemon3['weight']))
    print('HEIGHT    {}'.format(my_pokemon3['height']))
    print('')

    # asks the user which card from the randomly generated they want to pick
    card_pick = int(input('Which card do you want to use? (1, 2 or 3) '))
    print('')

    # outputs the stats of the card they have chosen
    if card_pick == 1:
        my_pokemon = my_pokemon1
        print('Your card:')
        print('NAME      {}'.format(my_pokemon1['name']))
        print('ID        {}'.format(my_pokemon1['id']))
        print('WEIGHT    {}'.format(my_pokemon1['weight']))
        print('HEIGHT    {}'.format(my_pokemon1['height']))
    elif card_pick == 2:
        my_pokemon = my_pokemon2
        print('Your card:')
        print('NAME      {}'.format(my_pokemon2['name']))
        print('ID        {}'.format(my_pokemon2['id']))
        print('WEIGHT    {}'.format(my_pokemon2['weight']))
        print('HEIGHT    {}'.format(my_pokemon2['height']))
    elif card_pick == 3:
        my_pokemon = my_pokemon3
        print('Your card:')
        print('NAME      {}'.format(my_pokemon3['name']))
        print('ID        {}'.format(my_pokemon3['id']))
        print('WEIGHT    {}'.format(my_pokemon3['weight']))
        print('HEIGHT    {}'.format(my_pokemon3['height']))

    # asks the user which stat they want to use
    print('')
    stat_choice = input('Which stat do you want to use? (id, height or weight) ')
    print('')

    # randomly generates a card for the opponent, and outputs the stats for the card
    opponent_pokemon = random_pokemon()
    time.sleep(2)
    print('Opponent card:')
    print('NAME      {}'.format(opponent_pokemon['name']))
    print('ID        {}'.format(opponent_pokemon['id']))
    print('WEIGHT    {}'.format(opponent_pokemon['height']))
    print('HEIGHT    {}'.format(opponent_pokemon['weight']))
    print('')

    # compares the users' stat and the opponents stat
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
        print('')
        time.sleep(5)  # 5 second delay before next round
        run()
    elif my_stat < opponent_stat:
        print('You Lose!')
        print('')
        time.sleep(5)  # 5 second delay before next round
        opponent_win()
    else:
        print('Draw!')


run()
