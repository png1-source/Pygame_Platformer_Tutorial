#NOTE: Whenver code tutorial says display, replace this word with screen as per pygame terminology.

import pygame

class PhysicsEntity: # A class to represent a physical entity in the game world
    def __init__(self, game, e_type, pos, size): # Initialize the entity with its type, position, and size, velocity
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False} # Dictionary to track collision states in each direction 

    def rect(self): # Creates a function for getting the entity's rectangle for collision detection 
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]) # Return the entity's rectangle for collision detection

    def update(self, tilemap, movement=(0, 0)): # Update the entity's position based on movement input
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False} # Dictionary to track collision states in each direction 

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1]) # Combine input movement with current velocity

        self.pos[0] += frame_movement[0] # Apply horizontal movement to x position 
        entity_rect = self.rect() # Get the entity's rectangle for collision detection
        for rect in tilemap.physics_rects_around(self.pos): # Check for collisions with nearby physics rectangles in the tilemap
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left # Here, we are essentially identifying the character's movement as going right to combine with the collision detection, and setting the character's right side to be equal to the left side of the rectangle it collided with.
                    self.collisions['right'] = True # Marks the right collision as True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right # Here, we are essentially identifying the character's movement as going left to combine with the collision detection, and setting the character's left side to be equal to the right side of the rectangle it collided with. (Vice versa) 
                    self.collisions['left'] = True # Marks the left collision as True
                self.pos[0] = entity_rect.x # Update the entity's x position after collision resolution
                

        self.pos[1] += frame_movement[1] # Apply vertical movement to y position 
        entity_rect = self.rect() # Get the entity's rectangle for collision detection
        for rect in tilemap.physics_rects_around(self.pos): # Check for collisions with nearby physics rectangles in the tilemap
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top # Here, we are essentially identifying the character's movement as going right to combine with the collision detection, and setting the character's right side to be equal to the left side of the rectangle it collided with.
                    self.collisions['down'] = True # Marks the down collision as True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom # Here, we are essentially identifying the character's movement as going left to combine with the collision detection, and setting the character's left side to be equal to the right side of the rectangle it collided with. (Vice versa) 
                    self.collisions['up'] = True # Marks the up collision as True
                self.pos[1] = entity_rect.y # Update the entity's x position after collision resolution


        self.velocity[1] = min(5, self.velocity[1] + 0.1) # Apply gravity to vertical velocity, capping terminal velcoity at strength 5 

        if self.collisions['down'] or self.collisions['up']: # If there is a collision either above or below the entity (character) 
            self.velocity[1] = 0 # Reset vertical velocity to 0

    def render(self, surf, offset = (0,0)): # Render the entity onto the given surface with an optional offset
        surf.blit(self.game.assets['player'], (self.pos[0] - offset[0], self.pos[1] - offset[1])) # Blit the entiity sprite (Feteched via game.assets) at current posiiton. 
        