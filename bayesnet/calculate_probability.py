from model import model

# Calculate probability for a given observation
# Observation format: [rain, maintenance, train, appointment]
# Example: ["none", "no", "on time", "attend"]
probability = model.probability([["none", "no", "on time", "attend"]])

# Print the calculated probability
print(probability)

