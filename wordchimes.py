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
        self.frame = 0;
    def move(self):
        self.pos = self.pos.move(0, -self.speed)
        self.subpixel += (self.speed * 10) % 10
        if self.subpixel > 9:
            self.pos = self.pos.move(0, -1)
            self.subpixel = self.subpixel % 10
        self.frame += 1
    def isDone(self):
        return self.frame >= ANIM_FRAME_TIME

class WordChimes:
    letterMap = {K_a:('a', '01.png'), \
              K_b:('b', '02.png'), \
              K_c:('c', '03.png'), \
              K_d:('d', '04.png'), \
              K_e:('e', '05.png'), \
              K_f:('f', '06.png'), \
              K_g:('g', '07.png'), \
              K_h:('h', '08.png'), \
              K_i:('i', '09.png'), \
              K_j:('j', '10.png'), \
              K_k:('k', '11.png'), \
              K_l:('l', '12.png'), \
              K_m:('m', '13.png'), \
              K_n:('n', '14.png'), \
              K_o:('o', '15.png'), \
              K_p:('p', '16.png'), \
              K_q:('q', '17.png'), \
              K_r:('r', '18.png'), \
              K_s:('s', '19.png'), \
              K_t:('t', '20.png'), \
              K_u:('u', '21.png'), \
              K_v:('v', '22.png'), \
              K_w:('w', '23.png'), \
              K_x:('x', '24.png'), \
              K_y:('y', '25.png'), \
              K_z:('z', '26.png'), \
              K_SPACE:(' ', 'transparent.png'), \
              K_EXCLAIM:('!', 'tile.bmp')}
    letterMapAscii = 0
    letterMapImage = 1
    
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.background = self.load_image('mountainBG.png')
        self.letters = ""
        self.colorMod = 0
        self.bottomTiles = []
        self.screen = 0
        self.quit = False
        self.initMixer()
        self.initSounds()
        
        
        self.animating = False
        self.afterAnimating = False
        self.notes = None
        self.notesDone = []
        
        
            
    def initMixer(self):
        # Initialize mixer
        # the mixer is used by pygame to load and play the sound files
         freq = 44100 
         bitsize = -16
         channels = 2 
         buffer = 2048
         pygame.mixer.init(freq, bitsize, channels, buffer)
         pygame.mixer.music.set_volume(0.7)
    
    def initSounds(self):
        # fill sound array with sound files
        self.sound_list = []
        for i in range(0,  26):
            temp_sound_file = os.getcwd()
            temp_sound_file += "/soundfiles/"
            temp_sound_file += chr(i + 65)
            temp_sound_file += ".wav"
            self.sound_list.append(temp_sound_file)
            
    def run(self):
        #get screen
        self.screen = pygame.display.get_surface()
        self.initTyping()
        #update the display
        pygame.display.update()
        #print screen.get_height()
        
        #start the game loop
        while not self.quit:
            #Yield to GTK?
            while gtk.events_pending():
                gtk.main_iteration()
                
            if self.animating:
                note = self.notes[self.currentNote]
                note.move()
                #clear the whole screen
                self.screen.blit(self.background, (0, 0))
                #draw the moving note
                self.screen.blit(note.image, note.pos)
                
                if self.currentNote >= len(self.notes):
                    self.stopAnimating()
                #redraw the bottom letters that have reached their destination
                for letterTile in self.bottomTiles:
                    self.screen.blit(letterTile.image, letterTile.pos) 
                #redraw the notes that have reached there destination
                for finalNote in self.notesDone:
                    self.screen.blit(finalNote.image, finalNote.pos)
                #update the display
                pygame.display.update()
                #delay for a period of time
                self.clock.tick(FPS)
                if note.frame == ANIM_FRAME_TIME - FPS / 3:
                    if ord(note.letter) >= 97 and ord(note.letter) <= 122:
                        self.play_sound(self.sound_list[ord(note.letter) - 97])
                if note.isDone():
                    self.notesDone.append(note)
                    self.currentNote += 1
                    if self.currentNote >= len(self.notes):
                        self.stopAnimating()
                        continue
            else:
                pygame.display.update()
            #Event processing loop
            #events = []
            #Use wait() when we can, so we are not wasting
            #the laptop's battery.
            #if not self.animating:
            #   events = [ pygame.event.wait() ]
            #events +=  pygame.event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    break
                elif event.type == KEYDOWN:
                    self.doKeyDown(event)
            #End of event processing loop
            
        #End of main loop
        return
        while not self.quit:
            #check to see if user wants to exit
            for event in [ pygame.event.wait() ] + pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.quit = True 
            
            
            #listen for user input
            self.letters = ""
            self.colorMod = 0
            self.bottomTiles = []
            self.waiting = True
            while self.waiting and not self.quit:
                
                while gtk.events_pending():
                    gtk.main_iteration()
                
                print "@Checking events"
                for event in [ pygame.event.wait() ] + pygame.event.get(): 
                    #check to see if user wants to exit
                    if event.type == pygame.QUIT:
                        self.quit = True
                    elif event.type == KEYDOWN:
                        self.doKeyDown(event)
                print "@Finished looking at events"
            #create notes and set their position and speed to raise at
            
            
            note_number = 0
            #used to store the notes when the reach there final destination
            
            #this is the loop that move the notes up the screen
            for note in self.notes:
                if (self.quit):
                    break
                note.speed = ANIM_SPEED_START + (ord(note.letter)-97) * ANIM_SPEED_INCREASE
                #this loops tell the note gets to its destination
                for k in range(ANIM_FRAME_TIME):
                    if (self.quit):
                        break
                    while gtk.events_pending():
                        gtk.main_iteration()                    
                    
                    #check to see if user wants to exit
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            self.quit = True
                            break
                    #move the note up
                    note.move()
                    #clear the whole screen
                    self.screen.blit(self.background, (0, 0))
                    
                     #draw the moving note
                    self.screen.blit(note.image, note.pos)
                    #redraw the bottom letters that have reached there destination
                    for letterTile in self.bottomTiles:
                        self.screen.blit(letterTile.image, letterTile.pos) 
                    #redraw the notes that have reached there destination
                    for finalNote in notesDone:
                        self.screen.blit(finalNote.image, finalNote.pos)
                    #update the display
                    pygame.display.update()
     
                    #delay for a period of time
                    self.clock.tick(FPS)
                
                #add to final notes so they can be redrawn
                notesDone.append(note)
                
                #play the sound if not a space
                print ord(note.letter)
                if ord(note.letter) >= 97 and ord(note.letter) <= 122:
                    self.play_sound(self.sound_list[ord(note.letter) - 97])
                
                note_number += 1
                
    #Processes all KEYDOWN events
    def doKeyDown(self,  event):
        #Exit if escape is ever pressed
        if event.key == K_ESCAPE:
            self.quit = True
            return
        
        #Don't worry about any other keypresses while animating
        if self.animating == True:
            return
        
        #If a button has been pressed after animating is finished, then start fresh
        if self.afterAnimating:
            self.initTyping()
            self.afterAnimating = False
        #if len(self.letters) == 0:
            #clear the whole screen
        #    self.screen.blit(self.background, (0, 0))
            #update the display
        #    pygame.display.update()
        if len(self.letters) < 29:
            if event.key in self.letterMap:
                self.letters += self.letterMap[event.key][self.letterMapAscii]
                self.addTile(self.screen,  self.bottomTiles,  self.letterMap[event.key][self.letterMapImage],  self.letters)
        if event.key == K_BACKSPACE:
            if len(self.letters) > 0:
                self.colorMod -= 1
                self.letters = self.letters[:-1]
                self.bottomTiles.pop()
                self.redrawTiles(self.screen,  self.background, self.bottomTiles)
        elif (event.key == K_RETURN):
            self.initAnimating()
                
    def initTyping(self):
        self.colorMod = 0;
        #clear the whole screen
        self.screen.blit(self.background, (0, 0))
        #update the display
        pygame.display.update()
        
    def initAnimating(self):
        self.animating = True
        self.notes = []
        self.notesDone = []
        self.colorMod = 0
        self.currentNote = 0;
        for x in range(len(self.letters)):
            if ord(self.letters[x]) >= 97 and ord(self.letters[x]) <= 122:
                noteImage = self.load_letter("Note.png")
            elif ord(self.letters[x]) == 32:
                noteImage = self.load_letter("transparent.png")
            note = ImageObject(noteImage, x*40+10, self.screen.get_height() - 50,  3,  self.letters[x])
            note.speed = ANIM_SPEED_START + (ord(note.letter)-97) * ANIM_SPEED_INCREASE
            self.notes.append(note)
            self.colorMod += 1
    
    def stopAnimating(self):
        self.animating = False
        self.afterAnimating = True
        self.letters = ""
        self.notes = None
        self.notesDone = None
        self.bottomTiles = []
    #play_sound
    def play_sound(self,  sound_path):
        try:
            pygame.mixer.music.load(sound_path)
            print "loaded %s" % sound_path
        except:
            print "%s failed to load" % sound_path
            return
        pygame.mixer.music.play()
    

    def load_image(self,  name):
        path = os.path.join(os.path.dirname(__file__), 'Images', name)
        image = pygame.image.load(path)
        return image
    
    
    
    def get_path(self):
        colorFile = ""
        colorModTemp = self.colorMod  % 8
        
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
    def load_letter(self,  name):
        colorFile = self.get_path()
        #self.colorMod = 1
        path = os.path.join(os.path.dirname(__file__), 'LettersColor', colorFile, name)
        return pygame.image.load(path) 
        
    def redrawTiles(self,  screen,  background,  bottomTiles):
        #clear the whole screen
        screen.blit(background, (0, 0))
        #redraw the bottom letters that have reached there destination
        for letterTile in bottomTiles:
            screen.blit(letterTile.image, letterTile.pos)
        #update the display
        pygame.display.update()
        
        
    def addTile(self,  screen,  bottomTiles,  image,  letters):
        #load the image
        letterTileImage = self.load_letter(image)
        letterTile = ImageObject(letterTileImage,  (len(bottomTiles)*40+10), screen.get_height() - 50,   1,  letters[len(letters)-1])
        #draw the image
        screen.blit(letterTile.image, letterTile.pos)
        #add to array
        bottomTiles.append(letterTile)
        #update the display
        pygame.display.update()
        self.colorMod += 1
        
