# Author: Bonnie Zhu
# Date: January 14
# Description:Defines a Hidden Markov Model (HMM) with states for sun and rain, and their respective observation distributions.

# hidden_markov_model.py
from pomegranate import HiddenMarkovModel, DiscreteDistribution
import numpy as np

# Observation model for each state
sun = DiscreteDistribution({
    "umbrella": 0.2,
    "no umbrella": 0.8
})

rain = DiscreteDistribution({
    "umbrella": 0.9,
    "no umbrella": 0.1
})

states = [sun, rain]

# Transition model
transitions = np.array(
    [[0.8, 0.2],  # Tomorrow's predictions if today = sun
    [0.3, 0.7]]  # Tomorrow's predictions if today = rain
)

# Starting probabilities
starts = np.array([0.5, 0.5])

# Create the Hidden Markov Model
model = HiddenMarkovModel.from_matrix(
    transitions, states, starts,
    state_names=["sun", "rain"]
)
model.bake()
