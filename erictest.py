import os, pygame
from pygame.locals import *

#the note object that will assend the screen
class ImageObject:
    def __init__(self, image, Xcord,  Ycord, speed,  letter):
        self.letter = letter
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(Xcord, Ycord)
    def move(self):
            self.pos = self.pos.move(0, -self.speed)


#function to load an image
def load_image(name):
    path = os.path.join('res', name)
    return pygame.image.load(path).convert()
    
    
def redrawTiles(screen,  background,  bottomTiles):
    #clear the whole screen
    screen.blit(background, (0, 0))
    #redraw the bottom letters that have reached there destination
    for letterTile in bottomTiles:
        screen.blit(letterTile.image, letterTile.pos)
    #update the display
    pygame.display.update()
    
    
def addTile(screen,  bottomTiles,  image,  letters):
    #load the image
    letterTileImage = load_image(image)
    letterTile = ImageObject(letterTileImage,  (len(bottomTiles)*50+10), 550,   1,  letters[len(letters)-1])
    #draw the image
    screen.blit(letterTile.image, letterTile.pos)
    #add to array
    bottomTiles.append(letterTile)
    #update the display
    pygame.display.update()


#first to run when program starts
def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    
    #used so animation displays at a reasonable speed
    clock = pygame.time.Clock()

    player = load_image('chimp.bmp')
    background = load_image('fist.bmp')

    #draw the background
    screen.blit(background, (0, 0))
    #update the display
    pygame.display.update()

    
    #start the game loop
    done = False
    while done == False:
        #check to see if user wants to exit
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
        
        
        #listen for user input
        letters = ""
        bottomTiles = []
        waiting = True
        while waiting == True and done ==False:
            #check for input
            for event in pygame.event.get():
                #check to see if user wants to exit
                if event.type == pygame.QUIT: 
                    done = True
                    
                if event.type == KEYDOWN:
                    if event.key == K_0:
                        letters +='0'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_1:
                        letters +='1'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_2:
                        letters +='2'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_3:
                        letters +='3'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_4:
                        letters +='4'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_5:
                        letters +='5'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_6:
                        letters +='6'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_7:
                        letters +='7'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_8:
                        letters +='8'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_9:
                        letters +='9'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_a:
                        letters +='a'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_b:
                        letters +='b'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_c:
                        letters +='c'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_d:
                        letters +='d'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_e:
                        letters +='e'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_f:
                        letters +='f'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_g:
                        letters +='g'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_h:
                        letters +='h'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_i:
                        letters +='i'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_j:
                        letters +='j'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_k:
                        letters +='k'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_l:
                        letters +='l'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_m:
                        letters +='m'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_n:
                        letters +='n'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_o:
                        letters +='o'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_p:
                        letters +='p'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_q:
                        letters +='q'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_r:
                        letters +='r'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_s:
                        letters +='s'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_t:
                        letters +='t'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_u:
                        letters +='u'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_v:
                        letters +='v'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_w:
                        letters +='w'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_x:
                        letters +='x'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_y:
                        letters +='y'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_z:
                        letters +='z'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_SPACE:
                        letters +=' '
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_EXCLAIM:
                        letters +='!'
                        addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                    elif event.key == K_BACKSPACE:
                        if len(letters) > 0:
                            letters = letters[:-1]
                            bottomTiles.pop()
                            redrawTiles(screen,  background,  bottomTiles)
                    
                    print letters
                    
                    #see if done entering text
                    if (event.key == K_RETURN):
                        waiting = False
        
        
        #create notes and set their position and speed to raise at
        notes = []
        for x in range(len(letters)):
            note = ImageObject(player, x*50+10, 500,  10,  letters[x])
            notes.append(note)
        
        height = 50
        
        #used to store the notes when the reach there final destination
        finals = []
        
        #this is the loop that move the notes up the screen
        for note in notes:
            
            #sets the destination and the delay for assending notes assend
            accentDelay = 10
            if ord(note.letter) >= 97 and ord(note.letter) <= 122:
                height = 500 - ((ord(note.letter) - 97) * 20)
                accentDelay = (((ord(note.letter) - 97) * 20) + 20) / 10
            if ord(note.letter) >= 48 and ord(note.letter) <= 57:
                height = 500 - ((ord(note.letter) - 47 + (122 - 97)) * 20)
                accentDelay = (((ord(note.letter) - 47 + (122 - 97)) * 20) + 20) / 10
                
            #this loops tell the note gets to its destination
            while note.pos.top >= height and done == False:
                #check to see if user wants to exit
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        done = True 
                
                #move the note up
                note.move()
                #clear the whole screen
                screen.blit(background, (0, 0))
                
                 #draw the moving note
                screen.blit(note.image, note.pos)
                #redraw the bottom letters that have reached there destination
                for letterTile in bottomTiles:
                    screen.blit(letterTile.image, letterTile.pos) 
                #redraw the notes that have reached there destination
                for finalNote in finals:
                    screen.blit(finalNote.image, finalNote.pos)
                #update the display
                pygame.display.update()
 
                #delay for a period of time
                clock.tick(accentDelay)
            
            #add to final notes so they can be redrawn
            finals.append(note)

    pygame.quit ()


if __name__ == '__main__': 
    main()
