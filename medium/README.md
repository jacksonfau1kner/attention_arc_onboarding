# Medium: Getting Pokemon Data from the Internet (APIs)

Welcome back! 🎮 Now that you know how to work with data tables, let's learn how to get real Pokemon data from the internet using APIs.

## What You'll Learn

- How to make API requests to get data from the internet
- How to parse JSON data (the format APIs use)
- How to extract specific information from nested data
- How to handle errors when APIs don't work
- How to turn messy API data into clean tables

## What is an API?

An **API** (Application Programming Interface) is like asking a website for data:

- You send a request: "Give me information about Bulbasaur"
- The API sends back data in JSON format (like a structured text file)
- We'll a public Pokemon API: `https://pokeapi.co/`

## JSON Data Format

When you ask for Pokemon data, you get something like this:

```json
[
  {
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "types": [{ "type": { "name": "electric" } }],
    "stats": [
      { "base_stat": 35, "stat": { "name": "hp" } },
      { "base_stat": 55, "stat": { "name": "attack" } }
    ]
  },
  {
    "name": "bulbasaur",
    "height": 5,
    "weight": 72,
    "types": [{ "type": { "name": "grass" } }],
    "stats": [
      { "base_stat": 55, "stat": { "name": "hp" } },
      { "base_stat": 45, "stat": { "name": "attack" } }
    ]
  }
]
```

**The Challenge:** This nested data is much more complex than a table!

## What We'll Practice

### Making Basic API Calls

- Request data for a single Pokemon
- Handle successful and failed requests
- Understand response codes

### Parsing JSON Responses

- Extract basic info (name, height, weight)
- Navigate nested data structures
- Handle missing or optional fields

### Working with Lists and Nested Data

- Extract Pokemon types from nested lists
- Get stats from complex nested structures
- Handle Pokemon with multiple types

### Building Clean Data Tables

- Convert messy API data into pandas DataFrames
- Create consistent column names
- Handle missing data gracefully

## Sample Data Extraction

From this messy API response:

```json
{
  "name": "bulbasaur",
  "types": [{ "type": { "name": "grass" } }, { "type": { "name": "poison" } }],
  "stats": [
    { "base_stat": 45, "stat": { "name": "hp" } },
    { "base_stat": 49, "stat": { "name": "attack" } }
  ]
}
```

We want to extract this clean data:
| name | type1 | type2 | hp | attack |
| ---- | ----- | ----- | -- | ------ |
| Bulbasaur | Grass | Poison | 45 | 49 |

## Understanding the Data Files

In this project, you'll work with two types of Pokemon data:

- **`raw_pokemon_data.json`** - This is the raw, unprocessed data directly from the Pokemon API. It contains all the nested structures and complex formatting you see above.
- **`sample_api_data.json`** - This contains the same Pokemon data but with pre-parsed, simplified fields. It's essentially what your parsing function should produce from the raw data.

Think of `sample_api_data.json` as your "answer key" - it shows you what the final parsed data should look like!

---

## 🎯 Your Tasks

### Task 1: Enhance the Pokemon Parser

**Objective:** Extend the `parse_pokemon_data()` function to extract additional fields

**What to add:**

- `base_experience` (found on line 20 in `raw_pokemon_data.json`)
- `front_default` sprite (found on line 13471 in `raw_pokemon_data.json`)
- `front_shiny` sprite (found on line 13473 in `raw_pokemon_data.json`)

**Hint:** Look at how existing fields are extracted and follow the same pattern!

---

### Task 2: Save Individual Pokemon Data

**Objective:** Export a single Pokemon's data to CSV format

**Requirements:**

- Use `pd.to_csv()` to save Pokemon with `pokedex_id` 17 to a `.csv` file
- Make sure your CSV has proper headers and is readable

**Expected output:** A clean CSV file with one Pokemon's complete data

---

### Task 3: Build Your First Pokedex

**Objective:** Create a dataset of multiple Pokemon

**Requirements:**

- Loop through the first 25 Pokemon in the Pokedex (IDs 1-25)
- Parse each Pokemon's data using your enhanced function
- Save all the data to a single CSV file

**Challenge:** Handle any Pokemon that might have missing data gracefully! (Not every pokemon will have a secondary type!)

---

## 🚀 Getting Started

1. Start by examining the existing `parse_pokemon_data()` function
2. Look at the raw JSON data to understand the structure
3. Compare with `sample_api_data.json` to see the expected output
4. Test your parsing function on a single Pokemon first
5. Then scale up to multiple Pokemon

Good luck, Pokemon Master! 🌟
