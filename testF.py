import pandas as pd
from argparse import ArgumentParser
import sys

class Travel:
    def __init__(self, destination, budget, important="price"):
        self.destination = destination
        self.budget = budget
        self.important = important

    def recommend(self, df, budget, important="price"):
        BudgetRec = df[(df["Budget"] > budget - 300) & (df["Budget"] < budget + 300)]
        recommended = BudgetRec[BudgetRec["Important (optional)"].str.contains(important, case=False)]
        return recommended

    def __repr__(self):
        return f"Travel(destination='{self.destination}', budget={self.budget}, important='{self.important}')"

    def __str__(self):
        return f"{self.destination} ({self.budget} budget, important: {self.important})"

    def __lt__(self, other):
        return self.budget < other.budget

class Vacation(Travel):
    def __init__(self):
        super().__init__("Fiji", 20000, "price")
        print("This vacation is to: Fiji, it costs: 20000")


def read_file(filepath):
    df = pd.read_csv(filepath)
    return df


def from_file(filepath):
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
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to CSV File")
    parser.add_argument("destination", help="name of destination")
    parser.add_argument("budget", type=int, help="budget for trip")
    parser.add_argument("-i", "--important", default="price",
                        help="originally set to price. User may set this to price, food or convenience.")
    args = parser.parse_args(arglist)
    return args

def recommend_destinations(df, destination, budget, important_factor):
    travel_obj = Travel(destination, budget, important_factor)
    recommended_destinations = travel_obj.recommend(df, budget, important_factor)
    print(f"\nRecommended destinations for your budget and important factor ({important_factor}):")
    for idx, row in recommended_destinations.iterrows():
        print(f"- {row['Destination']} ({row['Budget']} budget, important: {row['Important (optional)']})")
    return recommended_destinations


def display_discounted_price(recommended_destinations):
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
    user_input = input("Enter destination, budget, and important_factor (optional, default: price): ")
    inputs = user_input.split()
    
    destination = inputs[0]
    budget = int(inputs[1])
    important_factor = inputs[2] if len(inputs) > 2 else "Price"
    
    return destination, budget, important_factor
     
def main(filepath, destination, budget, important_factor="price"):
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

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.destination, args.budget, args.important)