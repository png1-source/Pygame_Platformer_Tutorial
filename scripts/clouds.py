import random

class Cloud: # individual cloud object that moves across the screen
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    def update(self): # update the cloud's position based on its speed and depth. The depth is used to create a parallax effect, where clouds that are further away move slower than clouds that are closer.
        self.pos[0] += self.speed

    def render(self, surf, offset=(0,0)): # render the cloud onto the given surface (surf) at its current position, adjusted for the camera offset and depth. The offset is the camera position in the game world, and the depth is used to create a parallax effect.
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth) # calculate the render position based on the cloud's position, the camera offset, and the cloud's depth
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), (render_pos[1] % (surf.get_height() + self.img.get_height())) - self.img.get_height())) # render the cloud image onto the surface at the calculated render position. 

class Clouds:
    def __init__(self, cloud_images, count = 16):
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud((random.random() * 99999, random.random() * 99999), random.choice(cloud_images), random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2)) # create a new cloud with a random position, a random image from the cloud_images list, a random speed between 0.05 and 0.1, and a random depth between 0.2 and 0.8

        self.clouds.sort(key = lambda x: x.depth) # sort the clouds by their depth so that they are rendered in the correct order (clouds with a smaller depth are rendered behind clouds with a larger depth)           

    def update(self):
        for cloud in self.clouds:
            cloud.update() # update each cloud's position

    def render(self, surf, offset=(0,0)):
        for cloud in self.clouds:
            cloud.render(surf, offset = offset) # render each cloud onto the given surface with the current camera offset
        


               
