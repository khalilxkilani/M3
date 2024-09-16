# M3: A Markov Distinction
CSCI 3725: Computational Creativity\
Khalil Kilani\
September 17, 2024

# Flags from an Imaginary World

***

### 1.) How to Set up and Run the Code
1.) Download a zip file of the project from GitHub.\
2.) Unzip the file.\
3.) Open the file named "flag-gen-markov.py" in Visual Studio Code.\
4.) **Optional:** change the constant named "SEQUENCE_LEN" to produce a longer or shorter sequence of flags. The grid size and padding will automatically adjust.\
5.) Run the file named "flag-gen-markov.py" in an interactive window. To do so, click the small arrow next to the play button in the top-left corner of the Visual Studio Code menu bar and select "Run Current File in Interactive Window." This will open a separate window to display the generated flags.\
6.) Repeat!

### 2.) Description
This system produces flag designs using Markov chains. The visual artifacts consider the four flag properties listed below, so the system has four transition matrices in total. The flags are assembled by drawing rectangles atop a blank canvas, filling the rectangles with the required colors, centering a symbol upon the top layer, and adding a border. The system displays the generated flags to the user in a grid format. All the dimensions within the system change dynamically, meaning that the size of the flags, patterns, and grid are programmed to adjust to the user-defined constants.

- **Flag Patterns:**
    * Horizontal stripes and vertical stripes

- **Flag Pattern Repetitions:**
    * 2, 3, 4, and 9

- **Flag Symbols:**
    * Star (black and white), bear (grizzly and polar), flower (red, orange, and monochrome), and shield

- **Flag Color Themes:**
    * Pan-Arab (black, red, dark green)
    * Pan-African (dark green, gold, red)
    * Pan-Slavic (white, blue, red)
    * Pan-Iranian (white, red, yellow green)
    * Miranda (gold, medium blue, red)
    * Belgrano (medium blue, white, powder blue)
    * Red-White Family (red, white, maroon)

### 3.) Personal Meaning
This system is personally meaningful because I enjoy learning about flag designs, national capitals, and world geography. Additionally, I often play trivia games to memorize different flag designs. As I have a passion for international affairs and hope to pursue a career as a U.S. diplomat, I must be adept at recognizing different national symbols. For example, when I worked at the Department of State this past summer, foreign dignitaries and delegates would wear friendship pins with their nation's flag alongside the U.S. flag. Another example is how my colleagues often referred to nations by their capital rather than country name. What fascinates me most about national flag designs is the different "families" like the Pan-Arab or the Pan-African flags. These designs share color schemes and patterns rooted in symbolic history that depict a sense of cultural unity despite ongoing geopolitical conflicts.

### 4.) Challenges
* I pushed myself outside my comfort zone by pursuing a visual graphic topic not taught in class and being intentional about my organizational approach. To explain, I began by drawing my ideas on paper, programming a framework using hard-coded values, and then generalizing the approach to work for all values. The most challenging aspect of generalizing the functions for all values was working with coordinates on the drawing canvas. For example, the libraries I used did not have a method to center an image atop another or consecutively draw shapes, so I needed to calculate it all mathematically. Another example is how images may not have the same local file path on different machines. These issues required me to extensively read the documentation for the libraries I imported, honing my skills as a computer scientist to translate manual instructions into working programs. Another way I pushed myself was by opting to draw the rectangular patterns rather than using pre-made images of rectangles. I also researched articles about flags to understand which flag properties my system should consider to produce flags that are unique yet grounded in realistic styles.

* This project was an important challenge because it strengthened my ability to build a project without set instructions or final product. At first, the freedom of the assignment's broad guidelines made me very nervous as I had never built a project based on my accord. Rather than panic, I applied everything the computer science major has taught me. For example, I thoroughly defined my programming approach like in Data Structures, used GitHub efficiently to track changes like in Systems, and researched how libraries worked like in Principles of Programming Languages.

* The next steps for me going forward are to gamify the system, introduce user input, and include more flag properties. I plan to gamify the system by prompting the user to guess which region of the world each flag could belong to. Then, the system would reveal which flag properties it considered during flag generation. I can also introduce more user input to the system by prompting the user to choose the flag dimensions, starting state, and grid format. The new flag properties I hope to introduce are text, diagonal patterns, and non-rectangular flag shapes.

### 5.) Creativity
I believe that my system is creative because it is both novel and valuable. This system is novel because it generates unique flag designs that no nation currently uses. This system is valuable because its visual artifacts are realistic and rooted in historical themes. Overall, the system mainly qualifies as "P Creative" because it is psychologically creative for the individual user. However, I envision that this system could become "H-Creative" and benefit society if it solves modern problems relating to symbols of national identity. For example, my home state of Maine recently held a contest to redesign the state flag. There were over 400 submissions, and the winning design will either be adopted or rejected in a November 2024 ballot. If my system accounted for Maine's cultural and historical identity, it could produce flag designs meaningful to Mainers.

### 6.) Sources
* "The World's Flags, in 7 Charts" on [The Washington Post](https://www.washingtonpost.com/news/wonk/wp/2016/04/07/the-worlds-flags-in-7-charts/)
* "Flying Colors" on [The New York Times](https://www.nytimes.com/2023/08/20/briefing/state-flags.html)
* "Here is a look at the new state flag design Mainers will vote on this November" on [Maine Morning Star](https://mainemorningstar.com/briefs/here-is-a-look-at-the-new-state-flag-design-mainers-will-vote-on-this-november/)
* "Drawing Shapes on Images with Python and Pillow" on [Mouse Vs Python](https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/)
* "Pillow 10.4.0 Documentation" on [Pillow](https://pillow.readthedocs.io/en/stable/index.html)
* "Matplotlib 3.9.2 Documentation" on [Matplotlib](https://matplotlib.org/stable/index.html)
* "Markdown and Visual Studio Code" on [Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
* "Find the Current Directory and Executed File’s Directory in Python" on [Sentry](https://sentry.io/answers/find-the-current-directory-and-executed-file-s-directory-in-python/)
* "[600px Black star White background](https://commons.wikimedia.org/w/index.php?curid=49939362)" by [Blackcat](https://commons.wikimedia.org/wiki/User:Blackcat) is marked with [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.en?ref=openverse)
* "[File:600px White star on Black background.svg](https://commons.wikimedia.org/w/index.php?curid=46329297)" by Blackcat is marked with CC0 1.0
* "[Bear clipart, wild animal illustration](https://www.rawpixel.com/image/6286373/vector-public-domain-illustrations)" is marked with [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse)
* "[Polar bear baby clipart, wild](https://www.rawpixel.com/image/6285856/vector-sticker-public-domain-illustrations)" is marked with [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse)
* "[Blank shield with border](https://commons.wikimedia.org/w/index.php?curid=62442940)" by [Wikimandia](https://commons.wikimedia.org/wiki/User:Wikimandia) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/?ref=openverse)
* "[Red flowers clipart, spring illustration](https://www.rawpixel.com/image/6334793/psd-plant-flowers-sticker)" is marked with [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse)
* "[Flower illustration](https://www.rawpixel.com/image/9069754/image-rose-flower-plant)" is marked with [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse)
* "[Flower collage element psd](https://www.rawpixel.com/image/7646965/psd-flower-plant-pattern)" is marked with [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse)
