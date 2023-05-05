#This function's goal is to take the user input of budget and optional input of "important" which can be either food, money, or convinience.
import pandas as pd
from argparse import ArgumentParser
import sys

class Travel:
  '''Sets attributes
    Attributes:
      df(str): contains the dataframe that Readfile will read
  '''
  def __init__(self, df, important):
 #Aki will finish this part
    self.df = df
    self.important = important

  
  def Readfile(self, filepath):
    """reads a text file and assigns values to variables based on data in the 
          text file.

    Args:
        filepath (string): path to CSV File
    """
 #Reads the file, separates by space and assign each material to corresponding variable
 #Alfred will do this part
    df = pd.read_csv(filepath)

    return df
        
  def recommend(self, df, budget, important = "price"):
    '''Finds the recommended destination from the file
    Args:
     budget (int): Brief budget to go to that place
     important (str, optional): Important factor of travel that is originally set to "price." User may s
    '''
    BudgetRec = df[df["budget"] > budget - 300, ["budget"] < budget + 300]
    recommended = BudgetRec[BudgetRec["important"] == important]
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
  
# Added a main function, code below is just testing - Alfred
def main(filepath, destination, budget, important_factor = "price"):
  df = pd.read_csv(filepath)
  print(df)
  print(df["Budget"])

# Added command line arguments, these aren't required for the project 
# requirements, so they can be removed if feel their unnecessary - Alfred
def parse_args(arglist):
    """ allows use of the command line

    Args:
        arglist (string): list of command-line arguments
    
    Returns:
        args: the parsed arguments
    """
    parser = ArgumentParser()
    parser.add_argument("filepath",
                        help="path to CSV File")
    parser.add_argument("destination",
                        help="name of destination")
    parser.add_argument("budget", type=int,
                        help="budget for trip")
    parser.add_argument("-i" "--important", default= "price",
                        help="originally set to price. User may set this to \
                        price, food or convenience.")
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    """calls functions that are at the global scope
    """
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.destination, args.budget, args.i__important)