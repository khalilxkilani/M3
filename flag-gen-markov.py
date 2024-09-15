"""
Name: Khalil Kilani
Course: CSCI 3725
Assignment: M3 - A Markov Distinction
Date: September 17, 2024

A Markov model that produces national flags as visual art using different color themes,
patterns, and symbols.
"""

import matplotlib.pyplot as plt
import random
import os
from PIL import Image, ImageDraw, ImageOps

SEQUENCE_LEN = 9 # desired length of generated flag sequence
WIDTH_PX = 400 # flag dimensions in pixels
HEIGHT_PX = 250 # flag dimensions in pixels
DIMENSION_MULTIPLIER = 2.5 # determines inches allocated to each flag in grid
NUM_COLS = 3 # number of columns in the grid

# translation of flag themes into PIL color names
flag_colors = {
    "Pan-Arab" : ["black", "red", "darkgreen"],
    "Pan-African" : ["darkgreen", "gold", "red"],
    "Pan-Slavic" : ["white", "blue", "red"],
    "Pan-Iranian" : ["white", "red", "yellowgreen"],
    "Miranda" : ["gold", "mediumblue", "red"],
    "Belgrano" : ["mediumblue", "white", "powderblue"],
    "Red-White Family" : ["red", "white", "maroon"]
}

symbol_images = [] # global container to hold symbol images after reading them in

class MarkovChain:
    def __init__(self, transition_matrix):
        """Creates a new MarkovChain object.

        Args:
            transition_matrix (dict): holds states and their transition probabilities.
        """
        
        self.transition_matrix = transition_matrix
        self.states = list(transition_matrix.keys())
    
    def get_next_state(self, current_state):
        """Obtains the next state in the transition matrix according to the current state.

        Args:
            current_state (str): the current state within the transition matrix.

        Returns:
            list: the next state according to the transition weights.
        """
        
        return random.choices(
            self.states, weights=[self.transition_matrix[current_state][next_state] for next_state in self.states]
            )
    
    def generate_sequence(self, sequence_len):
        """Generates a sequence of flag properties using a Markov chain.

        Args:
            sequence_len (int): desired length of sequence generation.

        Returns:
            list: a sequence of flag properties.
        """
        
        current_state = random.choice(self.states) # start at a random state
        generated_sequence = []
        
        while len(generated_sequence) < sequence_len:
            next_state = (self.get_next_state(current_state))[0]  # unpack list of 1 item
            generated_sequence.append(next_state)
            current_state = next_state

        return generated_sequence

