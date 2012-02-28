#!/usr/bin/env python 
import pygame
from pygame.locals import *
import Image

#variables/data structures

imagePath  = "../Images/"
images = []

def loadImages():
    
    for i in range (0, 69):
        fileName = imagePath + str(i) + '.png' 
        print fileName
        tempImage = pygame.image.load(fileName)
        images.append(tempImage)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Key Listener Testing')
pygame.mouse.set_visible(0)

b = pygame.sprite.Sprite() # create sprite
#b.image = images[4]# load ball image

pygame.display.update()
loadImages()
background = pygame.image.load("../Images/mountainBG.png")

#draw the background
screen.blit(background, (0, 0))
#update the display
pygame.display.update()

    
done = False  
shiftBoolean = False
word = []
while not done:
   for event in pygame.event.get():
      if (event.type == KEYDOWN):
         i = event
         if(i.key == 8):
            word.pop()
         elif(i.key > 27):
            word.append(i.key)
         print images
        
         if (event.key == 27):
            done = True


