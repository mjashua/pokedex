import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    # response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format{name})
    pokemon = response.json()

    print("Name: {} \nId: {} \nBase XP: {}".format(
        str.capitalize(pokemon["name"]),
        str(pokemon["id"]),
        str(pokemon["base_experience"])
    ))

if __name__ == "__main__":
    search_pokemon(sys.argv[1])


