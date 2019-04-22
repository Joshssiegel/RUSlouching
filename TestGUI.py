import pygame
import time
import random

pygame.init()
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
bkg = (175,200,238)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #set_mode((width x height)) <== one parameter that is a tuple
soeImg = pygame.image.load('pics/rutgers-soe-logo-2.png')

def logo():
    gameDisplay.blit(soeImg, (display_width/2+50, display_height-150))

def text_objects(text, font):
    textSurface = font.render(text, True, oof)
    return textSurface, textSurface.get_rect()

def show_message(msg):
    pygame.display.set_caption('RU Slouching') #name of project
    gameDisplay.fill(bkg)
    largeText = pygame.font.Font('freesansbold.ttf',95)
    textSurf, textRect = text_objects(msg, largeText)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    logo()
    pygame.display.update()

def slouching(isSlouching):
    # slouching(1)
    # slouching(0)
    gameDisplay = pygame.display.set_mode((display_width,display_height)) #set_mode((width x height)) <== one parameter that is a tuple
    msg = ""
    if(isSlouching==1):
        msg = "slouching"
    else:
        msg = "NOT slouching"
    show_message(msg)
    time.sleep(3)
    # pygame.display.quit()
    # quit()
