# Author: Bonnie Zhu
# Date: January 14
# Description: Defines a Bayesian Network with nodes for rain, train delays, and appointment attendance.
#              It sets up the conditional probability tables and creates the network."
#              © CS50
from pomegranate import ConditionalProbabilityTable, BayesianNetwork, State

# Define the distributions for each node
rain = ConditionalProbabilityTable([
    ["none", "yes", 0.4],
    ["none", "no", 0.6],
    ["light", "yes", 0.2],
    ["light", "no", 0.8],
    ["heavy", "yes", 0.1],
    ["heavy", "no", 0.9]
], [])

train = ConditionalProbabilityTable([
    ["none", "yes", "on time", 0.8],
    ["none", "yes", "delayed", 0.2],
    ["none", "no", "on time", 0.9],
    ["none", "no", "delayed", 0.1],
    ["light", "yes", "on time", 0.6],
    ["light", "yes", "delayed", 0.4],
    ["light", "no", "on time", 0.7],
    ["light", "no", "delayed", 0.3],
    ["heavy", "yes", "on time", 0.4],
    ["heavy", "yes", "delayed", 0.6],
    ["heavy", "no", "on time", 0.5],
    ["heavy", "no", "delayed", 0.5],
], [rain])

appointment = ConditionalProbabilityTable([
    ["on time", "attend", 0.9],
    ["on time", "miss", 0.1],
    ["delayed", "attend", 0.6],
    ["delayed", "miss", 0.4]
], [train])

# Create states for the Bayesian Network
rain_state = State(rain, name="rain")
train_state = State(train, name="train")
appointment_state = State(appointment, name="appointment")

# Create and bake the Bayesian Network
model = BayesianNetwork("Train and Appointment Example")
model.add_states(rain_state, train_state, appointment_state)
model.add_edge(rain_state, train_state)
model.add_edge(train_state, appointment_state)
model.bake()
