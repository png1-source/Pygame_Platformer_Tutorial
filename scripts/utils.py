# NOTE: Whenver code tutorial says display, replace this word with screen as per pygame terminology.

import os # Operating system interfaces 

import pygame

BASE_IMG_PATH = 'data/images/' # Base path for all images

def load_image(path): # This function can be used multiple times to render an image. In coding, rendering means displaying an image on the screen. 
    img = pygame.image.load(BASE_IMG_PATH + path).convert() # Load image and convert for optimal blitting. The convert() method changes the pixel format of the image to match the display.
    img.set_colorkey((0, 0, 0)) # Set black (0,0,0) as the backround colour for our game as mentioned in the game.py file. 
    return img 

def load_images(path): # The function below retrives the images from a folder using 'path' and '/' to get inside the folder. 
    images =[]
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)): #os.listdir() function returns a list containing the names of the entries in the directory given by path. It is the most efficient way to retrive all of our images. 
        images.append(load_image(path + '/' + img_name)) 
    return images

class Animation: # Since there is no premade library for animations in pygame, we have to create our own animation class. This class will handle the animation of our game objects by cycling through a list of images.
    def __init__(self, images, img_dur = 5, loop = True): # Initialize the animation with a list of images, image duration, and a look flag
       self.images = images
       self.loop = loop
       self.img_duration = img_dur
       self.done = False
       self.frame = 0
       
    def copy(self): # The copy function creates a copy of the animation object created above. 
        return Animation(self.images, self.img_duration, self.loop) # Returns a new instance of the Animation class with the same images, image duration, and loop flag as the original animation object.
    
    def update(self): # The update function is responsible for updating the animation frame. It increments the frame counter and checks if the animation has reached the end of the image list. If it has, it either loops back to the beginning or marks the animation as done, depending on the loop flag.
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1) # We do -1 because the frame index starts at 0, so the last frame is at index len(self.images) - 1. This ensures that the animation stops at the last frame and does not go out of bounds.
            if self.frame >= self.img_duration * len(self.images) - 1: # This line checks if the animation has reached the last frame. If it has, it sets the done flag to True, indicating that the animation is complete. 
               self.done = True # The done flag can be used in the game logic to determine when to remove the animation or trigger other events based on the completion of the animation.
    
    def img(self):
        return self.images[int(self.frame / self.img_duration)]


