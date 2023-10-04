import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()

    # moves = requests.get(f"https://pokeapi.co/api/v2/move/{name}/")
    # move = moves.json()
    # hp = pokemon["stats"][0]["base_stat"]
    # attacks = pokemon["moves"][0]["move"]["name"]
    # held items = pokemon["held_items"][0]["item"]["name"]
    print("-------------------\n\nName: {}\nHP: {}/{}\nAttacks: {}\nHeld Items: {}\n".format(
        str.capitalize(pokemon["name"]),
        str(pokemon["stats"][0]["base_stat"]),
        str(pokemon["stats"][0]["base_stat"]),
        str.capitalize(pokemon["moves"][0]["move"]["name"]),
        str.capitalize(pokemon["held_items"][0]["item"]["name"])
    )) 

if __name__ == "__main__":
    search_pokemon(sys.argv[1])
    search_pokemon(sys.argv[2])