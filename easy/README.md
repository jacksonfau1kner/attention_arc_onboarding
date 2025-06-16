# Easy: Learning About Tables and Combining Data with Pokemon

Welcome! This tutorial will teach you how to work with data tables using Python. We'll use Pokemon data to make it fun!

## What You'll Learn

- How to create data tables (called "DataFrames")
- How to combine two tables together
- When to use different ways of combining tables

## Our Pokemon Data

We have two tables about Pokemon:

### Table 1: Pokemon Basic Info

This table has Pokemon names and details:

| pokedex_id | name       | type1 | type2  | height | weight |
| ---------- | ---------- | ----- | ------ | ------ | ------ |
| 1          | Bulbasaur  | Grass | Poison | 0.7    | 6.9    |
| 2          | Ivysaur    | Grass | Poison | 1.0    | 13.0   |
| 3          | Venusaur   | Grass | Poison | 2.0    | 100.0  |
| 4          | Charmander | Fire  | None   | 0.6    | 8.5    |
| 5          | Charmeleon | Fire  | None   | 1.1    | 19.0   |

### Table 2: Pokemon Battle Stats

This table has Pokemon fighting stats:

| pokedex_id | hp  | attack | defense |
| ---------- | --- | ------ | ------- |
| 1          | 45  | 49     | 49      |
| 2          | 60  | 62     | 63      |
| 3          | 80  | 82     | 83      |
| 6          | 78  | 84     | 78      |
| 7          | 44  | 48     | 65      |

**Notice:** Both tables have `pokedex_id` - this is how we connect them!

## Combining Tables (Called "Joins")

### Inner Join - Only Keep Matching Pokemon

This keeps only Pokemon that appear in BOTH tables.

**What Pokemon are in both tables?**

- Pokemon 1, 2, and 3 ✓
- Pokemon 4 and 5 are only in table 1 ✗
- Pokemon 6 and 7 are only in table 2 ✗

**Result after Inner Join:**
| pokedex_id | name | type1 | height | hp | attack | defense |
| ---------- | ---- | ----- | ------ | -- | ------ | ------- |
| 1 | Bulbasaur | Grass | 0.7 | 45 | 49 | 49 |
| 2 | Ivysaur | Grass | 1.0 | 60 | 62 | 63 |
| 3 | Venusaur | Grass | 2.0 | 80 | 82 | 83 |

**Result:** 3 Pokemon (only ones with complete information)

### Left Join - Keep All From First Table

This keeps ALL Pokemon from the first table, even if they don't have battle stats.

**Result after Left Join:**
| pokedex_id | name | type1 | height | hp | attack | defense |
| ---------- | ---- | ----- | ------ | -- | ------ | ------- |
| 1 | Bulbasaur | Grass | 0.7 | 45 | 49 | 49 |
| 2 | Ivysaur | Grass | 1.0 | 60 | 62 | 63 |
| 3 | Venusaur | Grass | 2.0 | 80 | 82 | 83 |
| 4 | Charmander | Fire | 0.6 | (missing) | (missing) | (missing) |
| 5 | Charmeleon | Fire | 1.1 | (missing) | (missing) | (missing) |

**Result:** 5 Pokemon (all from first table, some missing battle stats)

## When to Use Each Type

| Join Type      | When to Use                               | Example                                          |
| -------------- | ----------------------------------------- | ------------------------------------------------ |
| **Inner Join** | You need complete information             | "Show me Pokemon I can battle with"              |
| **Left Join**  | You want to keep all from your main table | "Show me all Pokemon, even without battle stats" |

## Simple Rules

1. **pokedex_id** is like a Pokemon's ID number - it connects the tables
2. **Inner Join** = Only complete matches
3. **Left Join** = Keep everything from the left (first) table
4. **Missing data** shows up as empty spots when Pokemon don't match

---

## 🎯 Your Tasks

### Task 1: Complete the Join Operation

**Objective:** Edit the variables in `example.py` to perform a left join

**What to do:**

- Replace `"???"` in the `operation` variable with the correct join type
- Replace `"???"` in the `merge_key_header` variable with the correct column name
- Run the code to see your results!

**Hint:** Look at the examples above to see what values you need!

---

### Task 2: Understanding the Results

**Objective:** Answer these questions to test your understanding

**Question 1:** There are some NaN (Not a Number) values being returned for some of the Pokemon. Why is that?

**Question 2:** What operation should be used to pull only the rows that successfully merged (no missing data)?

**Question 3:** Imagine the POKEMON_STATS table had a name column that COULD be used as the merge_key_header. Why is it best practice to use pokedex_id instead of name?

---

## 🚀 Getting Started

1. **First:** Read through this README to understand joins
2. **Then:** Open `easy/example.py` and complete Task 1
3. **Run:** Execute `python easy/example.py` to see your results
4. **Finally:** Answer the questions in Task 2 above

## What's Next?

Once you understand how joins work, you'll be ready for the medium section! 🌟
