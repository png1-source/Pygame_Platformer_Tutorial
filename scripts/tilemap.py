# NOTE: Whenver code tutorial says display, replace this word with screen as per pygame terminology.

import pygame
NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)] # Offsets to check neighbouring tiles. These numbers are essentially pemutations of -1. 
PHYSICS_TILES = {'grass', 'stone'}  # Set of tile types that have physics properties (e.g., collision). Similar to defining a dictionary but instead there are no key value pairs. 

class Tilemap:
    def __init__(self, game, tile_size=16): # Initialize the tilemap with a specified tile size
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []
       

    def tiles_around(self,pos): # Get tiles around a given position
         tiles = []
         tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))  # Get the tile coordinates by dividing pixel position by tile size
         for offset in NEIGHBOR_OFFSETS: # This for loop goes through each offset in the NEIGHBOR_OFFSETS list
              check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1]) # Calculate the neighboring tile location as a string key
              if check_loc in self.tilemap:
                  tiles.append(self.tilemap[check_loc]) # If the tile exists in the tilemap, add it to the tiles list
         return tiles 
    
    def physics_rects_around(self, pos): # Get physics rectangles for tiles around a given position
         rects = []
         for tile in self.tiles_around(pos):
              
              if tile['type'] in PHYSICS_TILES: # Check if the tile type has physics properties 
                   rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size)) # Create a rectangle for the tile and add it to the rects list
         return rects


    def render(self,surf, offset=(0,0)): # Render the tilemap onto the provided surface with an optional offset
            for tile in self.offgrid_tiles:
                surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])) # Renders offgrid tiles at their pixel positions
           
            for loc in self.tilemap:
                tile = self.tilemap[loc]
                surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1])) # Renders each tile at its corresponding position on the surface)

     
           
    