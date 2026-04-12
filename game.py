# NOTE: Whenver code tutorial says display, replace this word with screen as per pygame terminology.

import sys

import pygame # This line imports the pygame module to actually run the game. 

from scripts.utils import load_image, load_images, Animation # This line imports the load_image function from the utils.py file in the scripts folder.
from scripts.entities import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds # This line imports the Clouds class from the clouds.py file in the scripts folder. The Clouds class is used to create and manage clouds in the game.

class Game: # We make the Game code into a class of its own to be called in the future
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Ninja Game") # This line of code sets the title of the game as Ninja Game
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240)) 

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = { # Loading all the assets for the game in a dictionary for easy access. They keys of the dictionary are the names of the assets and the values are the loaded images or animations.
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'), 
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'), # Load the player image using the load_image function from utils.py
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur = 6),
            'player/run': Animation(load_images('entities/player/run'), img_dur = 4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
        }

      

        self.clouds = Clouds(self.assets['clouds'], count = 16) # create a Clouds instance with the loaded cloud images

        self.player = Player(self, (50, 50), (8, 15))  # create the player PhysicsEntity: pass game reference, entity type, starting position (x, y), and size (width, height)

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0] # initialize camera scroll values for x and y axes


    def run(self): # This function makes the loop in its own function which can be called in the future
        while True:
            self.display.blit(self.assets['background'], (0, 0)) # Draw the background image onto the screen at position (0, 0)

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1])) # create a tuple of integer scroll values for rendering. This is a key line of code as if we run the game without this code, the player gets jittery as the player's position and tiles position are float values not integer values.

            self.clouds.update() # update the clouds' positions
            self.clouds.render(self.display, offset=render_scroll)

            self.tilemap.render(self.display, offset = render_scroll) # render the tilemap onto the display with the current scroll offset. The scroll offset is the camera position in the game world. 

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)
           
            
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

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)) 
            pygame.display.update() # Update the full display surface to the screen. This is necessary to actually see the changes made to the display surface on the screen.
            self.clock.tick(60) # The clock.tick(60) sets the original FPS of the game as 60 FPS. 

Game().run() # This function runs the game. Without it, the game will not run. It is the essential part of the code. 


