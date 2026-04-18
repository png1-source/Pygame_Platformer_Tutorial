# NOTE: Whenver code tutorial says display, replace this word with screen as per pygame terminology.

import sys

import pygame # This line imports the pygame module to actually run the game. 

from scripts.utils import load_images 
from scripts.tilemap import Tilemap

RENDER_SCALE = 2.0


class Editor: # We make the Game code into a class of its own to be called in the future
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("editor") # This line of code sets the title of the game as Ninja Game
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240)) 

        self.clock = pygame.time.Clock()

        

        self.assets = { # Loading all the assets for the game in a dictionary for easy access. They keys of the dictionary are the names of the assets and the values are the loaded images or animations.
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'), 
            'stone': load_images('tiles/stone'),
        }

        self.movement = [False, False, False, False] # This list will be used to track the movement of the player. The first index will be for left movement and the second index will be for right movement.

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0] # initialize camera scroll values for x and y axes


    def run(self): # This function makes the loop in its own function which can be called in the future
        while True:
            self.display.blit((0,0,0)) # Fill the display surface with black color to clear the previous frame before drawing the new frame. This is necessary to prevent visual artifacts from previous frames from appearing on the screen.

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # This whole if statement is for when the user wants to quit the game. 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # This whole if statement is for when the user presses a key down.
                    if event.key == pygame.K_LEFT: # If the key pressed is the UP arrow key
                        self.movement[0] = True # Set the first index of the movement list to True
                    if event.key == pygame.K_RIGHT: # If the key pressed is the DOWN arrow key
                        self.movement[1] = True # Set the second index of the movement list to True
                    if event.key == pygame.K_UP: # If the key pressed is the UP arrow key
                        self.movement[2] = True # Set the third index of the movement list to True
                    if event.key == pygame.K_DOWN: # If the key pressed is the DOWN arrow key
                        self.movement[3] = True # Set the fourth index of the movement list to True
                if event.type == pygame.KEYUP: # This whole if statement is for when the user releases a key.
                    if event.key == pygame.K_LEFT: # If the key released is the UP arrow key
                        self.movement[0] = False # Set the first index of the movement list to False
                    if event.key == pygame.K_RIGHT: #` If the key released is the DOWN arrow key
                        self.movement[1] = False    # Set the second index of the movement list to False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)) 
            pygame.display.update() # Update the full display surface to the screen. This is necessary to actually see the changes made to the display surface on the screen.
            self.clock.tick(60) # The clock.tick(60) sets the original FPS of the game as 60 FPS. 

Editor().run() # This line creates an instance of the Editor class and calls its run method to start the editor loop.


