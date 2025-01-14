# Author: Bonnie Zhu
# Date: January 14
# Description: This script performs rejection sampling to estimate
#              the distribution of attending an appointment given 
#              that the train is delayed. It uses a Bayesian 
#              Network from the pomegranate library. © CS50

import pomegranate
from collections import Counter
from model import model

def generate_sample():
    """
    Generate a single sample from the Bayesian Network.
    Returns:
        sample (dict): A mapping of variable names to their sampled values.
    """
    # Mapping of random variable name to sample generated
    sample = {}

    # Mapping of distribution to sample generated
    parents = {}

    # Loop over all states, assuming topological order
    for state in model.states:
        # If we have a non-root node, sample conditional on parents
        if isinstance(state.distribution, pomegranate.ConditionalProbabilityTable):
            sample[state.name] = state.distribution.sample(parent_values=parents)
        # Otherwise, just sample from the distribution alone
        else:
            sample[state.name] = state.distribution.sample()

        # Keep track of the sampled value in the parents mapping
        parents[state.distribution] = sample[state.name]

    # Return generated sample
    return sample

# Rejection sampling
# Compute distribution of Appointment given that train is delayed
N = 10000  # Number of samples to generate
data = []  # List to store relevant samples
for i in range(N):
    # Generate a sample
    sample = generate_sample()
    # Append the appointment outcome if the train is delayed
    if sample["train"] == "delayed":
        data.append(sample["appointment"])

# Print the distribution of appointment outcomes
print(Counter(data))
