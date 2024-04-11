import entity
import random 
class EasyZombie(entity.Entity):

  def __init__(self):
    """
    randomize max_hp according to the table below for each of the
    different enemies. 
    """
    max_hp = random.randint(4,5)
    super().__init__("slow Zombie",max_hp)

  def attack(self,entity):
    """
    enemy attacks hero – randomize damage according to the
    table below.
    """
    damage= random.randint(1,5)
    entity.take_damage(damage)
    return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."