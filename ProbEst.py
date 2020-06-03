# Christian Nelson
# 6/02/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #4 ProbEst

# Import pandas
import pandas as pd
from pandas import DataFrame

# load in 'cars.csv' into DataFrame
cars_dataframe = pd.read_csv('cars.csv')

# Function for computing conditional probability
def compute_conditional_probability(make, aspiration):
    # Get number of instances of aspiration given make cast to float for division
    number_instances = float(len(cars_dataframe[(cars_dataframe.make == make) & (cars_dataframe.aspiration == aspiration)]))
    # Get total number of instances of make
    make_count = float(len((cars_dataframe[cars_dataframe.make == make])))
    # Calculate conditional probability
    conditional_probability = (number_instances / make_count)
    # Return condition probability
    return conditional_probability

conditional_probability = compute_conditional_probability('audi','std')

print(conditional_probability)
