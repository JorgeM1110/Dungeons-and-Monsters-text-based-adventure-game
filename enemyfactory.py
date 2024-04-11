import abc 

class EnemyFactory(abc.ABC):
  """
  abstract method (no code) that each concrete
  factory overrides to create and return enemy     
  objects.
  """

  @abc.abstractmethod
  def create_random_enemy(self):
    pass