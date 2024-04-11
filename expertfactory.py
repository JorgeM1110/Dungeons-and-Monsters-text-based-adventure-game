import enemyfactory
import random
import goblin
import skeleton
import zombie

class ExpertFactory(enemyfactory.EnemyFactory):
  """
  factory to create more difficult enemies.
  """

  def create_random_enemy(self):

    random_monster = random.randint(1,3)

    if random_monster == 1:
      return goblin.Goblin()

    elif random_monster == 2:
      return skeleton.Skelton()

    else:
      return zombie.Zombie()