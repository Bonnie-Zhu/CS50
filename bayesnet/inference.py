# Author: Bonnie Zhu
# Date: January 14
# Description: This script uses a model to calculate and print 
#              predictions based on the input state of "train: delayed."
#              © CS50

from model import model

# Calculate predictions
predictions = model.predict_proba({
    "train": "delayed"
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")