#first to run when program starts
def main():    
    pygame.init()
    pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
    game = WordChimes()
    game.run()
    
if __name__ == '__main__': 
    main()
#                            elif event.key == K_1:
#                                letters +='1'
#                                self.addTile(screen,  bottomTiles,  '1.png',  letters)
#                            elif event.key == K_2:
#                                letters +='2'
#                                self.addTile(screen,  bottomTiles,  '2.png',  letters)
#                            elif event.key == K_3:
#                                letters +='3'
#                                self.addTile(screen,  bottomTiles,  '3.png',  letters)   
#                            elif event.key == K_4:
#                                letters +='4'
#                                self.addTile(screen,  bottomTiles,  '4.png',  letters)
#                            elif event.key == K_5:
#                                letters +='5'
#                                self.addTile(screen,  bottomTiles,  '5.png',  letters)     
#                            elif event.key == K_6:
#                                letters +='6'
#                                self.addTile(screen,  bottomTiles,  '6.png',  letters)
#                            elif event.key == K_7:
#                                letters +='7'
#                                self.addTile(screen,  bottomTiles,  '7.png',  letters)     
#                            elif event.key == K_8:
#                                letters +='8'
#                                self.addTile(screen,  bottomTiles,  '8.png',  letters)
#                            elif event.key == K_9:
#                                letters +='9'
#                                self.addTile(screen,  bottomTiles,  '9.png',  letters) 
#                            elif event.key == K_0:
#                                letters +='0'
#                                self.addTile(screen,  bottomTiles,  '0.png',  letters)

