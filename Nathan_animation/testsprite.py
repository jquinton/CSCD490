#/usr/bin/env python

import os, sys,  pygame
from pygame.locals import *

def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
    
class Note(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('face.png')
        self.rect.topleft = 380, 250
        self.speed = 1.0
        self.move_x = 0
        self.move_y = 0
        
    def update(self):
        self.rect = self.rect.move(self.move_x, self.move_y)
            
    def moveRight(self):
        self.move_x = self.speed
        self.move_y = 0
    
    def moveLeft(self):
        self.move_x = self.speed * -1
        self.move_y = 0
        
    def moveUp(self):
        self.move_x = 0
        self.move_y = self.speed * -1
        
    def moveDown(self):
        self.move_x = 0
        self.move_y = self.speed
        
    def stop(self):
        self.move_x = 0
        self.move_y = 0

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((760, 520))
    pygame.display.set_caption('Test Sprite')

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((235, 235, 235))


#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    clock = pygame.time.Clock()
    note = Note()
    allsprites = pygame.sprite.RenderPlain((note))

#Main Loop
    while 1:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                note.moveRight()
            elif event.type == KEYDOWN and event.key == K_LEFT:
                note.moveLeft()
            elif event.type == KEYDOWN and event.key == K_UP:
                note.moveUp()
            elif event.type == KEYDOWN and event.key == K_DOWN:
                note.moveDown()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                note.stop()
        allsprites.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
