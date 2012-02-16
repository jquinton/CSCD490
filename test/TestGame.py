#!/usr/bin/python
import pygame
import gtk
import os

class TestGame:
    def load_image(self, name):
        path = os.path.join('Images/', name)
        return pygame.image.load(path).convert()
    
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.background = self.load_image('background.bmp')
        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False

    # The main game loop.
    def run(self):
        self.running = True    
            
        screen = pygame.display.get_surface()
        screen.blit(self.background,  (0, 0))

        while self.running:
            # Pump GTK messages.
            while gtk.events_pending():
                gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
            
            # Move the ball
            if not self.paused:
                self.x += self.vx
                if self.x > screen.get_width() + 100:
                    self.x = -100
                
                self.y += self.vy
                if self.y > screen.get_height() - 100:
                    self.y = screen.get_height() - 100
                    self.vy = -self.vy
                
                self.vy += 5;
            
            # Clear Display
            screen.blit(self.background,  (0, 0))

            # Draw the ball
            pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 100)
                    
            # Flip Display
            pygame.display.flip()  
            
            # Try to stay at 30 FPS
            self.clock.tick(60)

# This function is called when the game is run directly from the command line:
# ./TestGame.py 
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = TestGame() 
    game.run()

if __name__ == '__main__':
    main()

