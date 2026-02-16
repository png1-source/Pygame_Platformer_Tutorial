import random

class Clouds: # clouds are just a list of cloud objects that move across the screen
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    def update(self): # update the cloud's position based on its speed and depth. The depth is used to create a parallax effect, where clouds that are further away move slower than clouds that are closer.
        self.pos[0] += self.speed

    def render(self, surf, offset=(0,0)): # render the cloud onto the given surface (surf) at its current position, adjusted for the camera offset and depth. The offset is the camera position in the game world, and the depth is used to create a parallax effect.
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)


               
