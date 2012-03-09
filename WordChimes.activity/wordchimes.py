#! /usr/bin/env python

import pygame
from pygame.locals import *
import gtk
import os

MIXER_FREQ = 22050
MIXER_BITSIZE = -16
MIXER_CHANNELS = 1 
MIXER_BUFFER = 4096
MIXER_VOLUME = 0.4

SCREENWIDTH = 1200
SCREENHEIGHT = 700
FPS = 20
ANIM_FRAME_TIME = 20
ANIM_SPEED_INCREASE = .8
ANIM_SPEED_START = 1.6
colorMod = 0

null = None

#the note object that will assend the screen
class ImageObject():
    def __init__(self, image, Xcord,  Ycord, speed, keyData):
        self.speed = speed
        self.image = image
        self.keyData = keyData
        self.pos = image.get_rect().move(Xcord, Ycord)
        self.frame = 0
        self.subpixel = 0
        
    def move(self):
        self.pos = self.pos.move(0, -self.speed)
        self.subpixel += (self.speed * 10) % 10
        if self.subpixel > 9:
            self.pos = self.pos.move(0, -1)
            self.subpixel = self.subpixel % 10
        self.frame += 1
        
    def isDone(self):
        return self.frame >= ANIM_FRAME_TIME
        
    def play(this):
        this.keyData.playSound()
class KeyData:
    def __init__(this,  ascii,  imageFile,  soundFile):
        this.ascii = ascii
        this.imageFile = imageFile
        this.soundFile = soundFile
        this.sound = null
    def loadSound(this):
        try:
            file = os.path.join(os.getcwd(), 'soundfiles', this.soundFile)
            print file
            this.sound = pygame.mixer.Sound(file)
        except:
            pass
    def playSound(this):
        if (this.sound != null):
            this.sound.play()
            
        
        
