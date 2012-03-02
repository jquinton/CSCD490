#! /usr/bin/env python

import pygame
from pygame.locals import *
import gtk
import os

SCREENWIDTH = 1200
SCREENHEIGHT = 700
FPS = 20
ANIM_FRAME_TIME = 30
ANIM_SPEED_INCREASE = .5
ANIM_SPEED_START = 1.6
colorMod = 0

#the note object that will assend the screen
class ImageObject():
    def __init__(self, image, Xcord,  Ycord, speed,  letter):
        self.letter = letter
        self.speed = speed
        self.image = image
        self.subpixel = 0
        self.pos = image.get_rect().move(Xcord, Ycord)
    def move(self):
        self.pos = self.pos.move(0, -self.speed)
        self.subpixel += (self.speed * 10) % 10
        if self.subpixel > 9:
            self.pos = self.pos.move(0, -1)
            self.subpixel = self.subpixel % 10

class WordChimes:
    
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.background = load_image('mountainBG.png')
        
    def run(self):
         global colorMod 
         
        # fill sound array with sound files
         sound_list = []
         i = 0
         while i < 26 :
            temp_sound_file = os.getcwd()
            temp_sound_file += "/soundfiles/"
            temp_sound_file += chr(i + 65)
           
            if(i+65 != 74 and i+65 != 75 and i+65 != 76):
                temp_sound_file += ".mid"
            else:
                temp_sound_file += ".wav"
            sound_list.append(temp_sound_file)
            i += 1
        
        # Initialize mixer
        # the mixer is used by pygame to load and play the sound files
         freq = 44100 
         bitsize = -16
         channels = 2 
         buffer = 2048
         pygame.mixer.init(freq, bitsize, channels, buffer)
         pygame.mixer.music.set_volume(0.7)
        
        #used so animation displays at a reasonable speed

        #draw the background = load_im
        
        #setup screen
         screen = pygame.display.get_surface()
         screen.blit(self.background, (0, 0))
        #update the display
         pygame.display.update()
         print screen.get_height()
        
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
            colorMod =0
            while waiting == True and done == False:
                #check for input
                
                while gtk.events_pending():
                    gtk.main_iteration()
                
                
                for event in pygame.event.get():
                    #check to see if user wants to exit
                    if event.type == pygame.QUIT: 
                        done = True
                        break
                    if event.type == KEYDOWN:
                        
                        
                        if len(letters) == 0:
                            #clear the whole screen
                            screen.blit(self.background, (0, 0))
                    
                        if len(letters) < 29:
                        
                            if event.key == K_a:
                                letters +='a'
                                addTile(screen,  bottomTiles,  '01.png',  letters)
                            elif event.key == K_b:
                                letters +='b'
                                addTile(screen,  bottomTiles,  '02.png',  letters)
                            elif event.key == K_c:
                                letters +='c'
                                addTile(screen,  bottomTiles,  '03.png',  letters)
                            elif event.key == K_d:
                                letters +='d'
                                addTile(screen,  bottomTiles,  '04.png',  letters)
                            elif event.key == K_e:
                                letters +='e'
                                addTile(screen,  bottomTiles,  '05.png',  letters)
                            elif event.key == K_f:
                                letters +='f'
                                addTile(screen,  bottomTiles,  '06.png',  letters)
                            elif event.key == K_g:
                                letters +='g'
                                addTile(screen,  bottomTiles,  '07.png',  letters)
                            elif event.key == K_h:
                                letters +='h'
                                addTile(screen,  bottomTiles,  '08.png',  letters)
                            elif event.key == K_i:
                                letters +='i'
                                addTile(screen,  bottomTiles,  '09.png',  letters)
                            elif event.key == K_j:
                                letters +='j'
                                addTile(screen,  bottomTiles,  '10.png',  letters)
                            elif event.key == K_k:
                                letters +='k'
                                addTile(screen,  bottomTiles,  '11.png',  letters)
                            elif event.key == K_l:
                                letters +='l'
                                addTile(screen,  bottomTiles,  '12.png',  letters)
                            elif event.key == K_m:
                                letters +='m'
                                addTile(screen,  bottomTiles,  '13.png',  letters)
                            elif event.key == K_n:
                                letters +='n'
                                addTile(screen,  bottomTiles,  '14.png',  letters)
                            elif event.key == K_o:
                                letters +='o'
                                addTile(screen,  bottomTiles,  '15.png',  letters)
                            elif event.key == K_p:
                                letters +='p'
                                addTile(screen,  bottomTiles,  '16.png',  letters)
                            elif event.key == K_q:
                                letters +='q'
                                addTile(screen,  bottomTiles,  '17.png',  letters)
                            elif event.key == K_r:
                                letters +='r'
                                addTile(screen,  bottomTiles,  '18.png',  letters)
                            elif event.key == K_s:
                                letters +='s'
                                addTile(screen,  bottomTiles,  '19.png',  letters)
                            elif event.key == K_t:
                                letters +='t'
                                addTile(screen,  bottomTiles,  '20.png',  letters)
                            elif event.key == K_u:
                                letters +='u'
                                addTile(screen,  bottomTiles,  '21.png',  letters)
                            elif event.key == K_v:
                                letters +='v'
                                addTile(screen,  bottomTiles,  '22.png',  letters)
                            elif event.key == K_w:
                                letters +='w'
                                addTile(screen,  bottomTiles,  '23.png',  letters)
                            elif event.key == K_x:
                                letters +='x'
                                addTile(screen,  bottomTiles,  '24.png',  letters)
                            elif event.key == K_y:
                                letters +='y'
                                addTile(screen,  bottomTiles,  '25.png',  letters)
                            elif event.key == K_z:
                                letters +='z'
                                addTile(screen,  bottomTiles,  '26.png',  letters)
