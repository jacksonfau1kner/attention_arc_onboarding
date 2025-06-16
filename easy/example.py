# First, we need to import pandas (a tool for working like tables)
import pandas as pd

# ------------------------------------------ #
# ---------- INTRODUCTION START ------------ #
# ------------------------------------------ #


# ------------ POKEMON_INFO -------------- #
# pokedex_id | name       | type1 | height
# ------------------------------------------
# 1          | Bulbasaur  | Grass | 0.7
# 2          | Ivysaur    | Grass | 1.0
# 3          | Venusaur   | Grass | 2.0
# 4          | Charmander | Fire  | 0.6
# 5          | Charmeleon | Fire  | 1.1

POKEMON_INFO = pd.DataFrame(
    {
        "pokedex_id": [1, 2, 3, 4, 5],
        "name": ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon"],
        "type1": ["Grass", "Grass", "Grass", "Fire", "Fire"],
        "height": [0.7, 1.0, 2.0, 0.6, 1.1],
    }
)


# ---------- POKEMON_STATS ------------ #
# pokedex_id | hp | attack | defense
# -------------------------------------
# 1          | 45 | 49     | 49
# 2          | 60 | 62     | 63
# 3          | 80 | 82     | 83

POKEMON_STATS = pd.DataFrame(
    {
        "pokedex_id": [1, 2, 3, 6, 7],
        "hp": [45, 60, 80, 78, 44],
        "attack": [49, 62, 82, 84, 48],
        "defense": [49, 63, 83, 78, 65],
    }
)
# ---------- POKEMON_STATS ------------ #


# ------------------------------------------ #
# ----------- INTRODUCTION END ------------- #
# ------------------------------------------ #


def merge_pokemon_data(operation, merge_key_header):
    merge_pokemon_data = pd.merge(
        POKEMON_INFO, POKEMON_STATS, how=operation, on=merge_key_header
    )
    return merge_pokemon_data


# Task 1: Edit the values below to make a left join on the pokedex_id column
operation = "???"
merge_key_header = "???"
merged_data = merge_pokemon_data(operation, merge_key_header)
print(merged_data)
