class Map:
  _instance = None
  _initialized = False 

  def __new__(cls):
    """
    if the map hasn’t been constructed, then construct it and store it in
    the instance class variable and return it. If it has, then just return the instance.
    """
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    """
    create and fill the 2D map list from the file contents. Create and
    fill the 2D revealed list with all False values
    """
    if not Map._initialized:
      self.load_map(1)
      Map._initialized = True
      
  def load_map(self,map_num):
    """
    fill the 2D map list from the specified file contents and reset the 2D revealed list with
    all False values.
    """
    with open("map" + str(map_num) + ".txt", "r") as file:
      self.map = [list(line.strip()) for line in file]
    self.revealed = [[False for n in range(len(self.map[0]))]for n in range(len(self.map))] 
    
  def __getitem__(self,row):
    """
    returns the specified row from
    the map.
    """
    return self.map[row]

  def __len__(self):
    """
    returns the number of rows in the map list
    """
    return len(self.map)

  def show_map(self, loc):
    """
    returns the map as a string in the format of a 5x5 matrix of
    characters where revealed locations are the characters from the map, unrevealed
    locations are ‘x’s, and the hero’s location is a ‘*’.
    """
    str_map = ""
    for i in range(len(self.map)):
      for j in range(len(self.map[i])):
        if i == loc[0] and j == loc[1]:  
          str_map += "*"
        elif self.revealed[i][j]: 
          str_map += self.map[i][j]
        else:
          str_map += "x"
      str_map += "\n"
    return str_map

  def reveal(self,loc):
    """
    sets the value in the 2D revealed list at the specified location to
    True.
    """
    self.revealed[loc[0]][loc[1]] = True
    
  def remove_at_loc(self,loc):
    """
    overwrites the character in the map list at the specified
    location with an ‘n’.
    """
    self.map[loc[0]][loc[1]] = "n"
    
    

  
  
        
    
    