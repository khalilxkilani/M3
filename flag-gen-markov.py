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
        "Pan-Arab" : {"Pan-Arab" : 0.1, "Pan-African" : 0.2, "Pan-Slavic" : 0.3, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-African" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.2, "Pan-Iranian" : 0.3, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-Slavic" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.2, "Miranda" : 0.3, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-Iranian" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.2, "Belgrano" : 0.3, "Red-White Family" : 0.1},
        "Miranda" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.2, "Red-White Family" : 0.3},
        "Belgrano" : {"Pan-Arab" : 0.4, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Red-White Family" : {"Pan-Arab" : 0.1, "Pan-African" : 0.2, "Pan-Slavic" : 0.2, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
    }
    
    flag_patterns = {
        "Horizontal Stripes" : {"Horizontal Stripes" : 0.4, "Vertical Stripes" : 0.2, "Diagonal Stripes" : 0.4},
        "Vertical Stripes" : {"Horizontal Stripes" : 0.1, "Vertical Stripes" : 0.4, "Diagonal Stripes" : 0.5},
        "Diagonal Stripes" : {"Horizontal Stripes" : 0.5, "Vertical Stripes" : 0.2, "Diagonal Stripes" : 0.3},
    }
    
    flag_symbols = {
        "Star" : {"Star" : 0.4, "Shield" : 0.1, "Bear" : 0.3, "Flower" : 0.2},
        "Shield" : {"Star" : 0.2, "Shield" : 0.1, "Bear" : 0.5, "Flower" : 0.2},
        "Bear" : {"Star" : 0.5, "Shield" : 0.2, "Bear" : 0.1, "Flower" : 0.2},
        "Flower" : {"Star" : 0.2, "Shield" : 0.3, "Bear" : 0.1, "Flower" : 0.4}
    }
    
    properties = [flag_color_themes, flag_patterns, flag_symbols]
    generated_sequences = []
    
    for property in properties:
        property_maker = MarkovChain(property)
        new_sequence = property_maker.generate_sequence(SEQUENCE_LEN)
        # print(new_sequence) # DEBUGGER
        generated_sequences.append(new_sequence)
    
    # print(generated_sequences) # DEBUGGER
    flag_tuples = tuple(zip(*generated_sequences))
    
    print(flag_tuples) # DEBUGGER

if __name__ == "__main__":
    main()