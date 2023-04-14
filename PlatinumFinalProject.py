#This function's goal is to take the user input of budget and optional input of "important" which can be either food, money, or convinience.

class Travel:
  '''Sets attributes
    Attributes:
      destination (str): Name of the possible travel destination
      budget (int): Brief budget to go to that place
      important (str, optional): Important factor of travel that is originally set to "price." User may set this to price, food or convenience.
  '''
  def __init__(self, destination, budget, important = price):
 #Aki will finish this part
    self.destination = destination
    self.budget = budget
    self.important = important

  
  def Readfile(self, filepath):
    """reads a text file and assigns values to variables based on data in the 
          text file.

    Args:
        filepath (string): file that will be passed in this function to be read
    """
 #Reads the file, separates by space and assign each material to corresponding variable
 #Alfred will do this part
    with open(filepath, "r", encoding = "utf-8") as f:
      for line in f:
        line = line.split()
        self.destination = line[0]
        self.budget = line[1]
        self.important = line[2]
        
  def recommend(self, budget, important = price):
    '''Finds the recommended destination from the file
    Args:
     budget (int): Brief budget to go to that place
     important (str, optional): Important factor of travel that is originally set to "price." User may s
    '''
    recList = []
    for Readfile(filepath):
      try math.isclose(budget, self.budget, rel_tol = 300):
        if True:
          recList.append(destination)
         else:
          continue
    return recList
          
      
  
  def __repr__():
 #returns the final statement of where the user could go
 #Younju will do this part
    