#                            elif event.key == K_`:
#                                letters +='`'
#                                self.addTile(screen,  bottomTiles,  '`.png',  letters)
#                            elif event.key == K_=:
#                                letters +='='
#                                self.addTile(screen,  bottomTiles,  '=.png',  letters) 
#                            elif event.key == K_-:
#                                letters +='-'
#                                self.addTile(screen,  bottomTiles,  '-.png',  letters)
#                            elif event.key == K_,:
#                                letters +=','
#                                self.addTile(screen,  bottomTiles,  ',.png',  letters) 
#                            elif event.key == K_;:
#                                letters +=';'
#                                self.addTile(screen,  bottomTiles,  ';.png',  letters)
#                            elif event.key == K_[:
#                                letters +='['
#                                self.addTile(screen,  bottomTiles,  '[.png',  letters) 
#                            elif event.key == K_]:
#                                letters +=']'
#                                self.addTile(screen,  bottomTiles,  '].png',  letters)
#                            elif event.key == K_.:
#                                letters +='.'
#                                self.addTile(screen,  bottomTiles,  'period.png',  letters) 
#                            elif event.key == K_/:
#                                letters +='/'
#                                self.addTile(screen,  bottomTiles,  'slash.png',  letters)
#                            elif event.key == K_\:
#                                letters +='\\'
#                                self.addTile(screen,  bottomTiles,  '\.png',  letters) 
#                            elif event.key == K_'\'':
#                                letters +='\''
#                                self.addTile(screen,  bottomTiles,  '\'.png',  letters)
