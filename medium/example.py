# First, we need to import requests (for API calls)
import requests

# Let's start with a simple API request
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(pokedex_id):
    # Get the data from the API
    response = requests.get(f"{POKEMON_API_URL}/{pokedex_id}")
    pokemon_data = response.json()
    return pokemon_data


def parse_pokemon_data(pokemon_data):
    # Parse the response
    pokemon_name = pokemon_data["name"]
    pokemon_height = pokemon_data["height"]
    pokemon_weight = pokemon_data["weight"]
    pokemon_primary_type = pokemon_data["types"][0]["type"]["name"]
    # Hint:
    # pokemon_base_experience = pokemon_data["something"]
    # front_default_sprite = pokemon_data["sprite"]["something"]
    # front_shiny_sprite = pokemon_data["something"]["something"]

    pokemon_secondary_type = (
        pokemon_data["types"][1]["type"]["name"]
        if len(pokemon_data["types"]) > 1
        else None
    )

    return {
        "name": pokemon_name,
        "height": pokemon_height,
        "weight": pokemon_weight,
        "primary_type": pokemon_primary_type,
        "secondary_type": pokemon_secondary_type,
        # TODO: Add the following fields:
        # "base_experience":
        # "front_default_sprite":
        # "front_shiny_sprite":
    }


# Task 1:
# edit the def parse_pokemon_data() to include the following fields:
# - base_experience (line 20 in medium/raw_pokemon_data.json)
# - front_default sprite (line 13471 in medium/raw_pokemon_data.json)
# - front_shiny sprite (line 13473 in medium/raw_pokemon_data.json)


# Task 2:
# Use pd.to_csv to save pokedex_id 17 to a .csv


# Task 3:
# Loop through the first 25 pokemon in the pokedex and save the data to a csv file
