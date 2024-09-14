"""
Name: Khalil Kilani
Course: CSCI 3725
Assignment: M3: A Markov Distinction
Date: September 17, 2024
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image

SEQUENCE_LEN = 3

class MarkovChain:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.states = list(transition_matrix.keys())
    
    def get_next_state(self, current_state):
        return random.choices(
            self.states, weights=[self.transition_matrix[current_state][next_state] for next_state in self.states]
            )
    
    def generate_sequence(self, sequence_len):
        current_state = random.choice(self.states)
        generated_sequence = []
        
        while len(generated_sequence) < sequence_len:
            next_state = (self.get_next_state(current_state))[0]  # unpack list of 1 item
            generated_sequence.append(next_state)
            current_move = next_state

        return generated_sequence

class Flag:
    def __init__(self, color_theme, pattern, symbol):
        self.color_theme = color_theme
        self.pattern = pattern
        self.symbol = symbol

def create_flag():
    return

def main():
    flag_color_themes = {
        "Pan-Arab" : {"Pan-Arab" : 0, "Pan-African" : 0, "Pan-Slavic" : 0, "Pan-Iranian" : 0, "Miranda" : 0, "Belgrano" : 0, "Red-White Family" : 0},
        "Pan-African" : {"Pan-Arab" : 0, "Pan-African" : 0, "Pan-Slavic" : 0, "Pan-Iranian" : 0, "Miranda" : 0, "Belgrano" : 0, "Red-White Family" : 0},
        "Pan-Slavic" : {"Pan-Arab" : 0, "Pan-African" : 0, "Pan-Slavic" : 0, "Pan-Iranian" : 0, "Miranda" : 0, "Belgrano" : 0, "Red-White Family" : 0},
        "Pan-Iranian" : {"Pan-Arab" : 0, "Pan-African" : 0, "Pan-Slavic" : 0, "Pan-Iranian" : 0, "Miranda" : 0, "Belgrano" : 0, "Red-White Family" : 0},
        "Miranda" : {"Pan-Arab" : 0, "Pan-African" : 0, "Pan-Slavic" : 0, "Pan-Iranian" : 0, "Miranda" : 0, "Belgrano" : 0, "Red-White Family" : 0},
        "Belgrano" : {"Pan-Arab" : 0, "Pan-African" : 0, "Pan-Slavic" : 0, "Pan-Iranian" : 0, "Miranda" : 0, "Belgrano" : 0, "Red-White Family" : 0},
        "Red-White Family" : {"Pan-Arab" : 0, "Pan-African" : 0, "Pan-Slavic" : 0, "Pan-Iranian" : 0, "Miranda" : 0, "Belgrano" : 0, "Red-White Family" : 0},
    }
    
    flag_patterns = {
        "Horizontal Stripes" : {"Horizontal Stripes" : 0, "Vertical Stripes" : 0, "Diagonal Stripes" : 0},
        "Vertical Stripes" : {"Horizontal Stripes" : 0, "Vertical Stripes" : 0, "Diagonal Stripes" : 0},
        "Diagonal Stripes" : {"Horizontal Stripes" : 0, "Vertical Stripes" : 0, "Diagonal Stripes" : 0},
    }
    
    flag_symbols = {
        "Star" : {"Star" : 0, "Shield" : 0, "Bear" : 0, "Flower" : 0},
        "Shield" : {"Star" : 0, "Shield" : 0, "Bear" : 0, "Flower" : 0},
        "Bear" : {"Star" : 0, "Shield" : 0, "Bear" : 0, "Flower" : 0},
        "Flower" : {"Star" : 0, "Shield" : 0, "Bear" : 0, "Flower" : 0}
    }
    
    properties = [flag_color_themes, flag_patterns, flag_symbols]
    generated_sequences = []
    
    for property in properties:
        property_maker = MarkovChain(property)
        new_sequence = property_maker.generate_sequence(SEQUENCE_LEN)
        generated_sequences.append(new_sequence)
    
    flag_tuples = zip(*generated_sequences)
    print(flag_tuples)

if __name__ == "__main__":
    main()