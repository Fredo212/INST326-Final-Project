#This function's goal is to take the user input of budget and optional input of "important" which can be either food, money, or convinience.

class Travel:
  '''Sets attributes
    Attributes:
      destination (str): Name of the possible travel destination
      budget (str): Brief budget to go to that place
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
        
 
  def __repr__():
 #returns the final statement of where the user could go
 #Younju will do this part
    
