import enemyfactory
import random
import easygoblin
import easyskeleton
import easyzombie

class BeginnerFactory(enemyfactory.EnemyFactory):
  """
  factory to create easy enemies.
  """

  def create_random_enemy(self):

    random_monster = random.randint(1,3)

    if random_monster == 1:
      return easygoblin.EasyGoblin()

    elif random_monster == 2:
       return easyskeleton.EasySkelton()

    else:
       return easyzombie.EasyZombie()