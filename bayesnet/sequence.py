# Author: Bonnie Zhu
# Date: January 14
# Description: This script performs rejection sampling to estimate
#              the distribution of attending an appointment given 
#              that the train is delayed. It uses a Bayesian 
#              Network from the pomegranate library. © CS50

from model import model

# Observed data
observations = [
    "umbrella",
    "umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella"
]

# Predict underlying states
predictions = model.predict(observations)
for prediction in predictions:
    print(model.states[prediction].name)