import abc

class Entity(abc.ABC):

  def __init__(self,name,max_hp):
    """
    initializes each of the instance variables
    """
    self._name = name 
    self.max_hp = max_hp
    self._hp = max_hp

  @property
  def name(self):
    return self._name 

  @property
  def hp(self):
    return self._hp


  def take_damage(self,dmg):
    """
    subtracts the dmg from the hp, but does not allow the
    hp to drop below 0.
    """
    self._hp -= dmg

    if self._hp < 0:
      self._hp = 0

  def heal(self):
    """
    restores the entity’s hp to max_hp.
    """
    self._hp = self.max_hp

  def __str__(self):
    """
    returns a string in the format ‘Name\nHP: hp/max_hp’
    """
    return self.name +"\nHP:" +   str(self._hp) + "/" + str(self.max_hp)

  @abc.abstractmethod
  def attack(self,entity):
    """
    entity subclasses will override to attack and do damage to the opposing entity.
    """
    pass