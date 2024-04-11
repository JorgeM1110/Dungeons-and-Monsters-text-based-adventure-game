import entity
import random 
class Zombie(entity.Entity):

  def __init__(self):
    """
    randomize max_hp according to the table below for each of the
    different enemies. 
    """
    max_hp = random.randint(8,10)
    super().__init__("Fast Zombie",max_hp)

  def attack(self,entity):
    """
    enemy attacks hero – randomize damage according to the
    table below.
    """
    damage= random.randint(5,12)
    entity.take_damage(damage)
    return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."