class WordChimes:
    letterMap = {"a":KeyData('a','01.png', 'a.wav'), \
              "b":KeyData('b','02.png', 'b.wav'), \
              "c":KeyData('c','03.png', 'c.wav'), \
              "d":KeyData('d','04.png', 'd.wav'), \
              "e":KeyData('e','05.png', 'e.wav'), \
              "f":KeyData('f','06.png', 'f.wav'), \
              "g":KeyData('g','07.png', 'g.wav'), \
              "h":KeyData('h','08.png', 'h.wav'), \
              "i":KeyData('i','09.png', 'i.wav'), \
              "j":KeyData('j','10.png', 'j.wav'), \
              "k":KeyData('k','11.png', 'k.wav'), \
              "l":KeyData('l','12.png', 'l.wav'), \
              "m":KeyData('m','13.png', 'm.wav'), \
              "n":KeyData('n','14.png', 'n.wav'), \
              "o":KeyData('o','15.png', 'o.wav'), \
              "p":KeyData('p','16.png', 'p.wav'), \
              "q":KeyData('q','17.png', 'q.wav'), \
              "r":KeyData('r','18.png', 'r.wav'), \
              "s":KeyData('s','19.png', 's.wav'), \
              "t":KeyData('t','20.png', 't.wav'), \
              "u":KeyData('u','21.png', 'u.wav'), \
              "v":KeyData('v','22.png', 'v.wav'), \
              "w":KeyData('w','23.png', 'w.wav'), \
              "x":KeyData('x','24.png', 'x.wav'), \
              "y":KeyData('y','25.png', 'y.wav'), \
              "z":KeyData('z','26.png', 'z.wav'), \
              " ":KeyData(' ','transparent.png', None), \
              "1":KeyData('1','26.png', 'z.wav')}
    
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.background = self.load_image('mountainBG.png')
        self.letters = ""
        self.typedKeyData = []
        self.colorMod = 0
        self.bottomTiles = []
        self.screen = 0
        self.quit = False
        self.initMixer()
        self.initSounds()
        #pygame.key.set_repeat(200,  200)
        
        self.animating = False
        self.afterAnimating = False
        self.notes = None
        self.notesDone = []
        
            
    def initMixer(self):
        # Initialize mixer
        # The mixer is used by pygame to load and play the sound files
         pygame.mixer.init(MIXER_FREQ, MIXER_BITSIZE, MIXER_CHANNELS, MIXER_BUFFER)
         pygame.mixer.music.set_volume(MIXER_VOLUME)
    
    def initSounds(this):
        for keyCode in this.letterMap:
            this.letterMap[keyCode].loadSound()
            
    def initTyping(self):
        self.colorMod = 0
        #clear the whole screen
        self.screen.blit(self.background, (0, 0))
        #update the display
        pygame.display.update()
        
    def run(self):
        #get screen
        self.screen = pygame.display.get_surface()
        self.initTyping()
        #update the display
        pygame.display.flip()
        #print screen.get_height()
        
        #start the game loop
        while not self.quit:
            self.doPaint = False
            #Yield to GTK?
            while gtk.events_pending():
                gtk.main_iteration()
                
            if self.animating:
                self.doPaint = True
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
                
                if note.frame == ANIM_FRAME_TIME - FPS / 3:
                    note.play()
                if note.isDone():
                    self.notesDone.append(note)
                    self.currentNote += 1
                    if self.currentNote >= len(self.notes):
                        self.stopAnimating()
                
            #Event processing loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    break
                elif event.type == KEYDOWN:
                    self.doKeyDown(event)
            #End of event processing loop
            
            if self.doPaint:
                pygame.display.update()
            self.clock.tick(FPS)
        print "quiting"    
        #End of main loop
        pygame.quit()
                
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
            if event.unicode in self.letterMap:
                self.letters += event.unicode
                self.addTile(self.screen,  self.bottomTiles,  event.unicode)
        if event.key == K_BACKSPACE:
            if len(self.letters) > 0:
                self.colorMod -= 1
                self.letters = self.letters[:-1]
                self.bottomTiles.pop()
                self.redrawTiles(self.screen,  self.background, self.bottomTiles)
        elif (event.key == K_RETURN):
            self.initAnimating()
                
    
        
    def initAnimating(self):
        self.animating = True
        self.notes = []
        self.notesDone = []
        self.colorMod = 0
        self.currentNote = 0
        for x in range(len(self.letters)):
            if ord(self.letters[x]) >= 97 and ord(self.letters[x]) <= 122:
                noteImage = self.load_letter("Note.png")
            elif ord(self.letters[x]) == 32:
                noteImage = self.load_letter("transparent.png")
            note = ImageObject(noteImage, x*40+10, self.screen.get_height() - 50,  3,  self.letterMap[self.letters[x]])
            note.speed = ANIM_SPEED_START + (ord(note.keyData.ascii)-97) * ANIM_SPEED_INCREASE
            self.notes.append(note)
            self.colorMod += 1
    
    def stopAnimating(self):
        self.animating = False
        self.afterAnimating = True
        self.letters = ""
        self.notes = None
        self.notesDone = None
        self.bottomTiles = []

    def load_image(this,  name):
        path = os.path.join(os.path.dirname(__file__), 'Images', name)
        image = pygame.image.load(path)
        return image
    
    
    
    def get_path(this):
        colorFile = ""
        colorModTemp = this.colorMod  % 8
        
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
        self.doPaint = True
        
        
    def addTile(this,  screen,  bottomTiles,  unicode):
        
        #load the image
        letterTileImage = this.load_letter(this.letterMap[unicode].imageFile)
        letterTile = ImageObject(letterTileImage,  (len(bottomTiles)*40+10), screen.get_height() - 50, 1, this.letterMap[unicode])
        #draw the image
        screen.blit(letterTile.image, letterTile.pos)
        #add to array
        bottomTiles.append(letterTile)
        #update the display
        this.doPaint = True
        this.colorMod += 1
        
#first to run when program starts
def main():    
    pygame.init()
    pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
    game = WordChimes()
    game.run()
    
if __name__ == '__main__': 
    main()
