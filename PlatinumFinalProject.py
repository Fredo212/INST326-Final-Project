#This function's goal is to take the user input of budget and optional input of "important" which can be either food, money, or convinience.
import pandas as pd

class Travel:
  '''Sets attributes
    Attributes:
      destination (str): Name of the possible travel destination
      budget (int): Brief budget to go to that place
      important (str, optional): Important factor of travel that is originally set to "price." User may set this to price, food or convenience.
  '''
  def __init__(self, destination, budget, important = "price"):
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
    destinations_df = pd.read_csv("Destinations_File.csv")

    return destinations_df
        
  def recommend(self, budget, important = "price"):
    '''Finds the recommended destination from the file
    Args:
     budget (int): Brief budget to go to that place
     important (str, optional): Important factor of travel that is originally set to "price." User may s
    '''
    BudgetRec = df[df["budget"] > budget - 300, ["budget"] < budget + 300]
    recommended = BudgetRec[BudgetRec["important"] == "price"]
    return recommended
          
  
  # If you want to change this code for read file, you can use this code. (Younju Kim)
  def from_file(self,filepath):
    """
    reads a text file and creates a list of Travel objects based on data in the text file.
    
    Args:
      filepath (string): file that will be passed in this function to be read
      
    Returns:
      A list of Travel objects
    """
    travels = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.split()
            destination = line[0]
            budget = int(line[1])
            important = line[2]
            travel = Travel(destination, budget, important)
            travels.append(travel)
    return travels
  
  def __repr__(self):
  
    """
    Returns a string representation of the Travel object.
    """
    return f"Travel(destination ='{self.destination}', budget={self.budget}, important = '{self.important}')"
  
  def __str__(self):
    """
    Returns a human-readable string representation of the Travel object.
    """
    return f"{self.destination} ({self.budget} budget, important: {self.important})"
  
  def __lt__(self,other):
    """
    Defines a less-than comparison between two Travel objects.
    """
    return self.budget < other.budget
    
class Vacation(Travel): 
  def __init__(self): 
    super().__init__("fiji", 20000, "price")
    print("this vacation is to: fji, it costs: 20000")

  def find_most_expensive_day(day_prices): 
    return day_prices.max() 
  
  

