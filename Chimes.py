import pygame
import random
import Tkinter as tk
 
# Initialize the game engine
pygame.init()

color=[]
black = [ 0, 0, 0]
white = [255,255,255]
height = 800 
width = 600
 
# Set the height and width of the screen
size=[height,width]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Listen2ABC")
 
# Create empty arrays for shape parts
circle_list=[]
line_list_start=[]
line_list_stop=[]
flag_list_stop=[]
 
# Loop n times and add a note shape in each position. Also generate random color for each note.
for i in range(100, 750, 50): #(start, stop, increment)
    x=i
    y=500
    circle_list.append([x,y])
    line_list_start.append([x+13, y])
    line_list_stop.append([x+13, y-40])
    flag_list_stop.append([x+25, y-20])
    r=random.randrange(0,255)
    g=random.randrange(0,255)
    b=random.randrange(0,255)
    color.append([r, g, b])
 
clock = pygame.time.Clock()
 
#Loop until the user clicks the close button.
done=False
while done==False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 
 
    # Make the screen background temporarily black until image processing is figured out
    screen.fill(black)
 
    # Process each shape in the list
    for i in range(len(circle_list)):
            # Draw the shape (music note?)
            pygame.draw.circle(screen,color[i],circle_list[i],15)
            pygame.draw.line(screen,color[i],line_list_start[i], line_list_stop[i],  3)
            pygame.draw.line(screen,color[i],line_list_stop[i], flag_list_stop[i],  3)
           
            # Move the shape up one pixel if 100 pixels from the top has not been reached
            # circle_list[i][x] where x=1 means move vertical or x=0 means move horizontal
            xd, yd = circle_list[i]
            if yd > 100:
                circle_list[i][1]-=1
                line_list_start[i][1]-=1
                line_list_stop[i][1]-=1
                flag_list_stop[i][1]-=1
         
    # Update the screen with the drawing
    pygame.display.flip()
    clock.tick(40)
             
pygame.quit ()
