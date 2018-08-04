from graphics import *
import pygame

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
    "yellow": (255, 255, 0)
}

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Buffy the Buffer Robot")
green = (0, 255, 0)
screen.fill(colors["green"])


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


newbody = Body()
newhead = Head()
newarms = Arms()
newlegs = Legs()
newneck = Neck()
newtube = Testtube("blue")
# newbubble = Bubble()
pygame.display.update()

x = 285
y = 400
width = 5
height = 5
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        y += vel

    if keys[pygame.K_UP]:
        y -= vel

    # screen.fill(colors["blue"])
    pygame.draw.rect(screen, colors["purple"], [315, 400, width, height], 0)
    pygame.draw.rect(screen, colors["yellow"], [x, y, width, height], 0)
    pygame.display.update()

pygame.quit()