#                            elif event.key == K_1:
#                                letters +='1'
#                                addTile(screen,  bottomTiles,  '1.png',  letters)
#                            elif event.key == K_2:
#                                letters +='2'
#                                addTile(screen,  bottomTiles,  '2.png',  letters)
#                            elif event.key == K_3:
#                                letters +='3'
#                                addTile(screen,  bottomTiles,  '3.png',  letters)   
#                            elif event.key == K_4:
#                                letters +='4'
#                                addTile(screen,  bottomTiles,  '4.png',  letters)
#                            elif event.key == K_5:
#                                letters +='5'
#                                addTile(screen,  bottomTiles,  '5.png',  letters)     
#                            elif event.key == K_6:
#                                letters +='6'
#                                addTile(screen,  bottomTiles,  '6.png',  letters)
#                            elif event.key == K_7:
#                                letters +='7'
#                                addTile(screen,  bottomTiles,  '7.png',  letters)     
#                            elif event.key == K_8:
#                                letters +='8'
#                                addTile(screen,  bottomTiles,  '8.png',  letters)
#                            elif event.key == K_9:
#                                letters +='9'
#                                addTile(screen,  bottomTiles,  '9.png',  letters) 
#                            elif event.key == K_0:
#                                letters +='0'
#                                addTile(screen,  bottomTiles,  '0.png',  letters)

