import pygame, os, sys

class textField:
        """ """
        
        def __init__(self):
                """ """
                
                self.text = ''
                self.fontPath = ''
                self.position = [50,50,350,70]
                self.fontSize = 10
                self.font = pygame.font.Font(None,self.fontSize*2)
                self.renderList = []
                self.searchDict = {}
                self.textColor = 0,0,0
                self.alpha = 175
                self.modified = False
                
                self.addLayer('Text', pygame.Surface((0,0)).convert())
                
        
        def addText(self, s):
                """ """
                
                self.text = self.text + s
                self.modified = True
                return self.text
                
        
        def setFont(self, basePath, font):
                """ """
                
                self.fontPath = os.path.join(*basePath.split('/') + [font])
                return self.fontPath
                
        
        def setFontSize(self, size):
                """ """
                
                self.fontSize = size
                return self.fontSize
                
        
        def setPosition(self, pos):
                """ """
                
                if len(pos)==2: self.position[:2] = pos #could cause problems if pos is a tuple
                else: self.position = pos
                return None
                
        
        def addLayer(self, name, surface, pos=(0,0), zIndex = 1):
                """ """
                
                self.searchDict[name] = len(self.renderList)
                self.renderList.append([name, surface, pos, zIndex])
#               we will most likely render this box more often than we will add layers. Best to sort the
#               layers when we add them and make sure they stay sorted.
                self.renderList.sort(lambda a,b : a[3] > b[3] and 1 or -1)
                return None
                
        
        def renderText(self):
                """ """
                
#               font = pygame.font.Font(self.fontPath, self.fontSize*2)
                font = pygame.font.Font(None, 22)
                
                n = 0
                for i in self.text.split('\n'):
                        text = self.font.render(i, 1, self.textColor)
                        textPos = text.get_rect(left=10, top=n*15 + 10)
                        self.renderList[self.searchDict['Text']][1].blit(text, (0,0,350,350))
                        n = n+1
                        
                
                return None
                
        
        def update(self):
                """ """
                
                if self.modified: 
                        print 'renderd text'
                        self.renderText()
                        self.modified = False
                
        
        def render(self, s):
                """
                None render(<obj surface> s)
                
                renders the current text field onto the surface s.
                """
                
                for i in self.renderList:
                        position = (i[2][0] + self.position[0], i[2][1] + self.position[1])
                        s.blit(i[1], (0,0,350,350))
                        
                
                return None
                
        



import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('/home/vocifer/Desktop/165-1920.jpg').convert()
screen.blit(background, (0,0))

pygame.mouse.set_visible(False)



a = textField()
a.setFont('../data/fonts/','GenI102.TTF')
a.addText('this is a \nnew \nline, and more shit.')
a.update()

clock = pygame.time.Clock()

if __name__ == '__main__':
        
        
        import sys
        
        pygame.init()
        
        screen = pygame.display.set_mode((800, 600))
        background = pygame.image.load('/home/vocifer/Desktop/165-1920.jpg').convert()
        screen.blit(background, (0,0))
        
        pygame.mouse.set_visible(False)
        
        
        
        a = textField()
        a.setFont('../data/fonts/','GenI102.TTF')
        a.addText('this is a \nnew \nline, and more shit.')
        a.update()
        
        clock = pygame.time.Clock()
        
        while True:


                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                
                screen.blit(background, (0,0))
                
                a.update()
                
                
                a.render(screen)
                
                
                pygame.display.flip()
                clock.tick(60)
                
        
