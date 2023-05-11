import pandas as pd
from argparse import ArgumentParser
import sys

class Travel:
    """
    A class representing a travel destination.
    
    Attributes:
      destination (str): The destination for the travel.
      budget (int): The budget for the travel
      important (str, optional): The important factor of the travel. Default is "price".
    """
    def __init__(self, destination, budget, important="price"):
      """_summary_

      Args:
          destination (str): The destination for the travel.
          budget (str): The budget for the travel
          important (str, optional): The important factor of the travel. Defaults to "price".
      """
      self.destination = destination
      self.budget = budget
      self.important = important

    def recommend(self, df, budget, important="price"):
        """
        Finds the recommended destination from the provided dataframe based on the given budget and important factor.
        
        Args:
          df (pd.DataFrame): The dataframe containing information about travel destinations.
          budget (int): The brief budget to go to that place.
          important (str, optional): The importan factor of travel. Default is "price".
          
        Returns:
          recommended (pd.DataFrame): The recommended destinations based on the input parameters.
        """
        BudgetRec = df[(df["Budget"] > budget - 300) & (df["Budget"] < budget + 300)]
        recommended = BudgetRec[BudgetRec["Important (optional)"].str.contains(important, case=False)]
        return recommended

    def __repr__(self):
        """
        Returns a string representation of the Travel object.
        """
        return f"Travel(destination='{self.destination}', budget={self.budget}, important='{self.important}')"

    def __str__(self):
        """
        Returns a human-readable string representation of the Travel object.
        """
        return f"{self.destination} ({self.budget} budget, important: {self.important})"

    def __lt__(self, other):
        """
        Defines a less-than comparison between two Travel objects based on their budgets.
        """
        return self.budget < other.budget

class Vacation(Travel):
  """
    A child class representing a Vacation, using all features of its parent, Travel.
    
    Attributes:
      destination (str): The destination for the vacation.
      budget (int): The budget for the vacation
      important (str): The important factor of the vacation. Default is "luxury".
      
    Methods:
      Overriden:
      recommend(df, budget, important="price"):
        Finds the recommended destination from the provided dataframe based on the given budget and important factor.
        
      all other methods from the parent class (Travel)
    """
  def __init__(self):
    super().__init__("Fiji", 20000, "price")
    print("This vacation is to: Fiji, it costs: 20000")


def read_file(filepath):
    """
    Reads a CSV file and returns a dataframe.
    
    Args:
      filepath (str): Path to the CSV file.
      
    Returns:
      df (pd.DataFrame): The dataframe containing the data from the CSV file.
    """
    df = pd.read_csv(filepath)
    return df


def from_file(filepath):
    """
    Reads a text file and creates a list of Travel objects based on data in the text file.
    
    Args:
      filepath (str): Path to the text file.
      
    Returns:
      travels (list): A list of Travel objects.
    """
    travels = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.split(",")
            destination = line[0]
            budget = int(line[1])
            important = line[2].strip()
            travel = Travel(destination, budget, important)
            travels.append(travel)
    return travels
    

def recommend_destinations(df, destination, budget, important_factor):
    """
    Recommends destinations based on the given budget and important factor.
    
    Args:
      df (pd.DataFrame): The dataframe containing information about travel destinations.
      destination (str): The name of the destination.
      budget (int): The budget for the trip.
      important_factor (str): The important factor for the trip.
      
    Returns:
      recommended_destinations (pd.DataFrame): The recommended destinations based on the input parameters.
    """
    travel_obj = Travel(destination, budget, important_factor)
    recommended_destinations = travel_obj.recommend(df, budget, important_factor)
    print(f"\nRecommended destinations for your budget and important factor ({important_factor}):")
     # Use list comprehension to generate the recommended destinations string
    destinations_str = '\n'.join([f"- {row['Destination']} ({row['Budget']} budget, important: {row['Important (optional)']})" for _, row in recommended_destinations.iterrows()])
    print(destinations_str)
    return recommended_destinations


def display_discounted_price(recommended_destinations):
    """
    Displays the discounted price for a randomly selected destination from the recommended destinations.
    
    Args:
      recommended_destinations (pd.DataFrame): The recommended destinations.
      
    """
    print("Updating data...")
    discounted_destination = recommended_destinations.sample(n=1).iloc[0]
    original_budget = discounted_destination['Budget']
    discounted_budget = int(original_budget * 0.8)  # Apply 20% discount

    print(f"\nUpdated price for {discounted_destination['Destination']}:")
    print(f"- {discounted_destination['Destination']} ({discounted_budget} budget, important: {discounted_destination['Important (optional)']})")

    print("\nRecommending destinations after the update:")
    for idx, row in recommended_destinations.iterrows():
        if row['Destination'] == discounted_destination['Destination']:
            print(f"- {row['Destination']} ({discounted_budget} budget, important: {row['Important (optional)']})")
        else:
            print(f"- {row['Destination']} ({row['Budget']} budget, important: {row['Important (optional)']})")

def get_user_input(recommended_destinations):
    """
    Gets the user input for destination, budget, and important factor.

    Args:
      recommended_destinations (pd.DataFrame): The recommended destinations.

    Returns:
      destination (str): The name of the destination.
      budget (int): The budget for the trip.
      important_factor (str): The important factor for the trip.
    """
    user_input = input("Enter destination, budget, and important_factor (optional, default: price): ")
    inputs = user_input.split()
    
    destination = inputs[0]
    budget = int(inputs[1])
    important_factor = inputs[2] if len(inputs) > 2 else "Price"
    
    return destination, budget, important_factor
     
def main(filepath, destination, budget, important_factor="price"):
    """
    The main function that performs the recommendation process and handles user interaction.

    Args:
      filepath (str): The path to the CSV file.
      destination (str): The name of the destination.
      budget (int): The budget for the trip.
      important_factor (str, optional): The important factor for the trip. Default is "price".

    """
    df = read_file(filepath)
    print(df)
        
    recommended_destinations = recommend_destinations(df, destination, budget, important_factor)

    # Check if user wants to see a discounted price
    answer = input("There is a discount. Would you like to see it at a discounted price? (yes/no): ")
    if answer.lower() == "yes":
        display_discounted_price(recommended_destinations) 
    
    elif answer.lower() == "no":
        destination, budget, important_factor = get_user_input(recommended_destinations)
        main(filepath, destination, budget, important_factor)
    else:
        sys.exit()

def parse_args(arglist):
    """
    Parses the command-line arguments.
    
    Args:
      arglist (list): List of command-line arguments.
      
    Returns:

    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to CSV File")
    parser.add_argument("destination", help="name of destination")
    parser.add_argument("budget", type=int, help="budget for trip")
    parser.add_argument("-i", "--important", default="price",
                        help="originally set to price. User may set this to price, food or convenience.")
    args = parser.parse_args(arglist)
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.destination, args.budget, args.important)