#                            elif event.key == K_`:
#                                letters +='`'
#                                addTile(screen,  bottomTiles,  '`.png',  letters)
#                            elif event.key == K_=:
#                                letters +='='
#                                addTile(screen,  bottomTiles,  '=.png',  letters) 
#                            elif event.key == K_-:
#                                letters +='-'
#                                addTile(screen,  bottomTiles,  '-.png',  letters)
#                            elif event.key == K_,:
#                                letters +=','
#                                addTile(screen,  bottomTiles,  ',.png',  letters) 
#                            elif event.key == K_;:
#                                letters +=';'
#                                addTile(screen,  bottomTiles,  ';.png',  letters)
#                            elif event.key == K_[:
#                                letters +='['
#                                addTile(screen,  bottomTiles,  '[.png',  letters) 
#                            elif event.key == K_]:
#                                letters +=']'
#                                addTile(screen,  bottomTiles,  '].png',  letters)
#                            elif event.key == K_.:
#                                letters +='.'
#                                addTile(screen,  bottomTiles,  'period.png',  letters) 
#                            elif event.key == K_/:
#                                letters +='/'
#                                addTile(screen,  bottomTiles,  'slash.png',  letters)
#                            elif event.key == K_\:
#                                letters +='\\'
#                                addTile(screen,  bottomTiles,  '\.png',  letters) 
#                            elif event.key == K_'\'':
#                                letters +='\''
#                                addTile(screen,  bottomTiles,  '\'.png',  letters)

                                
                            elif event.key == K_SPACE:
                                letters +=' '
                                addTile(screen,  bottomTiles,  'transparent.png',  letters)
                            elif event.key == K_EXCLAIM:
                                letters +='!'
                                addTile(screen,  bottomTiles,  'tile.bmp',  letters)
                        
                        if event.key == K_BACKSPACE:
                            
                            if len(letters) > 0:
                                colorMod = colorMod -1
                                letters = letters[:-1]
                                bottomTiles.pop()
                                redrawTiles(screen,  self.background,  bottomTiles)
                        
                        #see if done entering text
                        if (event.key == K_RETURN):
                            colorMod = 0
                            waiting = False
                        colorMod = colorMod + 1
            
            
            #create notes and set their position and speed to raise at
            notes = []
            colorMod = 0
            for x in range(len(letters)):
                
                if ord(letters[x]) >= 97 and ord(letters[x]) <= 122:
                    noteImage = load_letter("Note.png")
                elif ord(letters[x]) == 32:
                          noteImage = load_letter("transparent.png")
                
                note = ImageObject(noteImage, x*40+10, screen.get_height() - 50,  3,  letters[x])
                notes.append(note)
                colorMod = colorMod + 1
            note_number = 0
            #used to store the notes when the reach there final destination
            finals = []
            
            #this is the loop that move the notes up the screen
            for note in notes:
                note.speed = ANIM_SPEED_START + (ord(note.letter)-97) * ANIM_SPEED_INCREASE
                #this loops tell the note gets to its destination
                for k in range(ANIM_FRAME_TIME):
                    while gtk.events_pending():
                        gtk.main_iteration()                    
                    
                    #check to see if user wants to exit
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            done = True
                            break
                    #move the note up
                    note.move()
                    #clear the whole screen
                    screen.blit(self.background, (0, 0))
                    
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
                    self.clock.tick(FPS)
                
                #add to final notes so they can be redrawn
                finals.append(note)
                #play the sound if not a space
                print ord(note.letter)
                if ord(note.letter) >= 97 and ord(note.letter) <= 122:
                    play_sound(sound_list[ord(note.letter) - 97])
                
                note_number += 1


def load_image(name):
    path = os.path.join(os.path.dirname(__file__), 'Images', name)
    image = pygame.image.load(path)
    return image
    
    
    
def get_path():
    colorFile = ""
    colorModTemp = colorMod  % 8
    
    if colorModTemp == 0:
        colorFile = "LettersBlue"
    elif colorModTemp == 1:
        colorFile = "LettersGreen"
    elif colorModTemp == 2:
        colorFile = "LettersOrange"
    elif colorModTemp == 3:
        colorFile = "LettersGrey"
    elif colorModTemp == 4:
        colorFile = "LettersPurple"
    elif colorModTemp == 5:
        colorFile = "LettersRed"
    elif colorModTemp == 6:
        colorFile = "LettersTeal"
    elif colorModTemp == 7:
        colorFile = "LettersYellow"
    return colorFile
    
    
#function to load a letter
def load_letter(name):
    colorFile = get_path()
    colorMod = 1
    path = os.path.join(os.path.dirname(__file__), 'LettersColor', colorFile, name)
    return pygame.image.load(path) 
        
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
    letterTileImage = load_letter(image)
    letterTile = ImageObject(letterTileImage,  (len(bottomTiles)*40+10), screen.get_height() - 50,   1,  letters[len(letters)-1])
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
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = WordChimes()
    game.run()
    
if __name__ == '__main__': 
    main()
