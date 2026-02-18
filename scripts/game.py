# NOTE: Whenver code tutorial says display, replace this word with screen as per pygame terminology.

import sys

import pygame # This line imports the pygame module to actually run the game. 

from scripts.utils import load_image, load_images # This line imports the load_image function from the utils.py file in the scripts folder.
from scripts.Entities import PhysicsEntity 
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds # This line imports the Clouds class from the clouds.py file in the scripts folder. The Clouds class is used to create and manage clouds in the game.

class Game: # We make the Game code into a class of its own to be called in the future
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Ninja Game") # This line of code sets the title of the game as Ninja Game
        self.screen = pygame.display.set_mode((640, 480)) # This line sets the display for the gmae as 640,480 pixels

        self.screen = pygame.Surface((320,240)) 

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'), 
            'stone': load_images('tiles/stone'),
            'spawners': load_images('tiles/spawners'),
            'player': load_image('entities/player.png'), # Load the player image using the load_image function from utils.py
            'background': load_image('background.png'),
            'clouds': load_images('clouds'), # Load the cloud images using the load_images function from utils.py
        }

        print(self.assets) # This line prints the assets dictionary to the console to check if the images are loaded correctly.

        self.clouds = Clouds(self.assets['clouds'], count = 16) # create a Clouds instance with the loaded cloud images

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))  # create the player PhysicsEntity: pass game reference, entity type, starting position (x, y), and size (width, height)

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0] # initialize camera scroll values for x and y axes


    def run(self): # This function makes the loop in its own function which can be called in the future
        while True:
            self.screen.blit(self.assets['background'], (0, 0)) # Draw the background image onto the screen at position (0, 0)

            self.scroll[0] +=(self.player.rect().centerx - self.screen.get_width() / 2 - self.scroll[0]) / 30 # The self.screen.get_width part of the code essentially cuts the screen's size by half so that the camera ends up tracking the player and not somewhere else. update horizontal scroll based on player position. As the camera is linked to the player's position
            self.scroll[1] +=(self.player.rect().centery - self.screen.get_height() / 2 - self.scroll[1]) / 30 # update vertical scroll based on player position
            render_scroll = (int(self.scroll[0]), int(self.scroll[1])) # create a tuple of integer scroll values for rendering. This is a key line of code as if we run the game without this code, the player gets jittery as the player's position and tiles position are float values not integer values.

            self.clouds.update() # update the clouds' positions
            self.clouds.render(self.screen, offset = render_scroll) # render the clouds onto the

            self.tilemap.render(self.screen, offset = self.scroll) # render the tilemap onto the screen with the current scroll offset. The scroll offset is the camera position in the game world. 

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))  # update player with vertical movement input
            self.player.render(self.screen, offset = self.scroll)  # render player with current scroll offset
           
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # This whole if statement is for when the user wants to quit the game. 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # This whole if statement is for when the user presses a key down.
                    if event.key == pygame.K_LEFT: # If the key pressed is the UP arrow key
                        self.movement[0] = True # Set the first index of the movement list to True
                    if event.key == pygame.K_RIGHT: # If the key pressed is the DOWN arrow key
                        self.movement[1] = True # Set the second index of the movement list to True
                    if event.key == pygame.K_UP: 
                        self.player.velocity[1] = -3 # Set the player's vertical velocity to -3 to make it jump to make the jumping physics work
                if event.type == pygame.KEYUP: # This whole if statement is for when the user releases a key.
                    if event.key == pygame.K_LEFT: # If the key released is the UP arrow key
                        self.movement[0] = False # Set the first index of the movement list to False
                    if event.key == pygame.K_RIGHT: #` If the key released is the DOWN arrow key
                        self.movement[1] = False    # Set the second index of the movement list to False
            pygame.display.update() # This just updates the display if it quits. 
            self.clock.tick(60) # The clock.tick(60) sets the original FPS of the game as 60 FPS. 

Game().run() # This function runs the game. Without it, the game will not run. It is the essential part of the code. 


