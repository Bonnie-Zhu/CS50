# Author: Bonnie Zhu
# Date: January 15, 2025
# Description: Defines a logical model to determine if it is raining based on given conditions using symbols for rain, Hagrid, and Dumbledore.

from knowledge.logic_model import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))