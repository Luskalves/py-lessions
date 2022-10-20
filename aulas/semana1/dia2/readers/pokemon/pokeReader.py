import json

# utilizando o LOADS
# with open("pokemons.json") as pokefile:
#     content = json.loads(pokefile.read())
#     for pokemon in content["results"]:
#         print(pokemon["name"])

#utilizando o LOAD
with open("pokemons.json") as poke_file:
    pokemons = json.load(poke_file)["results"]
    for pokemon in pokemons:
        if ("Fire" in pokemon["type"]):
           print(pokemon["name"])

electric_type_pokemons = [
    pokemon for pokemon in pokemons if "Electric" in pokemon["type"]
]

print(electric_type_pokemons)