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

        self.action = ' ' # This intilizes the current action of the entity as an empty string. The action variable can be used to determine which animation to play for the entity based on its current state (e.g., idle, running, jumping). By setting it to an empty string initially, we can later update it to reflect the entity's actions as the game progresses.
        self.anim_offset = (-3, -3)
        self.flip = False 
        self.set_action('idle') # Set the initial action of the entity to 'idle' using the set_action method. This will determine which animation to play for the entity when it is first created. By default, the entity will be in an idle state until it receives input or changes its state based on game logic.


    def rect(self): # Creates a function for getting the entity's rectangle for collision detection 
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]) # Return the entity's rectangle for collision detection
    
    def set_action(self, action): # Set the current action of the entity and update the animation accordingly
        if action != self.action: # Check if the new action is different from the current action
            self.action = action # Update the current action to the new action
            self.animation = self.assests[self.e_type + '/' + self.action].copy() # This line of code retrieves the appropriate animation for the entity based on its type and current action.


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

        if movement[0] > 0: # If there is horizontal movement to the right       
            self.flip = False # Set the flip flag to False to face right
        if movement[0] < 0: # If there is horizontal movement to the left
            self.flip = True # Set the flip flag to True to face left


        self.velocity[1] = min(5, self.velocity[1] + 0.1) # Apply gravity to vertical velocity, capping terminal velcoity at strength 5 

        if self.collisions['down'] or self.collisions['up']: # If there is a collision either above or below the entity (character) 
            self.velocity[1] = 0 # Reset vertical velocity to 0

        self.animation.update() # Update the entity's animation frame based on its current action and animation state

    def render(self, surf, offset = (0,0)): # Render the entity onto the given surface with an optional offset
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] + self.anim_offset[1] - offset[1])) # Blit the entity's current animation frame onto the surface at the entity's position adjusted by the animation offset and rendering offset. The pygame.transform.flip function is used to flip the image horizontally if the flip flag is set to True, allowing for left and right facing animations. The animation.img() method retrieves the current frame of the animation based on the entity's action and animation state.

        