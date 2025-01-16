import math
import numpy as np
from scipy.spatial.distance import cosine

# Read the words and their vectors from the file
with open("words.txt") as f:
    words = dict()
    for line in f:
        row = line.split()
        word = row[0]
        vector = np.array([float(x) for x in row[1:]])
        words[word] = vector

# Function to calculate cosine distance between two vectors
def distance(w1, w2):
    return cosine(w1, w2)

# Function to find the closest words to a given embedding
def closest_words(embedding):
    distances = {
        w: distance(embedding, words[w])
        for w in words
    }
    return sorted(distances, key=lambda w: distances[w])[:10]

# Function to find the closest word to a given embedding
def closest_word(embedding):
    return closest_words(embedding)[0]

# Example usage:
# Assuming you have an embedding vector to compare
example_embedding = np.random.rand(100)  # Replace with actual 100-dimensional embedding vector
print("Closest words:", closest_words(example_embedding))
print("Closest word:", closest_word(example_embedding))