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
    with open(filepath, "r", encoding = "utf-8") as f:
      for line in f:
        line = line.split()
        self.destination = line[0]
        self.budget = line[1]
        self.important = line[2]
        
  def recommend(self, budget, important = "price"):
    '''Finds the recommended destination from the file
    Args:
     budget (int): Brief budget to go to that place
     important (str, optional): Important factor of travel that is originally set to "price." User may s
    '''
    BudgetRec = df[df["budget"] > budget - 300, ["budget"] < budget + 300]
    recommended = BudgetRec[BudgetRec["important"] == "price"]
    return recommended
          

  
  def __repr__(self):
 #returns the final statement of where the user could go
 #Younju will do this part
    """
    Returns a string representation of the Travel object.
    """
    #try:
      #return f"Travel(destination='{self.destination}',price = {self.price})
    #except Exception as e:
      #raise Exception(f"An error occured
      # while generating the string representation of the Travel object: {e}")
    return f"Travel(destination ='{self.destination}', price={self.price})"


class Vacation(Travel): 
  def __init__(self): 
    super().__init__("fiji", 20000, "price")
    print("this vacation is to: fji, it costs: 20000")

  def find_most_expensive_day(day_prices): 
    return day_prices.max() 
  
  

