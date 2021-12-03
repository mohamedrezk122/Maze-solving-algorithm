from pygame.locals import *
import pygame ,sys
import numpy as np
from PIL import Image
from time import sleep
from maze import Maze
from bfs import BFS


pygame.init()

clock = pygame.time.Clock()
im = Image.open(r"./images_in/tiny.png")


width = 600
height = 600

screen = pygame.display.set_mode((width, height))


def hex2rgb(hexcode:str):

    color = []
    hexcode = hexcode.replace('#' , '')
    color.append(int(hexcode[0:2] , 16))
    color.append(int(hexcode[2:4] , 16))
    color.append(int(hexcode[4:6] , 16))

    return tuple(color)

class Scene:

    def __init__(self , *args):


        font = pygame.font.SysFont("consolas.ttf", 50)
        text = font.render('Maze Solving Algorithm', True , hex2rgb('#000000'))
        img = pygame.image.load('image.png')

        screen.fill(hex2rgb('#FFFFFF'))
        screen.blit(img , (150, 30))

        screen.blit(text , (95, 300))

        b1 = Button(150 ,50  , 225 ,450 , 'Solve' , screen , hex2rgb('#F63F3F') , hex2rgb('#FFFFFF') , Track)

        b2 = Button(150 ,50  , 225 ,525 , 'Quit' , screen , hex2rgb('#F63F3F') , hex2rgb('#FFFFFF') , quit )

        lst = [b1 , b2]
        while True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in lst:
                            if button.rect.collidepoint(event.pos):

                                button.press(*args)

                elif event.type == QUIT :

                    pygame.quit()
                    quit()
                    sys.exit()

            pygame.display.flip()

            clock.tick(60)

class Button:

    def __init__(self, width , height , x , y, text , display , color , text_color , func = None ):

        self.width = width
        self.height = height
        self.x  = x
        self.y = y
        self.func = func
        self.display = display
        self.color = color
        self.text = text
        self.text_color = text_color


        Button.draw(self)
        Button.add_text(self)


        pygame.display.update()

    def press(self ,*args):

        if self.func is not quit:

            self.func(*args)

        else:

            self.func()

    def draw(self):

        self.rect = pygame.draw.rect(self.display, self.color , (self.x , self.y ,self.width , self.height), border_radius = 10 )

        pygame.display.flip()

    def add_text(self):

        font = pygame.font.SysFont("arial.ttf", 30)
        text = font.render(self.text , True ,self.text_color )
        wid = text.get_width()
        hig = text.get_height()
        self.display.blit(text , (self.x + ((self.width - wid)*.5) , (self.y + ((self.height - hig)*.5))))


    def hover(self , pos):

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        else:
            return False

class Track:

    def __init__(self, maze , solution):


        self.maze = maze
        image = self.maze.im
        self.solution = solution


        screen.fill(hex2rgb('#FFFFFF'))


        self.img = self.maze.imdata
        width2 , height2 = image.size
        self.wid = int(width/ width2)
        self.hig = int(height / height2)

        Track.loop(self)

    def draw(self):

        for pos , cell in np.ndenumerate(self.img):

            if cell == 0:
                pygame.draw.rect(screen , hex2rgb('#000000'),( pos[1]*self.hig, pos[0]*self.wid, self.wid , self.hig))

            else:

                pygame.draw.rect(screen , hex2rgb('#FFFFFF'), ( pos[1]*self.hig, pos[0]*self.wid, self.wid , self.hig))

                if pos in self.maze.node:

                    pygame.draw.circle(screen , hex2rgb('#698FDD'),( pos[1]*self.hig + .5* self.hig, pos[0]*self.wid+.5* self.hig),radius = 5 , width = 1 )

        pygame.display.update()

    def path(self , x , y):


        pygame.draw.rect(screen , hex2rgb('#B4F3B5') ,( x*self.hig , y*self.wid  , self.wid , self.hig) )

        pygame.display.update()

    def tracker(self , x , y):


        pygame.draw.rect(screen , hex2rgb('#1DD15D') ,( x*self.hig , y*self.wid  , self.wid , self.hig) )
        pygame.display.update()


    def loop(self):
        while True:

            Track.draw(self)
            for x,y in self.solution:

                Track.tracker(self,y,x)
                sleep(.3)
                Track.path(self , y , x)

            sleep(1)
            break
            for event in pygame.event.get():

                if event.type == QUIT:

                    pygame.quit()
                    quit()
                    sys.exit()

            pygame.display.flip()

            clock.tick(60)
