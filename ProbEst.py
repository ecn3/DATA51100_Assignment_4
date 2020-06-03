# Christian Nelson
# 6/02/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #4 ProbEst

# Import pandas
import pandas as pd
from pandas import DataFrame

# Formats
fm1 = "Prob(aspiration={}|make={}) = {z:.2f}%"
fm2 = "Prob(make={}) = {j:.2f}%"

# load in 'cars.csv' into DataFrame
cars_dataframe = pd.read_csv('cars.csv')

# Get total number of instances
instances_count = float(len(cars_dataframe))

# Function for computing conditional probability
def compute_conditional_probability(make, aspiration):
    # Get number of instances of aspiration given make cast to float for division
    number_instances = float(len(cars_dataframe[(cars_dataframe.make == make) & (cars_dataframe.aspiration == aspiration)]))
    # Get total number of instances of make
    make_count = float(len((cars_dataframe[cars_dataframe.make == make])))
    # Calculate conditional probability
    conditional_probability = (number_instances / make_count)
    # Return condition probability as percentage
    return (conditional_probability * 100)

# Function for computing probability of each make
def compute_make_probability(make):
    # Get total number of instances of make
    make_count = float(len((cars_dataframe[cars_dataframe.make == make])))
    # Calculate probability
    make_probability = (make_count / instances_count)
    # Return condition probability as percentage
    return (make_probability * 100)


# Get the unique makes and aspirations
makes = cars_dataframe.make.unique()
aspirations = cars_dataframe.aspiration.unique()

# Output
# Header info
print("DATA-51100, SUMMER 2020")
print("Christian Nelson")
print("PROGRAMMING ASSIGNMENT #4\n")

# Iterate over each aspiration calculate cond prob of each make
for x in makes:
    for y in aspirations:
        conditional_probability = compute_conditional_probability(x,y)
        # Print conditional probabilities to the screen
        print(fm1.format(y,x,z=conditional_probability))

# Print empty  line
print('')

# Iterate over each make calculate prob of each make
for i in makes:
        make_probability = compute_make_probability(i)
        # Print conditional probabilities to the screen
        print(fm2.format(i,j=make_probability))
