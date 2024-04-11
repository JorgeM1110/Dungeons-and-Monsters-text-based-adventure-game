import entity
import random 

class Skelton(entity.Entity):

  def __init__(self):
    """
    randomize max_hp according to the table below for each of the
    different enemies. 
    """
    max_hp = random.randint(6,10)
    super().__init__("Skeleton King",max_hp)

  def attack(self,entity):
    """
    enemy attacks hero – randomize damage according to the
    table below.
    """
    damage= random.randint(6,10)
    entity.take_damage(damage)
    return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."