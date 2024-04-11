import entity 
import random
import map

class Hero(entity.Entity):

  def __init__(self,name):
    """
    initializes the name and max_hp using super, sets the
    hero’s starting location to row=0, col=0.
    """
    super().__init__(name, 25)
    self._loc = [0,0]
    m = map.Map()
    m.reveal(self._loc)
    
  @property 
  def location(self):
    return self._loc 

  @property
  def row(self):
      return self._loc[0]

  @property
  def col(self):
      return self._loc[1]

  def attack(self,entity):
    """
    hero attacks the enemy
    returns a string with attack info
    """
    damage = random.randint(2,5)
    entity.take_damage(damage)
    return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."

  def go_north(self):
    """
    updates the hero’s location
    """
    m = map.Map()
    if self.row > 0:
      self._loc[0] -= 1
      m.reveal(self._loc)
      return m[self.row][self.col]
    return 'o'
      
  def go_south(self):
    """
    updates the hero’s location
    """
    m = map.Map()
    if self.row < len(m) - 1:
      self._loc[0] += 1
      m.reveal(self._loc)
      return m[self.row][self.col]
    return 'o'

  def go_east(self):
    """
    updates the hero’s location
    """
    m = map.Map()
    if self.col < len(m[0]) - 1:
      self._loc[1] += 1
      m.reveal(self._loc)
      return m[self.row][self.col]
    return 'o'

  def go_west(self):
    """
    updates the hero’s location
    """
    m = map.Map()
    if self.col > 0:
      self._loc[1] -= 1
      m.reveal(self._loc)
      return m[self.row][self.col]
    return 'o'