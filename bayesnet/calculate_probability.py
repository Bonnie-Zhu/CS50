# Author: Bonnie Zhu
# Date: January 14
# Description:Uses the Bayesian Network model to calculate the probability of a given observation.

from model import model

def calculate_probability(observation):
    """
    Calculate the probability of a given observation.
    
    Args:
        observation (list): A list of observed values in the format:
                            [rain, maintenance, train, appointment]
    
    Returns:
        float: The probability of the observation.
    """
    probability = model.probability([observation])
    return probability

# Example usage
observation = ["none", "no", "on time", "attend"]
prob = calculate_probability(observation)
print(f"Probability of the observation {observation}: {prob}")
