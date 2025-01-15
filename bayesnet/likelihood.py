# 
# Author: Bonnie Zhu
# Date: January 14
# Description: This script calculates the probability of a specific 
#              observation in a Bayesian Network using the 
#              `probability` method from the pomegranate library. © CS50

# likelihood.py
from bayesian_network import model

# Example observation: [rain, maintenance, train, appointment]
observation = [["none", "no", "on time", "attend"]]

# Calculate probability
probability = model.probability(observation)
print(f"Likelihood of the observation {observation}: {probability}")
