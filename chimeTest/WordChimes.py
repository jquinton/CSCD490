import os, pygame
from pygame.locals import *

SCREENWIDTH = 1000
SCREENHEIGHT = 700

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
    path = os.path.join('Images/Letters/', name)
    return pygame.image.load(path).convert_alpha()
    
    
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
    letterTile = ImageObject(letterTileImage,  (len(bottomTiles)*40+10), SCREENHEIGHT - 40,   1,  letters[len(letters)-1])
    #draw the image
    screen.blit(letterTile.image, letterTile.pos)
    #add to array
    bottomTiles.append(letterTile)
    #update the display
    pygame.display.update()

#play_sound
def play_sound(sound_path):
    try:
        pygame.mixer.music.load(sound_path)
        print "loaded %s" % sound_path
    except:
        print "%s failed to load" % sound_path
        return
    pygame.mixer.music.play()



#first to run when program starts
def main():    
    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    
    # fill sound array with sound files
    sound_list=[]
    i = 0
    while i < 26 :
        temp_sound_file = os.getcwd()
        temp_sound_file += "/soundfiles/"
        temp_sound_file += chr(i + 65)
        temp_sound_file += ".mid"
        sound_list.append(temp_sound_file)
        i += 1
    
    # Initialize mixer
    # the mixer is used by pygame to load and play the sound files
    freq = 44100 
    bitsize = -16
    channels = 2 
    buffer = 1024 
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(1.0)
        
    #used so animation displays at a reasonable speed
    clock = pygame.time.Clock()

    background = load_image('mountainBG.png')

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
        while waiting == True and done == False:
            #check for input
            for event in pygame.event.get():
                #check to see if user wants to exit
                if event.type == pygame.QUIT: 
                    done = True
                    
                if event.type == KEYDOWN:
                    if len(letters) == 0:
                        #clear the whole screen
                        screen.blit(background, (0, 0))
                
                    if len(letters) < 29:
                    
                        if event.key == K_a:
                            letters +='a'
                            addTile(screen,  bottomTiles,  '0A.png',  letters)
                        elif event.key == K_b:
                            letters +='b'
                            addTile(screen,  bottomTiles,  '0B.png',  letters)
                        elif event.key == K_c:
                            letters +='c'
                            addTile(screen,  bottomTiles,  '0C.png',  letters)
                        elif event.key == K_d:
                            letters +='d'
                            addTile(screen,  bottomTiles,  '0D.png',  letters)
                        elif event.key == K_e:
                            letters +='e'
                            addTile(screen,  bottomTiles,  '0E.png',  letters)
                        elif event.key == K_f:
                            letters +='f'
                            addTile(screen,  bottomTiles,  '0F.png',  letters)
                        elif event.key == K_g:
                            letters +='g'
                            addTile(screen,  bottomTiles,  '0G.png',  letters)
                        elif event.key == K_h:
                            letters +='h'
                            addTile(screen,  bottomTiles,  '0H.png',  letters)
                        elif event.key == K_i:
                            letters +='i'
                            addTile(screen,  bottomTiles,  '0I.png',  letters)
                        elif event.key == K_j:
                            letters +='j'
                            addTile(screen,  bottomTiles,  '0J.png',  letters)
                        elif event.key == K_k:
                            letters +='k'
                            addTile(screen,  bottomTiles,  '0K.png',  letters)
                        elif event.key == K_l:
                            letters +='l'
                            addTile(screen,  bottomTiles,  '0L.png',  letters)
                        elif event.key == K_m:
                            letters +='m'
                            addTile(screen,  bottomTiles,  '0M.png',  letters)
                        elif event.key == K_n:
                            letters +='n'
                            addTile(screen,  bottomTiles,  '0N.png',  letters)
                        elif event.key == K_o:
                            letters +='o'
                            addTile(screen,  bottomTiles,  '0O.png',  letters)
                        elif event.key == K_p:
                            letters +='p'
                            addTile(screen,  bottomTiles,  '0P.png',  letters)
                        elif event.key == K_q:
                            letters +='q'
                            addTile(screen,  bottomTiles,  '0Q.png',  letters)
                        elif event.key == K_r:
                            letters +='r'
                            addTile(screen,  bottomTiles,  '0R.png',  letters)
                        elif event.key == K_s:
                            letters +='s'
                            addTile(screen,  bottomTiles,  '0S.png',  letters)
                        elif event.key == K_t:
                            letters +='t'
                            addTile(screen,  bottomTiles,  '0T.png',  letters)
                        elif event.key == K_u:
                            letters +='u'
                            addTile(screen,  bottomTiles,  '0U.png',  letters)
                        elif event.key == K_v:
                            letters +='v'
                            addTile(screen,  bottomTiles,  '0V.png',  letters)
                        elif event.key == K_w:
                            letters +='w'
                            addTile(screen,  bottomTiles,  '0W.png',  letters)
                        elif event.key == K_x:
                            letters +='x'
                            addTile(screen,  bottomTiles,  '0X.png',  letters)
                        elif event.key == K_y:
                            letters +='y'
                            addTile(screen,  bottomTiles,  '0Y.png',  letters)
                        elif event.key == K_z:
                            letters +='z'
                            addTile(screen,  bottomTiles,  '0Z.png',  letters)
                        elif event.key == K_SPACE:
                            letters +=' '
                            addTile(screen,  bottomTiles,  'transparent.png',  letters)
                        elif event.key == K_EXCLAIM:
                            letters +='!'
                            addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                        elif event.key == K_BACKSPACE:
                            if len(letters) > 0:
                                letters = letters[:-1]
                                bottomTiles.pop()
                                redrawTiles(screen,  background,  bottomTiles)
                    
                    #see if done entering text
                    if (event.key == K_RETURN):
                        waiting = False
        
        
        
       
        #create notes and set their position and speed to raise at
        notes = []
        for x in range(len(letters)):
            if ord(letters[x]) >= 97 and ord(letters[x]) <= 122:
                noteImage = load_image("0" + letters[x].upper() + ".png")
            elif ord(letters[x]) == 32:
                      noteImage = load_image("transparent.png")
      
            note = ImageObject(noteImage, x*40+10, SCREENHEIGHT - 20,  3,  letters[x])
            notes.append(note)
        
        height = 50
        note_number = 0
        #used to store the notes when the reach there final destination
        finals = []
        
        #this is the loop that move the notes up the screen
        for note in notes:
            
            #sets the destination and the delay for assending notes assend

            accentDelay = 10
            if ord(note.letter) >= 97 and ord(note.letter) <= 122:
                height = (SCREENHEIGHT-90) - ((ord(note.letter) - 97) * 15)
                accentDelay = 30 + ((ord(note.letter) - 97) * 5)
            elif ord(note.letter) == 32:
                height = (SCREENHEIGHT-90) - (ord(note.letter)  * 15)
                accentDelay = 30 + (ord(note.letter) * 5)
            
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
            #play the sound if not a space
            print ord(note.letter)
            if ord(note.letter) != 32:
                play_sound(sound_list[ord(note.letter) - 97])
            note_number += 1

    pygame.quit ()


if __name__ == '__main__': 
    main()
