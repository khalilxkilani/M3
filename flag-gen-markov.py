"""
Name: Khalil Kilani
Course: CSCI 3725
Assignment: M3: A Markov Distinction
Date: September 17, 2024
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image, ImageDraw

SEQUENCE_LEN = 3

flag_colors = {
    "Pan-Arab" : ["black", "red", "darkgreen"],
    "Pan-African" : ["darkgreen", "gold", "red"],
    "Pan-Slavic" : ["white", "blue", "red"],
    "Pan-Iranian" : ["white", "red", "yellowgreen"],
    "Miranda" : ["gold", "mediumblue", "red"],
    "Belgrano" : ["mediumblue", "white", "powderblue"],
    "Red-White Family" : ["red", "white", "maroon"]
}

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
    def __init__(self, pattern, color_theme, symbol):
        self.pattern = pattern
        self.color_theme = color_theme
        self.symbol = symbol

    def draw_flag(self):
        print(f"Pattern: {self.pattern}, Color Theme: {self.color_theme}, Symbol: {self.symbol}") # DEBUGGER
        
        image = Image.new("RGB", size=(417, 252))
        draw = ImageDraw.Draw(image)
        
        add_color_pattern(draw, self.pattern, self.color_theme)
        image.show()

def add_color_pattern(draw, flag_pattern, flag_color_theme):
    colors = flag_colors[flag_color_theme].copy() # without copy(), this would modify what is in the dict
    
    if flag_pattern == "Horizontal Stripes":
        coords = (0, 0, 417, 84) # coordinates for first rectangle
    elif flag_pattern == "Vertical Stripes":
        coords = (0, 0, 139, 252) # coordinates for first rectangle
    else:
        print(f"Error in add_pattern: case for {flag_pattern}")
    
    for i in range(3):
        if flag_pattern == "Horizontal Stripes":
            fill = random.choice(colors) # grab a random color from the current theme
            colors.remove(fill)
            draw.rectangle(coords, fill=fill)
            
            new_coords = (0, coords[1]+84, 417, coords[3]+84) # update coords by 84 px to move downward a third
            coords = new_coords
        elif flag_pattern == "Vertical Stripes":
            fill = random.choice(colors)
            colors.remove(fill)
            draw.rectangle(coords, fill=fill)
            
            new_coords = (coords[0]+139, 0, coords[2]+139, 252) # update coords by 139 px to move rightward a third
            coords = new_coords
        else:
            print(f"Error in add_pattern: case for {flag_pattern}")

def main():
    flag_patterns = {
        "Horizontal Stripes" : {"Horizontal Stripes" : 0.4, "Vertical Stripes" : 0.6},
        "Vertical Stripes" : {"Horizontal Stripes" : 0.6, "Vertical Stripes" : 0.4}
    }
    
    # flag_patterns = {
    #     "Horizontal Stripes" : {"Horizontal Stripes" : 0.4, "Vertical Stripes" : 0.2, "Diagonal Stripes" : 0.4},
    #     "Vertical Stripes" : {"Horizontal Stripes" : 0.1, "Vertical Stripes" : 0.4, "Diagonal Stripes" : 0.5},
    #     "Diagonal Stripes" : {"Horizontal Stripes" : 0.5, "Vertical Stripes" : 0.2, "Diagonal Stripes" : 0.3},
    # }
    
    flag_color_themes = {
        "Pan-Arab" : {"Pan-Arab" : 0.1, "Pan-African" : 0.2, "Pan-Slavic" : 0.3, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-African" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.2, "Pan-Iranian" : 0.3, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-Slavic" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.2, "Miranda" : 0.3, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-Iranian" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.2, "Belgrano" : 0.3, "Red-White Family" : 0.1},
        "Miranda" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.2, "Red-White Family" : 0.3},
        "Belgrano" : {"Pan-Arab" : 0.4, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Red-White Family" : {"Pan-Arab" : 0.1, "Pan-African" : 0.2, "Pan-Slavic" : 0.2, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
    }
    
    flag_symbols = {
        "Star" : {"Star" : 0.4, "Shield" : 0.1, "Bear" : 0.3, "Flower" : 0.2},
        "Shield" : {"Star" : 0.2, "Shield" : 0.1, "Bear" : 0.5, "Flower" : 0.2},
        "Bear" : {"Star" : 0.5, "Shield" : 0.2, "Bear" : 0.1, "Flower" : 0.2},
        "Flower" : {"Star" : 0.2, "Shield" : 0.3, "Bear" : 0.1, "Flower" : 0.4}
    }
    
    properties = [flag_patterns, flag_color_themes, flag_symbols]
    generated_sequences = []
    
    for property in properties:
        markov_chain = MarkovChain(property)
        new_sequence = markov_chain.generate_sequence(SEQUENCE_LEN)
        # print(new_sequence) # DEBUGGER
        generated_sequences.append(new_sequence)
    
    # print(generated_sequences) # DEBUGGER
    flag_tuples = tuple(zip(*generated_sequences))
    
    print(flag_tuples) # DEBUGGER
    
    for flag in flag_tuples:
        pattern, color_theme, symbol = flag # unpack the tuple of flag properties
        new_flag = Flag(pattern, color_theme, symbol) # create a flag object
        new_flag.draw_flag()
    
    # create_flag(("Horizontal Stripes", "Miranda", "Bear"))
    # create_flag(("Horizontal Stripes", "Pan-Slavic", "Flower"))
    # create_flag(("Horizontal Stripes", "Pan-Slavic", "Flower"))

if __name__ == "__main__":
    main()