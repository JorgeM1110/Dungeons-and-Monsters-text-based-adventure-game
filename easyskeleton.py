import entity
import random 

class EasySkelton(entity.Entity):

  def __init__(self):
    """
    randomize max_hp according to the table below for each of the
    different enemies. 
    """
    max_hp = random.randint(3,4)
    super().__init__("Skeleton Larry",max_hp)

  def attack(self,entity):
    """
    enemy attacks hero – randomize damage according to the
    table below.
    """
    damage= random.randint(1,4)
    entity.take_damage(damage)
    return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."