# 🔴 PokémonFinder — CLI Pokédex

A **command-line Pokédex application** built in Python that lets you browse, search, and filter Generation 1 Pokémon using data from a local JSON database.

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Data Source](#data-source)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Future Updates](#future-updates)

---

## 📖 About

PokémonFinder is a Python terminal application that reads Pokémon data from a `pokedex.json` file and provides an interactive menu for users to explore **151 Generation 1 Pokémon**. The program uses Python's built-in `json` module to parse the data and presents it in a clean, numbered format through the command line.

---

## ✅ Features

### 1. View All Pokémon
- Displays a **numbered list of every Pokémon** in the Pokédex (all 151 Gen 1 Pokémon).
- Each Pokémon is listed with its index number and name.

### 2. Filter Pokémon by Type
- Prompts the user to enter a Pokémon type (e.g., `Fire`, `Water`, `Grass`, `Electric`, etc.).
- Returns a filtered, numbered list of all Pokémon that match the specified type.
- Input is **case-insensitive** — the program automatically capitalizes the first letter to match the data format.

### 3. Get Pokémon Details
- Prompts the user to enter a Pokémon name to look up.
- Performs a **case-insensitive search** to find the Pokémon in the database.
- Displays detailed information including:
  - **Name**
  - **Type(s)** — e.g., Grass, Poison
  - **Height** — in meters
  - **Weight** — in kilograms
  - **Egg Distance** — hatching distance (e.g., 2 km, 5 km)
  - **Spawn Chance** — probability of encountering in the wild
  - **Average Spawns** — average number of spawns
  - **Spawn Time** — time of day the Pokémon is most likely to appear
  - **Weaknesses** — list of types the Pokémon is weak against
- Returns a friendly error message if the Pokémon is not found.

### 4. Interactive Menu Loop
- The application runs in a **continuous loop**, letting users make multiple queries without restarting.
- Users can exit cleanly by selecting option `0`.
- Invalid menu choices display a helpful error message.

---

## 📁 Project Structure

```
Pokemon/
├── PokemonFinder.py   # Main application — all logic and UI
├── pokedex.json       # JSON database containing 151 Gen 1 Pokémon
└── readme.md          # This file
```

---

## ⚙️ How It Works

1. **Data Loading** — On startup, the program reads `pokedex.json` using Python's `json` module and loads the entire Pokédex into memory as a Python dictionary.

2. **Helper Function (`get_pokemon`)** — A reusable function that filters the Pokémon list. When called with `type="all"` (default), it returns every Pokémon name. When called with a specific type (e.g., `"Fire"`), it uses list comprehension to return only matching Pokémon.

3. **List All (`list_all`)** — Calls `get_pokemon()` with no arguments and prints every name with a numbered index.

4. **List by Type (`list_by_type`)** — Takes user input for a type, passes it to `get_pokemon()`, and displays the filtered results.

5. **Display Pokémon (`display_pokemon`)** — Uses Python's `next()` with a generator expression to find a single Pokémon by name (case-insensitive). Prints detailed stats or an error if not found.

6. **Menu Loop (`user_interface`)** — A `while True` loop that displays menu options, reads user input, and routes to the correct function using `if/elif` statements.

---

## 📊 Data Source

The `pokedex.json` file contains a JSON object with a `"pokemon"` array. Each Pokémon entry includes:

| Field             | Type          | Description                                |
|-------------------|---------------|--------------------------------------------|
| `id`              | Integer       | Pokédex ID number                          |
| `num`             | String        | Pokédex number (zero-padded, e.g., "001")  |
| `name`            | String        | Pokémon name                               |
| `img`             | String        | URL to the Pokémon image                   |
| `type`            | Array[String] | List of types (e.g., ["Grass", "Poison"])  |
| `height`          | String        | Height in meters                           |
| `weight`          | String        | Weight in kilograms                        |
| `candy`           | String        | Candy name used for evolution              |
| `candy_count`     | Integer       | Number of candies needed to evolve         |
| `egg`             | String        | Egg hatching distance                      |
| `spawn_chance`    | Float         | Wild encounter probability                 |
| `avg_spawns`      | Float         | Average number of spawns                   |
| `spawn_time`      | String        | Peak spawn time (24-hour format)           |
| `multipliers`     | Array/null    | CP multipliers for evolution               |
| `weaknesses`      | Array[String] | Types the Pokémon is weak against          |
| `next_evolution`  | Array/null    | List of Pokémon this can evolve into       |
| `prev_evolution`  | Array/null    | List of Pokémon this evolved from          |

---

## 🚀 Usage

### Prerequisites
- **Python 3.x** installed on your system
- No external libraries required — only uses the built-in `json` module

### Running the Program

```bash
python PokemonFinder.py
```

### Example Session

```
Welcome to the Pokedex!

_____MENU_____
1. View all Pokemon
2. List Pokemon by type
3. Get a Pokemon
4. Get pokemon evolution
0. Exit
Enter your choice: 3
Enter a pokemon to get info about: pikachu

Pikachu
Type: Electric
Height: 0.41 m
Weight: 6.0 kg
Egg: 2 km
Spawn Chance: 0.21
Avg Spawns: 21
Spawn Time: 04:00
Weaknesses: Ground
```

---

## 📝 Menu Options

| Option | Action                  | Status         |
|--------|-------------------------|----------------|
| `1`    | View all Pokémon        | ✅ Implemented |
| `2`    | List Pokémon by type    | ✅ Implemented |
| `3`    | Get Pokémon details     | ✅ Implemented |
| `4`    | Get Pokémon evolution   | 🚧 Coming Soon |
| `0`    | Exit the program        | ✅ Implemented |

---

## 🔮 Future Updates

### Evolution Chain Lookup (Option 4) — *In Progress*

The menu already includes **Option 4: "Get pokemon evolution"**, which calls a `get_evolution()` function that is currently **not yet implemented**. This is the next planned feature.

#### Planned Functionality
- The user will enter a Pokémon name.
- The program will look up both `next_evolution` and `prev_evolution` fields from the JSON data.
- It will display the **full evolution chain** for that Pokémon.
- Example output for **Ivysaur**:
  ```
  Evolution chain for Ivysaur:
  Bulbasaur (#001) → Ivysaur (#002) → Venusaur (#003)
  ```

#### How It Will Work
The data already exists in `pokedex.json` — each Pokémon entry can contain:
- **`prev_evolution`** — an array of Pokémon it evolved from (not present on base-stage Pokémon like Bulbasaur)
- **`next_evolution`** — an array of Pokémon it can evolve into (not present on final-stage Pokémon like Venusaur)

The `get_evolution()` function will need to:
1. Find the Pokémon by name (case-insensitive, same as `display_pokemon`).
2. Check for the existence of `prev_evolution` and `next_evolution` keys (since they are **optional** — not every Pokémon has them).
3. Build and display the complete evolution chain.

---

## 🛠️ Built With

- **Python 3** — Core language
- **JSON** — Data storage format
- **json module** — Built-in Python library for parsing JSON data

---

*PokémonFinder — Gotta query 'em all!*
