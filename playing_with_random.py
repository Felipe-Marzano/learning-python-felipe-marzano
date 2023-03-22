# Testing the random library
import random

# Using random to flip the coin (heads and tails)
coin = ['heads', 'tails']
print(random.choice(coin))

# Making 'random' choose a pokemon for me
short_list_of_pokemon_names = ['Pikachu',
                               'Charmander', 'Squirtle', 'Bulbasaur']
print(random.choice(short_list_of_pokemon_names))

# Choosing an random number from 1 to 100
print(random.randint(1, 100))
