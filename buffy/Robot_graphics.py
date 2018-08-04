from graphics import *
import pygame
import sys
import random

pygame.init()

# Define some colors into a dictionary
# colorName = (r,g,b)
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "darkBlue": (0, 0, 128),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "pink": (255, 200, 200),
    "purple": (160, 32, 240),
    "yellow": (255, 255, 0),
    "lightblue": (102, 255, 255),
    "robotgrey": (192, 192, 192),
    "darkgrey": (162, 162, 162),
    "darkestgrey": (96, 96, 96)
}

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Buffy the Buffer Robot")
green = (0, 255, 0)
screen.fill(colors["green"])

""""""

class Head():
    def __init__(self):
        # Head
        pygame.draw.rect(screen, colors["black"], [250, 175, 100, 100], 0)
        # self.image = pygame.image.load(INSERT PATH)


class Neck():
    def __init__(self):
        # Neck
        pygame.draw.rect(screen, colors["black"], [292, 275, 16, 25], 0)


class Arms():
    def __init__(self):
        # right arm
        pygame.draw.line(screen, colors["black"], [400, 350], [325, 390], 20)
        # left arm
        pygame.draw.line(screen, colors["black"], [200, 350], [275, 390], 20)
        # right arm
        # pygame.draw.line(screen, colors["black"], [400,350], [450,380], 20)
        # left arm
        # pygame.draw.line(screen, colors["black"], [200,350], [150,380], 20)


class Legs():
    def __init__(self):
        # right leg
        pygame.draw.line(screen, colors["black"], [350, 560], [375, 600], 20)
        # left leg
        pygame.draw.line(screen, colors["black"], [250, 560], [225, 600], 20)


class Body():
    def __init__(self):
        # Body
        pygame.draw.rect(screen, colors["red"], [200, 300, 200, 260], 0)


class Testtube():
    def __init__(self, c):
        # Testtube
        self.color_testtube = colors[c]
        pygame.draw.rect(screen, self.color_testtube, [275, 400, 50, 120], 0)
        # pygame.draw.rect(screen, self.color_testtube, [450,480,50,120], 0)


class Bubble():
    def __init__(self):
        # Bubble
        pygame.draw.rect(screen, colors["pink"], [275, 400, 5, 5], 0)


# newbody = Body()
# newhead = Head()
# newarms = Arms()
# newlegs = Legs()
# newneck = Neck()
# newtube  = Testtube("blue")
# newbubble = Bubble()
pygame.display.update()

""""""

y1 = 400
y2 = 400
width = 10
height = 10
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        y2 += vel

    if keys[pygame.K_UP]:
        y2 -= vel

    if keys[pygame.K_LEFT]:
        y1 += vel

    if keys[pygame.K_RIGHT]:
        y1 -= vel

    screen.fill(colors["green"])
    # Hat
    pygame.draw.line(screen, colors["robotgrey"], [292, 175], [265, 140], 10)
    # Hat ball
    pygame.draw.circle(screen, colors["darkestgrey"], [265, 140], 7, 0)
    # right ear
    # pygame.draw.line(screen, colors["darkestgrey"], [350,190], [375,190], 10)
    # left ear
    # pygame.draw.line(screen, colors["darkestgrey"], [250,190], [225,190], 10)
    # Head
    pygame.draw.rect(screen, colors["robotgrey"], [250, 175, 100, 100], 0)
    # Mouth straight
    pygame.draw.line(screen, colors["white"], [290, 250], [310, 250], 10)
    # right eye
    pygame.draw.circle(screen, colors["lightblue"], [325, 200], 10, 0)
    # left eye
    pygame.draw.circle(screen, colors["lightblue"], [275, 200], 10, 0)
    # right pupil
    pygame.draw.circle(screen, colors["black"], [325, 200], 4, 0)
    # left pupil
    pygame.draw.circle(screen, colors["black"], [275, 200], 4, 0)
    # Neck
    pygame.draw.rect(screen, colors["black"], [292, 275, 16, 25], 0)
    # right leg
    pygame.draw.line(screen, colors["darkestgrey"], [350, 560], [350, 600], 30)
    # left leg
    pygame.draw.line(screen, colors["darkestgrey"], [250, 560], [250, 600], 30)
    # body
    pygame.draw.rect(screen, colors["robotgrey"], [200, 300, 200, 260], 0)
    # right knee
    pygame.draw.circle(screen, colors["darkgrey"], [350, 560], 15, 0)
    # left knee
    pygame.draw.circle(screen, colors["darkgrey"], [250, 560], 15, 0)
    # testtube outer
    pygame.draw.rect(screen, colors["white"], [268, 392, 64, 120], 0)
    # testtube
    pygame.draw.rect(screen, colors["blue"], [270, 390, 60, 120], 0)
    # testtube bottom
    ###
    # right arm
    pygame.draw.line(screen, colors["darkestgrey"], [400, 350], [325, 390], 23)
    # left arm
    pygame.draw.line(screen, colors["darkestgrey"], [195, 330], [195, 360], 23)
    # right upperarm
    pygame.draw.line(screen, colors["darkestgrey"], [405, 330], [405, 360], 17)
    # left upperarm
    pygame.draw.line(screen, colors["darkestgrey"], [200, 350], [275, 390], 17)
    # right shoulder
    pygame.draw.circle(screen, colors["darkgrey"], [400, 320], 20, 0)
    # left shoulder
    pygame.draw.circle(screen, colors["darkgrey"], [200, 320], 20, 0)
    # right drop
    pygame.draw.rect(screen, colors["purple"], [313, y1, width, height], 0)
    # left drop
    pygame.draw.rect(screen, colors["yellow"], [280, y2, width, height], 0)
    pygame.display.update()

pygame.quit()
