# Author: Bonnie Zhu
# Date: January 14
# Description: This script uses a model to calculate and print 
#              predictions based on the input state of "train: delayed."
#              © CS50

# inference.py
from bayesian_network import model as bayesian_model
from hidden_markov_model import model as hmm_model

# Bayesian Network Inference
predictions = bayesian_model.predict_proba({"train": "delayed"})
print("Bayesian Network Predictions:")
for node, prediction in zip(bayesian_model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")

# Hidden Markov Model Predictions
observations = ["umbrella", "no umbrella", "umbrella"]
predictions = hmm_model.predict(observations)
print("\nHidden Markov Model Predictions:")
for prediction in predictions:
    print(hmm_model.states[prediction].name)
