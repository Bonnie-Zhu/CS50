# 
# Author: Bonnie Zhu
# Date: January 14
# Description: This script calculates the probability of a specific 
#              observation in a Bayesian Network using the 
#              `probability` method from the pomegranate library. © CS50

from model import model

# Calculate probability for a given observation
# Observation format: [rain, maintenance, train, appointment]
# Example: ["none", "no", "on time", "attend"]
probability = model.probability([["none", "no", "on time", "attend"]])

# Print the calculated probability
print(probability)
