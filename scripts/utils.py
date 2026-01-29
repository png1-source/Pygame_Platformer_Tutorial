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


        