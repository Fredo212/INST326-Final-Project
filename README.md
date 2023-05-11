# PLATINUM TEAM FINAL REPORT
### NAME: Joel Cohen, Younju Kim, Allison Aki Parrish, Alfred Mbah
- - -
1.  An explanation of the purpose of each file in your repository
    * Destinations_File.csv: Dataset for using pandas in our code. There are 11 rows of data, including destination, budget, and important_factor
    * PlatinumFinalProject.py: Code for the final project using each function.
    * README.md: A description of our script and it also has documentation for our final project.
2. Clear instructions on how to run your program from the command line
    * The part where the user enters data for the first time:
      * In Mac: In Mac: python3 PlatinumFinalProject.py Destinations_File.csv [destination] [budget] [important_factor(this is optional, can skip)] example) python3 PlatinumFinalProject.py Destinations_File.csv Mexico 500 -i Food or python3 PlatinumFinalProject.py Destinations_File.csv Mexico 500 (important_factor is skipped)
      * In Windows: python PlatinumFinalProject.py Destinations_File.csv [destination] [budget] [important_factor(this is optional, can skip)] example) python PlatinumFinalProject.py Destinations_File.csv Japan 1000 -i Price or python PlatinumFinalProject.py Destinations_File.csv Japan 1000 (important_factor is skipped)
    * Then, the user can choose to input an answer in the command-line. Here are three options to answer in command-line: "yes", "no", and other characters or phrases.
3. Clear instructions on how to use your program and/or interpret the output of the program, as applicable
    * The output where the user enters data for the first time:
      * Displays all data stored from the csv file. It also recommends a value that is a budget difference of +-300 filtered according to the budget entered by the user and the important_factor.
    * The output, if the user chooses ‘yes’ option in command-line:
      * The program will display the previous recommendations with their respective discounted prices.
    * The output, if the user chooses 'no' option in command-line:
      * The user will have another chance to enter a new destination, budget, and important_factor to search flight again.
    * The output, if the user chooses any words or alphabets in command-line:
      * Any other input other than "yes" or "no" will terminate the program
4. Attribution: in order to evaluate whether each member has made a substantial, original contribution to the project, please provide a table like this:

|METHOD/FUNCTION|NAME (Primary author)|Techniques demonstrated|
|------|---|---|
|SUPER/__init__(Vacation class)|Joel Cohen|Super() is used to avoid repetition in the __init__ of the child class. Since a vacation is similar to Travel, there are the same constraints, leaving __init__ to take the same parameters, meaning we can just use the parent (Travel) __init__. The same goes for the recommended function.|
|F-strings containing expressions/recommend_destinations and display_discounted_price|Joel Cohen|Uses an f-string to include the value of the ‘important_factor’ variable in the printed message. Implemented * .80 to make a discount. So it is not just an expression; the f-string has some calculations.|
|Magic methods/repr(),str(),and lt()|Younju Kim|__repr__ method returns a string representation of the Travel object. It is called when the ‘repr()’ function is used on an instance of the class. __str__ method returns a human-readable string representation of the Travel object. It is called when the ‘str()’ function is used on an instance of the class. __lt__() method defines a less-than comparison between two Travel objects based on their budgets. It is used to compare objects using the ‘<’ operator.|
|with statement/from_file()|Younju Kim|Read file using pandas and iteration.|
|Conditional statements/get_user_input() and main()|Younju Kim|In the main function, the program presents two options to a user with the answer such as yes or no. In the get_user_input function, this method checks the length of the ‘inputs’ list to determine if an important factor was provided by the user.|
|Sequence unpacking/get_user_input|Younju Kim|In the get_user_input function, this method is used in the line ‘destination, budget, important_factor = inputs’. It assigns the values from the ‘inputs’ list to the variables ‘destination’, ‘budget’, and ‘important_factor’ using sequence unpacking.|
|__init__(), recommend()|Allison Aki Parrish|Optional parameter in recommend function (‘important’ parameter set to “price”)|
|recommend|Allison Aki Parrish|Filtering on Pandas df in order to achieve the user’s demanded destination from the dataframe|
|parse_args()|Alfred Mbah|the ArgumentParser class from the argparse module|
|recommend_destinations()|Alfred Mbah| List comprehension: This method is used to generate the string representation of recommended destinations. The comprehension iterates over the rows of the DataFrame and constructs the desired string format. The resulting strings are joined using the newline character ‘\n.’|
