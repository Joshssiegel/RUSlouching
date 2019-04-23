import pygame as pg
import time
import random

pg.init()
display_width = 800
display_height = 600

# defining the black and white ranges for the game
# (R,G,B)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
oof = (69,69,69)
bkg = (221,160,221)

########################################################################################################################
#######      START Window      #########################################################################################
########################################################################################################################
class Start:

    def __init__(self, rect, command):
        self.rect = pg.Rect(rect)
        self.image = pg.Surface(self.rect.size).convert()
        self.image.fill(black)
        self.function = command

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.function()

    # def addText(self, surf):
    #     self.surf.blit(self.font.render('START', True, (255,0,0)), (200, 100))
    #     pg.display.update()

    def draw(self, surf):
        surf.blit(self.image, self.rect)
        font = pg.font.Font('freesansbold.ttf',30)
        new_game_text = font.render("START", False, red)
        surf.blit(new_game_text, self.rect)
        # addText(self, surf)



def button_was_pressed():
    # pg.display.set_mode((0,0))
    done = True
    print('button_was_pressed')

screen = pg.display.set_mode((600,200))
screen.fill((white))
done = False
btn = Start(rect=(250,50,100,35), command=button_was_pressed)

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            quit()
        # btn.get_event(event)
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            done = True
    btn.draw(screen)
    pg.display.update()

########################################################################################################################
#######      Slouching Code      #######################################################################################
########################################################################################################################

gameDisplay = pg.display.set_mode((50, 50)) #set_mode((width x height)) <== one parameter that is a tuple
soeImg = pg.image.load('pics/rutgers-soe-logo-2.png')


def logo(x,y):
    gameDisplay.blit(soeImg, (x, y))

# logo(0,0)

def text_objects(text, font):
    textSurface = font.render(text, True, oof)
    return textSurface, textSurface.get_rect()

def show_message(msg):
    pg.display.set_caption('RU Slouching') #name of project
    gameDisplay.fill(bkg)
    largeText = pg.font.Font('freesansbold.ttf',95)
    textSurf, textRect = text_objects(msg, largeText)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    logo(display_width/2+50, display_height-150)
    pg.display.update()

def slouching(isSlouching):
    pg.init()
    # slouching(1)
    # slouching(0)
    gameDisplay = pg.display.set_mode((display_width,display_height)) #set_mode((width x height)) <== one parameter that is a tuple
    msg = ""
    if(isSlouching==1):
        msg = "slouching"
    else:
        msg = "NOT slouching"
    show_message(msg)
    time.sleep(3)
    # pg.display.quit()
    # quit()
