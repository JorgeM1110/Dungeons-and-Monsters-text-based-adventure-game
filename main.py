import random
import check_input
from hero import Hero
from map import Map
import expertfactory
import beginnerfactory

def check_non_monster_space(move, map_counter, game_map, player):
  """
  checks the non-monster space that the player is on and preforms the corresponding action.
  """
  if move ==  'o':
    print("You cannot go that way...")

  elif move == 'n':
    print("There is nothing here...")

  elif move == 's':
    print("You wound up back at the start of the dungeon.")

  elif move == 'i':
    player.heal()
    print("You found a Health Potion! You\n drink it to restore your health.")
    game_map.remove_at_loc(player.location)
  
  elif move == 'f':
    print("Congratulations! You found the stairs to the next floor of the dungeon.")
    if (map_counter + 1) > 3:
      map_counter = 1
    else:
      map_counter += 1 
    game_map.load_map(map_counter)
    game_map.reveal(player.location) 
  return map_counter


def main():
  
  name = input("What is your name, traveler? ")
  difficulty = check_input.get_int_range("Difficulty:\n1.Beginner\n2.Expert\n", 1, 2)
  if difficulty == 1:
    fact = beginnerfactory.BeginnerFactory()
  else:
    fact = expertfactory.ExpertFactory()
  player = Hero(name)
  map_counter = 1
  game_map = Map()
  while True:
    print("\n" + str(player))
    print(game_map.show_map(player.location))
    menu_choice = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice: ", 1, 5)
    print("")


    if menu_choice == 1: #checking the player's movement choice
      move = player.go_north()
    elif menu_choice == 2:
      move = player.go_south()
    elif menu_choice == 3:
      move = player.go_east()
    elif menu_choice == 4:
      move = player.go_west()
    else:
      break

    if move == 'm':
      monster = fact.create_random_enemy()
      print(f"You encounter a {monster}")

      run_away = False
      while player.hp != 0 and monster.hp != 0 and not run_away: #combat loop
        print(player)
        action = check_input.get_int_range(f"\n1.Attack {monster}\n2.Run Away\nEnter choice:",1,2)
        print("")
        if action == 1: #player has chosen to attack
            print(player.attack(monster))
            if monster.hp != 0:
                print(monster.attack(player))
                if player.hp == 0:
                  print("You have perished\nGame Over :(")
                  exit()
            else:
              print("You defeated the monster!")
              game_map.remove_at_loc(player.location)
              break
        elif action == 2: #player has chosen to run away.
          run_away = True 
          while(True): 

            menu_choice = random.randint(1,4)
            if menu_choice == 1 and player.row < len(game_map) - 1: #check to see if the direction of movement is an edge.
              move = player.go_south()
              print("You ran south")
              map_counter = check_non_monster_space(move, map_counter, game_map, player)
              break
            elif menu_choice == 2 and player.row > 0:
              move = player.go_north()
              print("You ran north")
              map_counter = check_non_monster_space(move, map_counter, game_map, player)
              break
            elif menu_choice == 3 and player.col > 0:
              move = player.go_west()
              print("You ran west")
              map_counter = check_non_monster_space(move, map_counter, game_map, player)
              break
            elif menu_choice == 4 and player.col < len(game_map[0]) - 1:
              move = player.go_east()
              print("You ran east")
              map_counter = check_non_monster_space(move, map_counter, game_map, player)
              break
            else:
              pass
  
    else:
      map_counter = check_non_monster_space(move, map_counter, game_map, player)

main()