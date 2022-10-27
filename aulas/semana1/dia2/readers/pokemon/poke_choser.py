import json
from random import randint

pokemon_list = []
indexes = []
time_choesed = []

with open("pokemons.json") as poke_file:
    pokemons = json.load(poke_file)["results"]

def type_fillter(type):
    type_list = [
        pokemon["name"] for pokemon in pokemons if type in pokemon["type"]
    ]
    return type_list

def time_chooser(pokemons_name):
    while(len(time_choesed) < 5):
        index = randint(0, len(pokemon_list))
        if (index not in indexes):
            time_choesed.append(pokemons_name[index])
            indexes.append(index)

type_pokemon = input("Digite o tipo dos pokemons: ")

is_valid = False
for pokemon in pokemons:
    if (type_pokemon in pokemon["type"]):
        is_valid = True
    if (is_valid):
        break

if (is_valid):
    pokemon_list = type_fillter(type_pokemon)
    time_chooser(pokemon_list)
    print(time_choesed)
else: 
    print("Não é um tipo válido")
    
