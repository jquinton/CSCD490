import pygame
import random
import Tkinter as tk
import os
 
# Initialize the game engine
pygame.init()

color=[]
BLACK = [ 0, 0, 0]
WHITE = [255,255,255]
HEIGHT = 800 
WIDTH = 600
NOTE_CIRCLE_RADIUS = 18
NOTE_STARTING_Y = 500
 
# Set the height and width of the screen
size=[HEIGHT,WIDTH]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Listen2ABC")
 
# Create empty arrays for shape parts
circle_list=[]
line_list_start=[]
line_list_stop=[]
flag_list_stop=[]

# Create empty array for sound files
sound_list=[]

# fill sound array with sound files
i = 0
while i < 25 :
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
 
#play_sound
def play_sound(sound_path):
    try:
        pygame.mixer.music.load(sound_path)
        print "loaded %s" % sound_path
    except:
        print "%s failed to load" % sound_path
        return
    pygame.mixer.music.play()

# Loop n times and add a note shape in each position. Also generate random color for each note.
for i in range(100, 750, 50): #(start, stop, increment)
    x=i
    y = NOTE_STARTING_Y
    circle_list.append([x,y])
    line_list_start.append([x+15, y])
    line_list_stop.append([x+15, y-40])
    flag_list_stop.append([x+25, y-20])
    r=random.randrange(100,255)
    g=random.randrange(100,255)
    b=random.randrange(100,255)
    color.append([r, g, b])
 
clock = pygame.time.Clock()

#temporarly have processingNeeded set here. This should be set true when the user clicks on listen
processingNeeded = True

 
#Loop until the user clicks the close button.
done=False
while done==False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 
 
    # Make the screen background temporarily black until image processing is figured out
    screen.fill(BLACK)
 
    #check to see if the animating loop needs to be entered. This should be set true when the
    #user clicks on listen
    if processingNeeded:
        # Process each shape in the list
        
        tempLetter = "A" #temporary simulation of different note heights
        for i in range(len(circle_list)):
            
            #temporary simulation of different note heights 
            tempheight = i * 24 + 100
            tempAsciiVal = ord(tempLetter)
            tempAsciiVal += 1
            tempLetter = chr(tempAsciiVal)
            
            #draw a note assending for height pixels from the top of the screen
            #stop is the height of the screen - the starting position of the notes - tempheight + 1 to allow letter 
            #animation when the note reaches the top.
            for k in range(0, HEIGHT - (HEIGHT - NOTE_STARTING_Y) - tempheight + 1, 1): #(start, stop, increment)
                # clear the last shape
                clearRect = pygame.Rect(((circle_list[i][0] - (NOTE_CIRCLE_RADIUS)),  line_list_stop[i][1]),  (NOTE_CIRCLE_RADIUS * 3, NOTE_CIRCLE_RADIUS * 4))
                pygame.draw.rect(screen, BLACK, clearRect )
                # Draw the shape (music note?)
                pygame.draw.circle(screen,color[i],circle_list[i],NOTE_CIRCLE_RADIUS)
                pygame.draw.line(screen,color[i],line_list_start[i], line_list_stop[i],  (NOTE_CIRCLE_RADIUS / 4))
                pygame.draw.line(screen,color[i],line_list_stop[i], flag_list_stop[i],  (NOTE_CIRCLE_RADIUS / 4))
                          
                # Move the shape up one pixel if 'tempheight' pixels from the top has not been reached
                # circle_list[i][x] where x=1 means move vertical or x=0 means move horizontal
                xd, yd = circle_list[i]
                if yd > tempheight:
                    circle_list[i][1]-=1
                    line_list_start[i][1]-=1
                    line_list_stop[i][1]-=1
                    flag_list_stop[i][1]-=1
                    
                    # draw the letter
                    if pygame.font:
                        font = pygame.font.Font(None, 22)
                        text = font.render(tempLetter, 1, BLACK)
                        textpos = pygame.Rect((circle_list[i][0] - (NOTE_CIRCLE_RADIUS / 4), circle_list[i][1] - (NOTE_CIRCLE_RADIUS / 4)), (10, 10))
                        screen.blit(text, textpos)
                 
                # The shape has reached its destination. animate the letter
                else:
                    #since the shape has reached its destination, this is when we want to call play_sound to play the midi file
                    play_sound(sound_list[tempAsciiVal - 65])
                    # draw the letter increasing size 
                    for j in range(24, 32, 1):#(start, stop, increment)
                        if pygame.font:
                            #clear the old letter
                            pygame.draw.circle(screen,color[i],circle_list[i],NOTE_CIRCLE_RADIUS)
                            
                            #draw the new letter
                            font = pygame.font.Font(None, j)
                            text = font.render(tempLetter, 2, BLACK)
                            textpos = pygame.Rect((circle_list[i][0] - (NOTE_CIRCLE_RADIUS / 4)-(j-22), circle_list[i][1] - (NOTE_CIRCLE_RADIUS / 4)-(j-22)), (10, 10))
                            screen.blit(text, textpos)
                            
                            clock.tick(40)
                            
                        # Update the screen with the drawing
                        pygame.display.flip()
                        
                    # draw the letter decreasing size 
                    for j in range(30, 22, -1):#(start, stop, increment)
                        if pygame.font:
                            #clear the old letter
                            pygame.draw.circle(screen,color[i],circle_list[i],NOTE_CIRCLE_RADIUS)
                            
                            #draw the new letter
                            font = pygame.font.Font(None, j)
                            text = font.render(tempLetter,  2, BLACK)
                            textpos = pygame.Rect((circle_list[i][0] - (NOTE_CIRCLE_RADIUS / 4)-(j-22), circle_list[i][1] - (NOTE_CIRCLE_RADIUS / 4)-(j-22)), (10, 10))
                            screen.blit(text, textpos)
                            
                            clock.tick(40)
                            
                        # Update the screen with the drawing
                        pygame.display.flip()
         
                
                # Update the screen with the drawing
                pygame.display.flip()
                clock.tick(200)
        
        # done animating. no need to continue looping        
        processingNeeded = False
        
pygame.quit ()