class Flag:
    def __init__(self, pattern, color_theme, pattern_repeat, symbol):
        """Creates a new Flag object.

        Args:
            pattern (str): the pattern of the flag.
            color_theme (str): the color theme of the flag.
            pattern_repeat (str): the number of times the flag patterns should repeat.
            symbol (str): the symbol of the flag.
        """
        
        self.pattern = pattern
        self.color_theme = color_theme
        self.pattern_repeat = int(pattern_repeat) # cast pattern repeat value from str to int
        self.symbol = symbol

    def draw_flag(self):
        """Creates a new flag according to the flag properties produced by the Markov chain.

        Returns:
            Image: the newly created flag.
        """
        
        image = Image.new("RGB", size=(WIDTH_PX, HEIGHT_PX)) # create a new canvas
        draw = ImageDraw.Draw(image)
        
        self.add_color_pattern(draw)
        self.add_symbol(image)
        image = ImageOps.expand(image, border=5, fill="black") # add a black border to the flag
        # image.show() # NOTICE: uncomment if you want to view the flags as temporary files rather than grid
        return image

    def add_color_pattern(self, draw):
        """Adds a pattern to the flag and color it using the flag theme.

        Args:
            draw (ImageDraw): a drawing interface for the flag image.
        """
        
        colors = flag_colors[self.color_theme].copy() # without copy(), this would modify what is in the dict
        prev_color = None
        
        if self.pattern == "Horizontal Stripes":
            coords = (0, 0, WIDTH_PX, HEIGHT_PX/self.pattern_repeat) # coordinates for first rectangle
        elif self.pattern == "Vertical Stripes":
            coords = (0, 0, WIDTH_PX/self.pattern_repeat, HEIGHT_PX) # coordinates for first rectangle
        else:
            print(f"Error in add_pattern: case for {self.pattern}")
        
        for i in range(self.pattern_repeat):
            if self.pattern == "Horizontal Stripes":
                # grab a random color from the current theme, do not repeat colors consecutively
                fill = random.choice([color for color in colors if color != prev_color])
                draw.rectangle(coords, fill=fill)
                
                # update coords to move downward
                new_coords = (0, coords[1]+(HEIGHT_PX/self.pattern_repeat), 417, coords[3]+(HEIGHT_PX/self.pattern_repeat))
                coords = new_coords
                prev_color = fill
            elif self.pattern == "Vertical Stripes":
                # grab a random color from the current theme, do not repeat colors consecutively
                fill = random.choice([color for color in colors if color != prev_color])
                draw.rectangle(coords, fill=fill)
                
                # update coords to move rightward
                new_coords = (coords[0]+(WIDTH_PX/self.pattern_repeat), 0, coords[2]+(WIDTH_PX/self.pattern_repeat), 252)
                coords = new_coords
                prev_color = fill
            else:
                print(f"Error in add_pattern: case for {self.pattern}")
    
    def add_symbol(self, image):
        """Adds a symbol to the flag.

        Args:
            image (Image): the flag to paste the symbol onto.
        """
        
        if self.symbol in ["Bear", "Star", "Flower"]: # for symbols with multiple styles, select a random option
            symbol = random.choice(symbol_images[self.symbol])
        else:
            symbol = symbol_images[self.symbol]
        
        symbol.thumbnail((WIDTH_PX/1.5, HEIGHT_PX/1.5)) # make image smaller while maintaining scale ratio
        symbol_width, symbol_height = symbol.width, symbol.height
        
        # obtain the centered coords for the symbol
        centered_coords = ((WIDTH_PX//2)-symbol_width//2, (HEIGHT_PX//2)-symbol_height//2)        
        image.paste(symbol, box=centered_coords, mask=symbol) # paste the symbol onto the flag

def make_grid(num_rows, flag_images):
    """Creates a grid to hold all of the generated flags.

    Args:
        num_rows (int): number of rows in the grid.
        flag_images (list): the flag Image objects.
    """
    
    # create a figure and specify size in inches
    grid = plt.figure(figsize=(DIMENSION_MULTIPLIER * NUM_COLS, DIMENSION_MULTIPLIER * num_rows)) # 2.5 x 2.5 inch square allocated to each flag
    plt.rcParams["font.family"] = "serif" # change the font of the graphs 
    
    # add a subplot for each flag
    for i in range(0, SEQUENCE_LEN):
        grid.add_subplot(num_rows, NUM_COLS, i + 1) # add a subplot next to the prior one
        plt.imshow(flag_images[i])
        plt.title(f"Flag #{i+1}") # assign a number for each flag
        plt.axis("off")
    
    grid.suptitle("Flags from an Imaginary World", fontsize=24, weight="bold", color="black") # add a title
    grid.tight_layout() # fit subplots into grid bounds
    grid.show()

def main():
    global symbol_images
    flag_patterns = {
        "Horizontal Stripes" : {"Horizontal Stripes" : 0.4, "Vertical Stripes" : 0.6},
        "Vertical Stripes" : {"Horizontal Stripes" : 0.6, "Vertical Stripes" : 0.4}
    }
    
    flag_color_themes = {
        "Pan-Arab" : {"Pan-Arab" : 0.1, "Pan-African" : 0.2, "Pan-Slavic" : 0.3, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-African" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.2, "Pan-Iranian" : 0.3, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-Slavic" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.2, "Miranda" : 0.3, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Pan-Iranian" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.2, "Belgrano" : 0.3, "Red-White Family" : 0.1},
        "Miranda" : {"Pan-Arab" : 0.1, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.2, "Red-White Family" : 0.3},
        "Belgrano" : {"Pan-Arab" : 0.4, "Pan-African" : 0.1, "Pan-Slavic" : 0.1, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
        "Red-White Family" : {"Pan-Arab" : 0.1, "Pan-African" : 0.2, "Pan-Slavic" : 0.2, "Pan-Iranian" : 0.1, "Miranda" : 0.1, "Belgrano" : 0.1, "Red-White Family" : 0.1},
    }
    
    flag_num_repetitions = {
        "2" : {"2" : 0.2, "3" : 0.5, "4" : 0.2, "9" : 0.1},
        "3" : {"2" : 0.4, "3" : 0.4, "4" : 0.1, "9" : 0.1},
        "4" : {"2" : 0.2, "3" : 0.6, "4" : 0.1, "9" : 0.1},
        "9" : {"2" : 0.2, "3" : 0.5, "4" : 0.2, "9" : 0.1}
    }
    
    flag_symbols = {
        "Star" : {"Star" : 0.2, "Shield" : 0.1, "Bear" : 0.3, "Flower" : 0.4},
        "Shield" : {"Star" : 0.2, "Shield" : 0.1, "Bear" : 0.5, "Flower" : 0.2},
        "Bear" : {"Star" : 0.3, "Shield" : 0.4, "Bear" : 0.1, "Flower" : 0.2},
        "Flower" : {"Star" : 0.4, "Shield" : 0.2, "Bear" : 0.3, "Flower" : 0.1}
    }
    
    # reading in the images
    directory = os.path.dirname(os.path.realpath(__file__)) # get path to current directory to ensure images can be found when not working locally
    bear_image = Image.open(directory + "/graphics/bear.png") # prepend path to current directory to path of image
    polar_bear_image = Image.open(directory + "/graphics/polar-bear.png")
    white_star = Image.open(directory + "/graphics/white-star.png")
    black_star = Image.open(directory + "/graphics/black-star.png")
    red_flowers = Image.open(directory + "/graphics/red-flowers.png")
    orange_flower = Image.open(directory + "/graphics/orange-flower.png")
    bw_flower = Image.open(directory + "/graphics/bw-flower.png")
    shield = Image.open(directory + "/graphics/shield.png")
    
    symbol_images = {
        "Bear" : [bear_image, polar_bear_image],
        "Star" : [white_star, black_star],
        "Flower" : [red_flowers, orange_flower, bw_flower],
        "Shield" : shield
        }
    
    properties = [flag_patterns, flag_color_themes, flag_num_repetitions, flag_symbols]
    generated_sequences = []
    
    for property in properties:
        markov_chain = MarkovChain(property)
        new_sequence = markov_chain.generate_sequence(SEQUENCE_LEN)
        generated_sequences.append(new_sequence)
    
    flag_tuples = tuple(zip(*generated_sequences)) # create a tuple holding properties of each flag
    flag_images = []
    
    for flag in flag_tuples:
        pattern, color_theme, num_repetitions, symbol = flag # unpack the tuple of flag properties
        new_flag = Flag(pattern, color_theme, num_repetitions, symbol) # create a flag object
        new_flag_image = new_flag.draw_flag()
        flag_images.append(new_flag_image)
    
    num_rows = SEQUENCE_LEN // 3 # determine number of rows needed to fit all flags, round down
    if (SEQUENCE_LEN % 3) != 0: # if there is remainder of flags, add an extra row
        num_rows += 1
    
    make_grid(num_rows, flag_images)

if __name__ == "__main__": # only run main() if this is the main file
    main()