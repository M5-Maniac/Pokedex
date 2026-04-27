import json

with open('pokedex.json', 'r') as in_file:
    pokedex = json.load(in_file)

def user_interface():
  print('Welcome to the Pokedex!\n')

  while True:
    print("_____MENU_____")
    print("1. View all Pokemon")
    print("2. List Pokemon by type")
    print("3. Get a Pokemon")
    print("4. Get pokemon evolution")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      list_all()
    elif choice == '2':
      list_by_type()
    elif choice == '3':
      display_pokemon()
    elif choice == '4':
      get_evolution()
    elif choice == '0':
      print("Thank you for using the Pokedex!")
      break
    else:
      print("Invalid choice. Please try again.")

def get_pokemon(type="all"):
  if type == "all":
    names = [p['name'] for p in pokedex['pokemon']]
  else:
    names = [p['name'] for p in pokedex['pokemon'] if type in p['type']]

  return names

def list_all():
  print("\nAll Pokemon:")
  names = get_pokemon()
  for i, name in enumerate(names):
    print(f"{i + 1}: {name}")
  print("\n")

def list_by_type():
  print("\n")
  poke_type = input("Enter a Pokemon type: ").capitalize()
  names = get_pokemon(poke_type)
  print(f"\nPokemon of {poke_type}:")
  for i, name in enumerate(names):
    print(f"{i + 1}: {name}")
  print("\n")

def display_pokemon():
  poke_name = input("Enter a pokemon to get info about: ")


  pokemon = next((p for p in pokedex['pokemon'] if p['name'].lower() == poke_name.lower()), None)

  if pokemon is None:
    print(f"Pokemon '{poke_name}' not found!\n")
    return

  # Print all the info
  print(f"\n{pokemon['name']}")
  print(f"Type: {', '.join(pokemon['type'])}")
  print(f"Height: {pokemon['height']}")
  print(f"Weight: {pokemon['weight']}")
  print(f"Egg: {pokemon['egg']}")
  print(f"Spawn Chance: {pokemon['spawn_chance']}")
  print(f"Avg Spawns: {pokemon['avg_spawns']}")
  print(f"Spawn Time: {pokemon['spawn_time']}")
  print(f"Weaknesses: {', '.join(pokemon['weaknesses'])}")
  print()



#main program
user_interface()